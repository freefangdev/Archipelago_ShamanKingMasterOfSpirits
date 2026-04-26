import logging
from typing import TYPE_CHECKING, Dict, Any
from worlds._bizhawk.client import BizHawkClient
from worlds._bizhawk import RequestFailedError, read, write
from .game_data import traps, collectible_location_flags, key_location_flags, spirit_location_flags, spiritSlotFlagDict, spiritCollectionFlagDict, itemDataDict, ItemData, MemoryLocations, FlagData, weapon_progression_dict, defence_progression_dict, SpiritData, itemData, chest_addresses
from .items import ITEM_ID_TO_ITEM
from .names import ItemTypes, MemoryKeys, MemoryDomainKeys, Names, Options, spirit_flag_mods
from .locations import LOCATION_NAME_TO_ID

if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext

logger = logging.getLogger("Client")
memory_locations = MemoryLocations()
max_bag_weight = 10
max_bag_slots = 10

class State:
    def __init__(self):
        self.death_trigger = False #Todo Death link
        self.exit_stage_trigger = False
        self.trap_duration = 0x02FF
        self.traps_to_trigger:list[str] = []
        self.receive_amount:int = 0
        self.yen_to_add:int = 0
        self.magatama_to_add:int = 0
        self.tome_to_add:int = 0
        self.leaf_to_add:int = 0
        self.rock_to_add:int = 0
        self.skeleton_to_add:int = 0
        self.spirits_to_add:list[str] = []
        self.spirit_slots_to_add:list[str] = []
        self.bag_items_to_add:list[str] = []
        self.weapons_to_add:list[str] = []
        self.defence_to_add:list[str] = []

    def reset(self):
        self.__init__()

state = State()

def cmd_trigger_trap(self, trap_name: str, trap_length: str) -> None:
    """Give a trap"""
    global state
    
    if trap_name is not None and trap_name in traps:
        state.traps_to_trigger.append(trap_name)
        logger.info(f"Set trap type {trap_name}")
        
    if trap_length is not None:
        state.trap_duration = min(int(trap_length), int(0xFFFF))
        logger.info("Set trap length")

    logger.info("Trap set")

def cmd_trigger_death(self) -> None:
    """Die"""
    global state
    state.death_trigger = True
    logger.info("Death set")

def cmd_exit_stage(self) -> None:
    """Exit current stage"""
    global state
    state.exit_stage_trigger = True
    logger.info("Exit stage set")
    
def cmd_slot_data(self):
    """Prints slot data settings for the connected seed"""
    for key in self.ctx.slot_data.keys():
        self.output(str(key) + ": " + str(self.ctx.slot_data[key]))
            
def apply_mods(writes) -> None:
    #Disable gaining vanilla items when picking up hp/sp upgrades
    writes.append(memory_locations.make_write(MemoryKeys.DISABLE_VANILLA_HP_SP_PICKUP, 0x7E6A))
    #Disable gaining vanilla items when picking up spirit slot upgrades
    writes.append(memory_locations.make_write(MemoryKeys.DISABLE_VANILLA_SPIRIT_SLOT_PICKUP, 0x7E6A))
    #Disable item pickup message
    writes.append(memory_locations.make_write(MemoryKeys.DISABLE_GROUNDED_PICKUP_MESSAGE, 0xDB0A))
    #Disable vanilla chest rewards by setting the reward count for each chest to one 10 yen coin
    #sometimes multiple can show up as the game uses multiple chests in one location for a chest
    #with different items
    for address in chest_addresses:
        writes.append((address, [0x01], "ROM"))
        writes.append((address+2, [0x00], "ROM"))
    #Separate key collection from having the key, move collection status to bit 4
    writes.append(memory_locations.make_write(MemoryKeys.KEY_COLLECTION_BIT_MOD, 16))
    #Change location spirit collection writes from 235b to 232c in order to separate spirit location to spirit in inventory  
    for spirit_flag_mod in spirit_flag_mods:
        writes.append(memory_locations.make_write(spirit_flag_mod, 0x60))
    #Change tome save location/mechanism
    #Todo replace with non-locking fix
    #writes.append(memory_locations.make_write(MemoryKeys.TOME_LOCATION_MOD, 0xAF352C7801342C7082E0))
    #Loaded message in map scroller
    writes.append((0x267D40, b"Archipelago loaded successfully!", "ROM"))
    
def apply_options(writes, options) -> None:
    #if options[Options.Early_Totem_Spirit_Locations] == 1: #Todo: figure out options
        #Enable Totem Spirit locations before Silva/Silver boss
        writes.append(memory_locations.make_write(MemoryKeys.TOTEM_SPIRIT_LOCATION_MOD_1, 0))
        writes.append(memory_locations.make_write(MemoryKeys.TOTEM_SPIRIT_LOCATION_MOD_2, 0))
        
    #if options[Options.Disable_Splash_Art_When_Using_Spirits] == 1:
        #Disable random spirit splash effect
        writes.append(memory_locations.make_write(MemoryKeys.DISABLE_SPIRIT_SPLASH, 0))

class ShamanKingMasterOfSpiritsClient(BizHawkClient):
    game = Names.Game_Name
    system = "GBA"

    async def validate_rom(self, ctx: "BizHawkClientContext") -> bool:
        try:
            logger.warning("Sk check")
            # Check Correct name
            game_name = await read(ctx.bizhawk_ctx, [
                #Short name from rom header
                (0xA0, 11, "ROM"),
                #Full name from the credits
                (0x608BC, 17, "ROM"),
                #Current screen type, 0 for start menu, 1 for world map, 2 for levels
                #(0x1DDD, 1, "IWRAM")
            ])
            
            if (game_name is None 
                    or game_name[0].decode("ascii") != "SHAMAN KING"
                    or game_name[1].decode("ascii") != "MASTER OF SPIRITS"):
                logger.warning(game_name)
                return False

        except UnicodeDecodeError:
            logger.warning("UnicodeDecodeError")
            return False
        except RequestFailedError:
            logger.warning("RequestFailedError")
            return False

        #Check if in the opening menu before patching
        #if game_name[2] != 0x0:
            logger.warning("Return to the start menu to validate the rom")
            return False
        
        #Set context
        ctx.game = self.game
        ctx.items_handling = 0b111  # remote items
        
        #Add custom commands
        ctx.command_processor.commands["trap"] = cmd_trigger_trap
        ctx.command_processor.commands["kill"] = cmd_trigger_death
        ctx.command_processor.commands["exitstage"] = cmd_exit_stage
        ctx.command_processor.commands["slotdata"] = cmd_slot_data
        
        writes = []
        #TODO: Settings stuff
        #Implement mods
        apply_mods(writes)
        apply_options(writes, ctx.slot_data)
        
        await write(ctx.bizhawk_ctx, writes)
        
        return True
    
    async def game_watcher(self, ctx: "BizHawkClientContext") -> None:
        from .items import item_table
        if ctx.server is None or ctx.server.socket.closed or ctx.slot_data is None:
            return
        
        global state
        
        (screen_type_bytes, 
         yoh_object_pointer_bytes, 
         event_flag_bytes, 
         bag_slot_bytes, 
         bag_weight_bytes, 
         leaves_bytes, 
         rocks_bytes, 
         skeletons_bytes, 
         yen_bytes, 
         hp_bytes, 
         max_hp_bytes, 
         max_hp_excl_buffs_bytes, 
         max_sp_bytes, 
         magatama_and_tome_count_bytes, 
         spirit_collection_bytes, 
         spirit_slot_bytes,
         weapon_slot_bytes,
         defence_slot_bytes,
         item_flags_bytes,
         key_flags_bytes,
         spirit_flags_bytes,) \
            = await read(ctx.bizhawk_ctx, [
            memory_locations.get_entry(MemoryKeys.CURRENT_SCREEN),
            memory_locations.get_entry(MemoryKeys.YOH_OBJECT),
            memory_locations.get_entry(MemoryKeys.EVENT_FLAGS),
            memory_locations.get_entry(MemoryKeys.BAG_SLOTS),
            memory_locations.get_entry(MemoryKeys.BAG_WEIGHT),
            memory_locations.get_entry(MemoryKeys.LEAF_COUNT),
            memory_locations.get_entry(MemoryKeys.ROCK_COUNT),
            memory_locations.get_entry(MemoryKeys.SKELETON_COUNT),
            memory_locations.get_entry(MemoryKeys.MONEY),
            memory_locations.get_entry(MemoryKeys.HP),
            memory_locations.get_entry(MemoryKeys.MAX_HP),
            memory_locations.get_entry(MemoryKeys.MAX_HP_EXCL_BUFFS),
            memory_locations.get_entry(MemoryKeys.MAX_SP),
            memory_locations.get_entry(MemoryKeys.MAGATAMA_AND_TOME_COUNT),
            memory_locations.get_entry(MemoryKeys.SPIRIT_COLLECTION),
            memory_locations.get_entry(MemoryKeys.SPIRIT_SLOTS),
            memory_locations.get_entry(MemoryKeys.WEAPON_SLOT),
            memory_locations.get_entry(MemoryKeys.DEFENCE_SLOT),
            memory_locations.get_entry(MemoryKeys.ITEM_FLAGS),
            memory_locations.get_entry(MemoryKeys.KEY_FLAGS),
            memory_locations.get_entry(MemoryKeys.SPIRIT_FLAGS),
        ])
        
        writes = []
        
        yoh_object_pointer_iwram = int.from_bytes(yoh_object_pointer_bytes, "little") - 0x3000000
        
        #Only do while in the level
        if self.is_in_gameplay_state(screen_type_bytes): 
            if state.death_trigger:
                #Set in-stage hp to zero
                writes.append((0x3636, [0x00], MemoryDomainKeys.IWRAM))
                state.death_trigger = False
                
            if state.exit_stage_trigger:
                # Exit stage
                writes.append((0x62D0, [0x02], MemoryDomainKeys.IWRAM))
                state.exit_stage_trigger = False

        for i, item in enumerate(ctx.items_received[state.receive_amount:]):
            item_id = item.item
            item_received = ITEM_ID_TO_ITEM[item_id]
            if isinstance(item_received, SpiritData):
                state.spirits_to_add.append(item_received.name)
            elif isinstance(item_received, ItemData):
                match item_received.itemType:
                    case ItemTypes.Attack_Upgrade:
                        state.weapons_to_add.append(item_received.name)
                    case ItemTypes.Upgrade:
                        logger.info('WIP') #Todo figure out thunder sword
                    case ItemTypes.Defence_Upgrade:
                        state.defence_to_add.append(item_received.name)
                    case ItemTypes.Spirit_Slot_Upgrade:
                        state.spirit_slots_to_add.append(item_received.name)
                    case ItemTypes.Health_Upgrade:
                        state.magatama_to_add = state.magatama_to_add + 1
                    case ItemTypes.Furyoku_Upgrade:
                        state.tome_to_add = state.tome_to_add + 1
                    case ItemTypes.Key:
                        logger.info('Keys are WIP')
                    case ItemTypes.Money:
                        state.yen_to_add = state.yen_to_add + item_received.price
                    case ItemTypes.Bag:
                        if item_received.proxyItemCount is not None:
                            state.bag_items_to_add.extend([item_received.proxyItem]*item_received.proxyItemCount)
                        else:
                            state.bag_items_to_add.append(item_received.name)
                    case ItemTypes.Consumable:
                        match item_received.name:
                            case Names.Leaf:
                                state.leaf_to_add = state.leaf_to_add + 1
                            case Names.Rock:
                                state.rock_to_add = state.rock_to_add + 1
                            case Names.Skeleton:
                                state.skeleton_to_add = state.skeleton_to_add + 1
                    case ItemTypes.Trap:
                        state.traps_to_trigger.append(item_received.name)
                    case _:
                        logger.info(f"{item_received.itemType} is not implemented!")
            else:
                logger.info(f"{type(item_received)} is not implemented!")
            
        # Add items to inventory, sell if they do not fit
        self.add_items_to_inventory(writes, bag_slot_bytes, bag_weight_bytes)
        
        # Handle weapons and defensive items
        self.update_equipment_value(writes, MemoryKeys.WEAPON_SLOT,     weapon_progression_dict,    weapon_slot_bytes,  state.weapons_to_add)
        self.update_equipment_value(writes, MemoryKeys.DEFENCE_SLOT,    defence_progression_dict,   defence_slot_bytes, state.defence_to_add)

        # Handle bitflag collections
        self.set_flags(writes, MemoryKeys.SPIRIT_COLLECTION,    spiritCollectionFlagDict,   spirit_collection_bytes,    state.spirits_to_add)
        self.set_flags(writes, MemoryKeys.SPIRIT_SLOTS,         spiritSlotFlagDict,         spirit_slot_bytes,          state.spirit_slots_to_add)

        # Add magatama & tome
        magatama_and_tome_count = int.from_bytes(magatama_and_tome_count_bytes, "little")
        magatama_and_tome_count = self.get_hp_upgrade(magatama_and_tome_count, screen_type_bytes, writes, yoh_object_pointer_iwram, max_hp_excl_buffs_bytes, max_hp_bytes)
        magatama_and_tome_count = self.get_sp_upgrade(magatama_and_tome_count, max_sp_bytes, writes)
        writes.append(memory_locations.make_write(MemoryKeys.MAGATAMA_AND_TOME_COUNT, magatama_and_tome_count))

        # Add yen, leaves, rocks & skeletons
        self.increment_memory_value(writes, MemoryKeys.MONEY,           yen_bytes,          state.yen_to_add,     99999999)
        self.increment_memory_value(writes, MemoryKeys.LEAF_COUNT,      leaves_bytes,       state.leaf_to_add,    99)
        self.increment_memory_value(writes, MemoryKeys.ROCK_COUNT,      rocks_bytes,        state.rock_to_add,    99)
        self.increment_memory_value(writes, MemoryKeys.SKELETON_COUNT,  skeletons_bytes,    state.skeleton_to_add,99)

        #Handle traps
        self.trigger_traps(state.traps_to_trigger, writes, yoh_object_pointer_iwram, screen_type_bytes)

        await write(ctx.bizhawk_ctx, writes)
        
        state.reset()
        state.receive_amount = len(ctx.items_received)
        
        new_checks = []

        #Handle chest and other in-level collectible checks
        for collection_location in collectible_location_flags:
            location_id = LOCATION_NAME_TO_ID[collection_location.name]
            if location_id not in ctx.checked_locations:
                is_checked = self.is_bit_set(item_flags_bytes[collection_location.address_offset], collection_location.bit)
                if is_checked:
                    new_checks.append(location_id)

        #Handle key checks
        for key_location in key_location_flags:
            location_id = LOCATION_NAME_TO_ID[key_location.name]
            if location_id not in ctx.checked_locations:
                is_checked = self.is_bit_set(key_flags_bytes[key_location.address_offset], key_location.bit)
                if is_checked:
                    new_checks.append(location_id)
                    
        #Handle spirit checks
        for spirit_location in spirit_location_flags:
            location_id = LOCATION_NAME_TO_ID[spirit_location.name]
            if location_id not in ctx.checked_locations:
                is_checked = self.is_bit_set(spirit_flags_bytes[spirit_location.address_offset], spirit_location.bit)
                if is_checked:
                    new_checks.append(location_id)

        #Handle boss & event checks

        for new_check_id in new_checks:
            ctx.locations_checked.add(new_check_id)
            await ctx.send_msgs([{"cmd": 'LocationChecks', "locations": [new_check_id]}])

    def trigger_traps(self, trap_names:list[str], writes: list[Any], yoh_object_pointer_iwram: int, screen_type_bytes: bytes):
        global state
        #Todo: Non-status traps
        status_effect = 0
        status_duration = 0
        if self.is_in_gameplay_state(screen_type_bytes):
            for trap_name in trap_names:
                status_effect = status_effect & traps[trap_name]
                status_duration = max(status_duration, state.trap_duration) #Todo: trap duration by type 
                
        if status_effect != 0:
            # Set status effect
            writes.append((yoh_object_pointer_iwram + 0x3C, status_effect.to_bytes(2, "little"),
                           MemoryDomainKeys.IWRAM))
            # Set status effect time
            writes.append(
                (yoh_object_pointer_iwram + 0x66, status_duration.to_bytes(2, "little"), MemoryDomainKeys.IWRAM))

    @staticmethod
    def is_in_gameplay_state(screen_type_bytes: bytes) -> bool:
        return screen_type_bytes[0] == 0x03 #Todo add check for cutscene state

    @staticmethod #Todo add progressive equip updates
    def update_equipment_value(writes, memory_key:str, equipment_list, current_value_bytes:bytes, target_names:list[str]):

        if len(target_names) == 0:
            return 

        current_value = int.from_bytes(current_value_bytes, "little")
        new_index = -1
        current_index = -1
        target_value = None
    
        for i, (name, value) in enumerate(equipment_list):            
            if name in target_names:
                new_index = i
                target_value = value
            if value == current_value:
                current_index = i

        if new_index != -1 and current_index != -1 and current_index < new_index:
            writes.append(memory_locations.make_write(memory_key, target_value))
            #Todo set attack/def
    
    def add_items_to_inventory(self, writes, bag_slot_bytes: bytes, bag_weight_bytes: bytes):
        new_bag_slot_bytes = bytearray(bag_slot_bytes)
        bag_weight = int.from_bytes(bag_weight_bytes, "little")
        for item_to_add in state.bag_items_to_add:
            thing = itemDataDict[item_to_add]
            if bag_weight + thing.weight <= max_bag_weight:
                for index in range(max_bag_slots):
                    if new_bag_slot_bytes[index] == 0:
                        new_bag_slot_bytes[index] = thing.objectId
                        bag_weight = bag_weight + thing.weight
                        break
                else:
                    self.sell_item(thing)
            else:
                self.sell_item(thing)
                
        writes.append(memory_locations.make_write_bytes(MemoryKeys.BAG_SLOTS, new_bag_slot_bytes))
        writes.append(memory_locations.make_write(MemoryKeys.BAG_WEIGHT, bag_weight))

    @staticmethod
    def sell_item(item:ItemData):
        global state
        state.yen_to_add = state.yen_to_add + int(item.price/2)
        #Todo "sell" the item full price if option is set

    def get_sp_upgrade(self, magatama_and_tome_count: int, max_sp_bytes: bytes, writes: list[Any]) -> int:
        current_tome_count = (magatama_and_tome_count >> 2) & 3
        tome_sp_up_count = int((current_tome_count + state.tome_to_add) / 4 - current_tome_count / 4)
        new_value = (current_tome_count + state.tome_to_add) & 3
        magatama_and_tome_count = magatama_and_tome_count & 0xf3 | (new_value << 2)

        if tome_sp_up_count > 0:
            self.increment_memory_value(writes, MemoryKeys.MAX_SP, max_sp_bytes, 40 * tome_sp_up_count, 200)
        return magatama_and_tome_count

    def get_hp_upgrade(self, magatama_and_tome_count: int, screen_type_bytes: bytes, writes: list[Any],
                             yoh_object_pointer_iwram: int, max_hp_excl_buffs_bytes:bytes, max_hp_bytes:bytes) -> int:
        
        # Extract and increment the lower 2 bits
        current_magatama_count = magatama_and_tome_count & 3
        magatama_hp_up_count = int((current_magatama_count + state.magatama_to_add) / 4 - current_magatama_count / 4)
        new_magatama_count = (current_magatama_count + state.magatama_to_add) & 3
        magatama_and_tome_count = magatama_and_tome_count & 0xfc | new_magatama_count

        # If enough are collected for a hp upgrade
        if magatama_hp_up_count > 0:
            hp_increment = 24 * magatama_hp_up_count
            hp_cap = 240
            
            # Increment various hp values and refill current hp
            self.increment_memory_value(writes, MemoryKeys.MAX_HP_EXCL_BUFFS, max_hp_excl_buffs_bytes, hp_increment, hp_cap)
            max_hp = self.increment_memory_value(writes, MemoryKeys.MAX_HP, max_hp_bytes, hp_increment, hp_cap)
            writes.append(memory_locations.make_write(MemoryKeys.HP, max_hp))

            # Update in-level health while inside a level
            if self.is_in_gameplay_state(screen_type_bytes):
                writes.append((yoh_object_pointer_iwram + 0x6a, max_hp.to_bytes(2, "little"), MemoryDomainKeys.IWRAM))
        return magatama_and_tome_count

    def increment_memory_value(self, writes: list[Any], memory_key:str, current_bytes: bytes, add: int, cap: int) -> int:
        new_value = int.from_bytes(current_bytes, "little")
        new_value = self.add_clamped(new_value, add, cap)
        writes.append(memory_locations.make_write(memory_key, new_value))
        return new_value

    @staticmethod
    def add_clamped(count: int, add:int, cap:int) -> int:
        count = count + add
        if count > cap:
            count = cap
        return count
    
    def set_flags(self, writes: list[Any], memory_key:str, flag_data_dict: dict[str, FlagData], current_bytes: bytes, names: list[str]) -> None:
        new_bytes = bytearray(current_bytes)
        
        for name in names:
            flag_data = flag_data_dict[name]
            current_byte = current_bytes[flag_data.address_offset]
            new_byte = self.set_bit(current_byte, flag_data.bit)
            new_bytes[flag_data.address_offset] = new_byte
            
        writes.append(memory_locations.make_write_bytes(memory_key, new_bytes))

    @staticmethod
    def set_bit(value:int, bit:int) ->int:
        return value | (1<<bit)

    @staticmethod
    def is_bit_set(value: int, bit_position: int) -> bool:
        return bool(value & (1 << bit_position))    
        