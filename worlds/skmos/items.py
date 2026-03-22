from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import Item, ItemClassification
from .game_data import spiritData, itemData, SpiritData, ItemData

if TYPE_CHECKING:
    from .skmosworld import ShamanKingMasterOfSpiritsWorld

item_table = spiritData + itemData
filler_item_table = []

ITEM_NAME_TO_ID:dict[str, int] = {item.name: i+1 for i, item in enumerate(item_table)}
ITEM_ID_TO_ITEM:dict[int,SpiritData|ItemData] = {i+1: item for i, item in enumerate(item_table)}
DEFAULT_ITEM_CLASSIFICATIONS = {item.name: item.classification for item in item_table}

class SkmosItem(Item):
    game = "Shaman King: Master of Spirits"

def get_random_filler_item_name(world: ShamanKingMasterOfSpiritsWorld) -> str:
    # Handle traps
    if world.random.randint(0, 99) < world.options.trap_chance:
        #Todo only selected traps
        return world.random.choice([item.name for item in item_table
                                    if item.classification == ItemClassification.trap])
    
    # To balance the distribution similar to the original game we make 
    # a list and populate that according tot the vanilla item distribution
    # Then pick an item and remove it from the list and keep doing this for filler
    # till the list is empty and we repeat again
    global filler_item_table
    if len(filler_item_table) == 0:
        filler_item_table = [item.name for item in item_table 
                             if item.classification == ItemClassification.filler 
                             for _ in range(item.vanillaCount)]
        world.random.shuffle(filler_item_table)
    
    return filler_item_table.pop()

def create_item_with_correct_classification(world: ShamanKingMasterOfSpiritsWorld, name: str) -> SkmosItem:
    return SkmosItem(name, DEFAULT_ITEM_CLASSIFICATIONS[name], ITEM_NAME_TO_ID[name], world.player)

def create_all_items(world: ShamanKingMasterOfSpiritsWorld) -> None:
    item_pool = get_items(world)
    number_of_items = len(item_pool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    item_pool += [world.create_filler() for _ in range(needed_number_of_filler_items)]
    world.multiworld.itempool += item_pool

def get_items(world: ShamanKingMasterOfSpiritsWorld) -> list[Item]:
    #Get all items, except for filler and trap, as these will be added later
    return [world.create_item(item.name) for item in item_table 
            if item.classification not in [ItemClassification.filler, ItemClassification.trap]]

