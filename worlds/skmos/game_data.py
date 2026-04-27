from BaseClasses import ItemClassification
from typing import Dict
from .names import Names, AreaLevels, MemoryDomainKeys, MemoryKeys, ItemTypes

areaId = {
    Names.Eastern_Cemetery: 0x00,
    Names.Northern_Fields: 0x01,
    Names.Western_Cemetery: 0x02,
    Names.Southern_Mountains: 0x03,
    Names.Jungle_Ruins: 0x04,
    Names.Tao_Grounds: 0x05,
    Names.Industrial_Area: 0x06,
    Names.Ice_Lands: 0x07,
    Names.Map: 0xF,
}

areaShorthandToFullName = {
    "EC": Names.Eastern_Cemetery,
    "NF": Names.Northern_Fields,
    "WC": Names.Western_Cemetery,
    "SM": Names.Southern_Mountains,
    "JR": Names.Jungle_Ruins,
    "TG": Names.Tao_Grounds,
    "IA": Names.Industrial_Area,
    "IL": Names.Ice_Lands,
}

areaFullNameToShorthand = {
    Names.Eastern_Cemetery: "EC",
    Names.Northern_Fields: "NF",
    Names.Western_Cemetery: "WC",
    Names.Southern_Mountains: "SM",
    Names.Jungle_Ruins: "JR",
    Names.Tao_Grounds: "TG",
    Names.Industrial_Area: "IA",
    Names.Ice_Lands: "IL",
}

areaLevelCount = {
    "EC": 6,
    "NF": 7,
    "WC": 9,
    "SM": 7,
    "JR": 7,
    "TG": 10,
    "IA": 5,
    "IL": 3,
}

lvl = AreaLevels()

class LevelData:
    def __init__(self, level, screen_count):
        self.level = level
        self.screenCount = screen_count

levels = [
    #Eastern Cemetary
    LevelData(lvl.EC1, 2),
    LevelData(lvl.EC2, 0),
    LevelData(lvl.EC3, 0),
    LevelData(lvl.EC4, 0),
    LevelData(lvl.EC5, 0),
    LevelData(lvl.EC6, 0),
    #Northern Fields
    LevelData(lvl.NF1, 0),
    LevelData(lvl.NF2, 0),
    LevelData(lvl.NF3, 0),
    LevelData(lvl.NF4, 0),
    LevelData(lvl.NF5, 0),
    LevelData(lvl.NF6, 0),
    LevelData(lvl.NF7, 0),
    #Western Cemetery
    LevelData(lvl.WC1, 0),
    LevelData(lvl.WC2, 0),
    LevelData(lvl.WC3, 0),
    LevelData(lvl.WC4, 0),
    LevelData(lvl.WC5, 0),
    LevelData(lvl.WC6, 0),
    LevelData(lvl.WC7, 0),
    LevelData(lvl.WC8, 0),
    LevelData(lvl.WC9, 0),
    #Southern Mountains
    LevelData(lvl.SM1, 0),
    LevelData(lvl.SM2, 0),
    LevelData(lvl.SM3, 0),
    LevelData(lvl.SM4, 0),
    LevelData(lvl.SM5, 0),
    LevelData(lvl.SM6, 0),
    LevelData(lvl.SM7, 0),
    #Jungle Ruins
    LevelData(lvl.JR1, 0),
    LevelData(lvl.JR2, 0),
    LevelData(lvl.JR3, 0),
    LevelData(lvl.JR4, 0),
    LevelData(lvl.JR5, 0),
    LevelData(lvl.JR6, 0),
    LevelData(lvl.JR7, 0),
    #Tao Grounds
    LevelData(lvl.TG1, 0),
    LevelData(lvl.TG2, 0),
    LevelData(lvl.TG3, 0),
    LevelData(lvl.TG4, 0),
    LevelData(lvl.TG5, 0),
    LevelData(lvl.TG6, 0),
    LevelData(lvl.TG7, 0),
    LevelData(lvl.TG8, 0),
    LevelData(lvl.TG9, 0),
    LevelData(lvl.TG10, 0),
    #Industrial Area
    LevelData(lvl.IA1, 0),
    LevelData(lvl.IA2, 0),
    LevelData(lvl.IA3, 0),
    LevelData(lvl.IA4, 0),
    LevelData(lvl.IA5, 0),
    #Ice Lands
    LevelData(lvl.IL1, 0),
    LevelData(lvl.IL2, 0),
    LevelData(lvl.IL3, 0),
    #Inn
    LevelData(lvl.Inn, 1),
]

class BossData:
    def __init__(self, name, level, original_reward):
        self.name = name
        self.level = level
        self.originalReward = original_reward

bossData = [
    BossData(Names.Ryo_Boss,          lvl.EC4, [Names.Tome_Page, Names.Tokageroh]),
    BossData(Names.Trey_Boss,         lvl.NF4, [Names.Tome_Page, Names.Corey]),
    BossData(Names.Eliza_Boss,        lvl.WC6, [Names.Tome_Page, Names.Eliza]),
    BossData(Names.Silva_Boss,        lvl.SM5, [Names.Tome_Page]),#spirits active across the map
    BossData(Names.Joco_Boss,         lvl.JR6, [Names.Tome_Page, Names.Mic]),
    BossData(Names.Lee_Pai_Long_Boss, lvl.TG3, [Names.Tome_Page, Names.Lee_Pai_Long]),
    BossData(Names.Len_Tao_Boss,      lvl.TG6, [Names.Tome_Page, Names.Bason]),
    BossData(Names.En_Tao_Boss,       lvl.TG8, [Names.Tome_Page, Names.Grand_Tao_Dragon]),
    BossData(Names.Lyzerg_Boss,       lvl.IA3, [Names.Tome_Page, Names.Chloe]),
    BossData(Names.Michael_Boss,      lvl.IA5, [Names.Tome_Page, Names.Michael]),
    BossData(Names.Magister_Boss,     lvl.IL3, [Names.Tome_Page]),
    BossData(Names.Mephias_Boss,      lvl.IL3, []),
]

class EventData:
    def __init__(self, name, level, requirement_type, requirement, original_reward):
        self.name = name
        self.level = level
        self.requirementType = requirement_type
        self.requirement = requirement
        self.originalReward = original_reward
        
eventData = [
    EventData(Names.Intro,                   lvl.Inn, None,      None,    Names.Amidamaru),
    EventData(Names.Light_Sword_Event,       lvl.Inn, "Boss",    Names.Eliza_Boss,   Names.Light_Sword),
    EventData(Names.Shikigami_Event,         lvl.NF6, None,      None,    [Names.Shikigami, Names.Tome_Page]),
    EventData(Names.Ponchi_and_Konchi_Event, lvl.WC8, None,      None,    [Names.Ponchi, Names.Konchi]),
    EventData(Names.Mosuke_Event,            lvl.WC9, None,      None,     Names.Mosuke),
    EventData(Names.Antiquity_Event,         lvl.SM7, "Boss",    Names.Lyzerg_Boss,  Names.Antiquity),
    EventData(Names.Thunder_Sword_Event,     lvl.Inn, "Boss",    [Names.Len_Tao_Boss, Names.En_Tao_Boss], Names.Thunder_Sword),
    EventData(Names.Mash_Event,              lvl.Inn, "Boss",    Names.Michael_Boss, Names.Mash),
    EventData(Names.Zenki_and_Kohki_Event,   lvl.IL2, None,      None,    [Names.Zenki, Names.Konchi]),
    EventData(Names.Spirit_of_Fire_or_Game_complete_Event, lvl.IL3, "Credits", Names.Mephias_Boss, Names.Spirit_of_Fire),
]

class SpiritData:
    def __init__(self, number, name, sp_requirement, classification, original_location = None, event = None, boss = None):
        self.number = number
        self.name = name
        self.spRequirement = sp_requirement
        self.classification = classification
        self.originalLocation = original_location
        self.event = event
        self.boss = boss
        
spiritData = [
    SpiritData(1,  Names.Amidamaru,        25,      ItemClassification.useful,          event = Names.Intro),
    SpiritData(2,  Names.Mosuke,           None,    ItemClassification.useful,          event = Names.Mosuke_Event),
    SpiritData(3,  Names.Tokageroh,        None,    ItemClassification.progression,     boss = Names.Ryo_Boss),
    SpiritData(4,  Names.Corey,            20,      ItemClassification.progression,     boss = Names.Trey_Boss),
    SpiritData(5,  Names.Eliza,            None,    ItemClassification.progression,     boss = Names.Eliza_Boss),
    SpiritData(6,  Names.Silver_Shield,    None,    ItemClassification.progression,     lvl.WC8),
    SpiritData(7,  Names.Silver_Tail,      None,    ItemClassification.progression,     lvl.SM7),
    SpiritData(8,  Names.Silver_Wing,      None,    ItemClassification.progression,     lvl.WC1),
    SpiritData(9,  Names.Silver_Horn,      None,    ItemClassification.progression,     lvl.NF2),
    SpiritData(10, Names.Silver_Rod,       None,    ItemClassification.progression,     lvl.EC4),
    SpiritData(11, Names.Mic,              6,       ItemClassification.progression,     boss = Names.Joco_Boss),
    SpiritData(12, Names.Lee_Pai_Long,     4,       ItemClassification.progression,     boss = Names.Lee_Pai_Long_Boss),
    SpiritData(13, Names.Bason,            60,      ItemClassification.progression,     boss = Names.Len_Tao_Boss),
    SpiritData(14, Names.Grand_Tao_Dragon, 12,      ItemClassification.useful,          boss = Names.En_Tao_Boss),
    SpiritData(15, Names.Chloe,            1,       ItemClassification.progression,     boss = Names.Lyzerg_Boss),
    SpiritData(16, Names.Michael,          50,      ItemClassification.useful,          boss = Names.Michael_Boss),
    SpiritData(17, Names.Kanta,            6,       ItemClassification.useful,          lvl.EC3),
    SpiritData(18, Names.Gussy_Kenji,      15,      ItemClassification.useful,          lvl.EC2),
    SpiritData(19, Names.Tamegoroh,        None,    ItemClassification.useful,          lvl.NF7),
    SpiritData(20, Names.Shikigami,        6,       ItemClassification.useful,          event = Names.Shikigami_Event),
    SpiritData(21, Names.Frankensteiny,    None,    ItemClassification.useful,          lvl.WC3),
    SpiritData(22, Names.Ponchi,           7,       ItemClassification.useful,          event = Names.Ponchi_and_Konchi_Event),
    SpiritData(23, Names.Konchi,           30,      ItemClassification.useful,          event = Names.Ponchi_and_Konchi_Event),
    SpiritData(24, Names.Chimi_Moryo,      4,       ItemClassification.useful,          lvl.EC3),
    SpiritData(25, Names.Shaolin,          42,      ItemClassification.useful,          lvl.TG4),
    SpiritData(26, Names.Black_Raven,      None,    ItemClassification.progression,     lvl.TG7),
    SpiritData(27, Names.Tao_the_Great,    50,      ItemClassification.useful,          lvl.TG9),
    SpiritData(28, Names.Ian,              None,    ItemClassification.useful,          lvl.NF4),
    SpiritData(29, Names.Nizba,            None,    ItemClassification.useful,          lvl.NF1),
    SpiritData(30, Names.Dreisa,           None,    ItemClassification.useful,          lvl.WC1),
    SpiritData(31, Names.Yopia,            None,    ItemClassification.useful,          lvl.WC4),
    SpiritData(32, Names.Badbh,            None,    ItemClassification.useful,          lvl.NF3),
    SpiritData(33, Names.Vodianoi,         None,    ItemClassification.useful,          lvl.NF3),
    SpiritData(34, Names.Deht_the_Viking,  None,    ItemClassification.useful,          lvl.NF3),
    SpiritData(35, Names.Gororo,           20,      ItemClassification.progression,     lvl.TG3),
    SpiritData(36, Names.Zenki,            2,       ItemClassification.useful,          event = Names.Zenki_and_Kohki_Event),
    SpiritData(37, Names.Kohki,            2,       ItemClassification.useful,          event = Names.Zenki_and_Kohki_Event),
    SpiritData(38, Names.Golem,            30,      ItemClassification.useful,          lvl.IL2),
    SpiritData(39, Names.Orona,            40,      ItemClassification.useful,          lvl.JR5),
    SpiritData(40, Names.Pascal_Avaf,      2,       ItemClassification.progression,     lvl.IL1),
    SpiritData(41, Names.Yamagami,         2,       ItemClassification.useful,          lvl.SM3),
    SpiritData(42, Names.Gundari,          None,    ItemClassification.useful,          lvl.TG8),
    SpiritData(43, Names.Raphael,          None,    ItemClassification.useful,          lvl.TG3),
    SpiritData(44, Names.Gabriel,          None,    ItemClassification.useful,          lvl.SM3),
    SpiritData(45, Names.Uriel,            None,    ItemClassification.useful,          lvl.IA2),
    SpiritData(46, Names.Metatoron,        None,    ItemClassification.useful,          lvl.IA2),
    SpiritData(47, Names.Sariel,           None,    ItemClassification.useful,          lvl.IA4),
    SpiritData(48, Names.Remiel,           None,    ItemClassification.useful,          lvl.IA4),
    SpiritData(49, Names.Mash,             120,     ItemClassification.useful,          event = Names.Mash_Event),
    SpiritData(50, Names.Blaumro,          12,      ItemClassification.useful,          lvl.TG4),
    SpiritData(51, Names.Footballer,       14,      ItemClassification.progression,     lvl.IA1),
    SpiritData(52, Names.Shion_Shion,      4,       ItemClassification.progression,     lvl.IA1),
    SpiritData(53, Names.Blocks,           50,      ItemClassification.progression,     lvl.IA1),
    SpiritData(54, Names.Jen,              None,    ItemClassification.useful,          lvl.SM4),
    SpiritData(55, Names.Ashcroft,         20,      ItemClassification.useful,          lvl.SM3),
    SpiritData(56, Names.Jack,             4,       ItemClassification.useful,          lvl.JR4),
    SpiritData(57, Names.Chuck,            20,      ItemClassification.useful,          [lvl.JR1, lvl.JR4]),
    SpiritData(58, Names.Carlos_and_Joao,  30,      ItemClassification.useful,          lvl.SM7),
    SpiritData(59, Names.Antonio,          2,       ItemClassification.useful,          lvl.JR5),
    SpiritData(60, Names.Jose,             2,       ItemClassification.useful,          lvl.SM3),
    SpiritData(61, Names.Pancho,           2,       ItemClassification.useful,          lvl.TG3),
    SpiritData(62, Names.Zapata,           2,       ItemClassification.useful,          lvl.TG1),
    SpiritData(63, Names.Miguel,           2,       ItemClassification.useful,          lvl.IA4),
    SpiritData(64, Names.Magnescope,       1,       ItemClassification.useful,          lvl.EC4),
    SpiritData(65, Names.Mama,             4,       ItemClassification.progression,     lvl.IL1),
    SpiritData(66, Names.Cifer,            60,      ItemClassification.useful,          lvl.IL1),
    SpiritData(67, Names.Spirit_of_Fire, None, ItemClassification.useful, event = Names.Spirit_of_Fire_or_Game_complete_Event),
    SpiritData(68, Names.Matamune,         160,     ItemClassification.useful,          lvl.IL2),
]

class SpiritCombo:
    def __init__(self, number, name, sp_requirement, classification, requirements):
        self.number = number
        self.name = name
        self.spRequirement = sp_requirement
        self.classification = classification
        self.requirements = requirements

spiritCombo = {
    SpiritCombo(1, Names.Revival, None, ItemClassification.useful, [Names.Ian, Names.Nizba, Names.Dreisa, Names.Yopia]),
    SpiritCombo(2, Names.Totem_Attack, 120, ItemClassification.progression, [ Names.Silver_Shield, 
                                                                                                               Names.Silver_Tail, 
                                                                                                               Names.Silver_Wing, 
                                                                                                               Names.Silver_Horn, 
                                                                                                               Names.Silver_Rod, 
                                                                                                               Names.Headphones,
                                                                                                               Names.Left_Glove,
                                                                                                               Names.Right_Glove,
                                                                                                               Names.Left_Sandal,
                                                                                                               Names.Right_Sandal]),
    SpiritCombo(3, Names.Grand_Halo_Blade, 52, ItemClassification.useful, [Names.Amidamaru, Names.Mosuke]),
    SpiritCombo(4, Names.Cavalry_Charge, 55, ItemClassification.progression, [Names.Bason, Names.Black_Raven]),
    SpiritCombo(5, Names.Grande_Phantasma, 90, ItemClassification.useful, [Names.Antonio, Names.Jose, Names.Pancho, Names.Zapata, Names.Miguel]),
    SpiritCombo(6, Names.Ray_of_Light, 150, ItemClassification.useful, [Names.Michael,
                                                                                                        Names.Gabriel,
                                                                                                        Names.Raphael,
                                                                                                        Names.Uriel,
                                                                                                        Names.Sariel,
                                                                                                        Names.Remiel,
                                                                                                        Names.Metatoron]),#Technically Michael + 4 others of these
    SpiritCombo(7, Names.Jaguar_Man, 10, ItemClassification.progression, [Names.Mic, Names.Pascal_Avaf]),
    SpiritCombo(8, Names.Celestial_Slash, 30, ItemClassification.useful, [Names.Amidamaru, Names.Light_Sword]),
    SpiritCombo(9, Names.Into_the_Antiquity, 110, ItemClassification.useful, [Names.Amidamaru, Names.Antiquity]),
    SpiritCombo(10,Names.Golden_Thunder_Impalement, 40, ItemClassification.useful, [Names.Bason, Names.Thunder_Sword]),
}

class ItemData:
    def __init__(self, name:str, item_type:str, classification:ItemClassification, 
                 original_location:str = None, event:str = None, boss:str = None, price:int = None, weight:int = None, object_id:int = None, proxy_item:str = None, proxy_item_count:int = None, vanilla_count:int = 1):
        self.name = name
        self.itemType = item_type
        self.classification = classification
        self.originalLocation = original_location
        self.event = event
        self.boss = boss
        self.price = price
        self.weight = weight
        self.objectId = object_id
        self.proxyItem = proxy_item
        self.proxyItemCount = proxy_item_count
        self.vanillaCount = vanilla_count
        
itemData = [
    ItemData(Names.Wood_Sword,  ItemTypes.Attack_Upgrade, ItemClassification.useful), #Start game with
    ItemData(Names.Light_Sword, ItemTypes.Attack_Upgrade, ItemClassification.useful, event = Names.Light_Sword_Event),
    ItemData(Names.Antiquity,   ItemTypes.Attack_Upgrade, ItemClassification.useful, event = Names.Antiquity_Event),
    
    ItemData(Names.Thunder_Sword, ItemTypes.Upgrade, ItemClassification.useful, event = Names.Thunder_Sword_Event),
    
    ItemData(Names.Lucky_Charm,    ItemTypes.Defence_Upgrade, ItemClassification.useful, lvl.NF3),
    ItemData(Names.Bear_Claw,      ItemTypes.Defence_Upgrade, ItemClassification.useful, lvl.TG10),
    ItemData(Names.Battle_Clothes, ItemTypes.Defence_Upgrade, ItemClassification.useful, lvl.IA2),
    
    ItemData(Names.Headphones,   ItemTypes.Spirit_Slot_Upgrade, ItemClassification.progression, lvl.EC4),# Progression if Totem attack needs all spirits
    ItemData(Names.Right_Glove,  ItemTypes.Spirit_Slot_Upgrade, ItemClassification.progression),#Starts the game with
    ItemData(Names.Left_Glove,   ItemTypes.Spirit_Slot_Upgrade, ItemClassification.progression, lvl.NF2),
    ItemData(Names.Left_Sandal,  ItemTypes.Spirit_Slot_Upgrade, ItemClassification.progression, lvl.SM3),
    ItemData(Names.Right_Sandal, ItemTypes.Spirit_Slot_Upgrade, ItemClassification.progression, lvl.WC4),

    ItemData(Names.Magatama_Bead, ItemTypes.Health_Upgrade, ItemClassification.useful, lvl.EC2, vanilla_count=20),
    ItemData(Names.Magatama_Bead, ItemTypes.Health_Upgrade, ItemClassification.useful, lvl.NF2, vanilla_count=20),
    ItemData(Names.Magatama_Bead, ItemTypes.Health_Upgrade, ItemClassification.useful, lvl.NF3, vanilla_count=20),
    ItemData(Names.Magatama_Bead, ItemTypes.Health_Upgrade, ItemClassification.useful, lvl.EC3, vanilla_count=20),
    ItemData(Names.Magatama_Bead, ItemTypes.Health_Upgrade, ItemClassification.useful, lvl.WC2, vanilla_count=20),
    ItemData(Names.Magatama_Bead, ItemTypes.Health_Upgrade, ItemClassification.useful, lvl.WC4, vanilla_count=20),
    ItemData(Names.Magatama_Bead, ItemTypes.Health_Upgrade, ItemClassification.useful, lvl.SM2, vanilla_count=20),
    ItemData(Names.Magatama_Bead, ItemTypes.Health_Upgrade, ItemClassification.useful, lvl.SM3, vanilla_count=20),
    ItemData(Names.Magatama_Bead, ItemTypes.Health_Upgrade, ItemClassification.useful, lvl.JR2, vanilla_count=20),
    ItemData(Names.Magatama_Bead, ItemTypes.Health_Upgrade, ItemClassification.useful, lvl.JR5, vanilla_count=20),
    ItemData(Names.Magatama_Bead, ItemTypes.Health_Upgrade, ItemClassification.useful, lvl.TG5, vanilla_count=20),
    ItemData(Names.Magatama_Bead, ItemTypes.Health_Upgrade, ItemClassification.useful, lvl.TG6, vanilla_count=20),
    ItemData(Names.Magatama_Bead, ItemTypes.Health_Upgrade, ItemClassification.useful, lvl.EC2, vanilla_count=20),
    ItemData(Names.Magatama_Bead, ItemTypes.Health_Upgrade, ItemClassification.useful, lvl.IA2, vanilla_count=20),
    ItemData(Names.Magatama_Bead, ItemTypes.Health_Upgrade, ItemClassification.useful, lvl.IA1, vanilla_count=20),
    ItemData(Names.Magatama_Bead, ItemTypes.Health_Upgrade, ItemClassification.useful, lvl.JR4, vanilla_count=20),
    ItemData(Names.Magatama_Bead, ItemTypes.Health_Upgrade, ItemClassification.useful, lvl.TG8, vanilla_count=20),
    ItemData(Names.Magatama_Bead, ItemTypes.Health_Upgrade, ItemClassification.useful, lvl.IA4, vanilla_count=20),
    ItemData(Names.Magatama_Bead, ItemTypes.Health_Upgrade, ItemClassification.useful, lvl.IL2, vanilla_count=20),
    ItemData(Names.Magatama_Bead, ItemTypes.Health_Upgrade, ItemClassification.useful, lvl.IL2, vanilla_count=20),

    ItemData(Names.Tome_Page, ItemTypes.Furyoku_Upgrade, ItemClassification.useful, boss = Names.Ryo_Boss, vanilla_count=12),
    ItemData(Names.Tome_Page, ItemTypes.Furyoku_Upgrade, ItemClassification.useful, boss = Names.Trey_Boss, vanilla_count=12),
    ItemData(Names.Tome_Page, ItemTypes.Furyoku_Upgrade, ItemClassification.useful, event = Names.Shikigami_Event, vanilla_count=12),
    ItemData(Names.Tome_Page, ItemTypes.Furyoku_Upgrade, ItemClassification.useful, boss = Names.Eliza_Boss, vanilla_count=12),
    ItemData(Names.Tome_Page, ItemTypes.Furyoku_Upgrade, ItemClassification.useful, boss = Names.Silva_Boss, vanilla_count=12),
    ItemData(Names.Tome_Page, ItemTypes.Furyoku_Upgrade, ItemClassification.useful, boss = Names.Joco_Boss, vanilla_count=12),
    ItemData(Names.Tome_Page, ItemTypes.Furyoku_Upgrade, ItemClassification.useful, boss = Names.Lee_Pai_Long_Boss, vanilla_count=12),
    ItemData(Names.Tome_Page, ItemTypes.Furyoku_Upgrade, ItemClassification.useful, boss = Names.Len_Tao_Boss, vanilla_count=12),
    ItemData(Names.Tome_Page, ItemTypes.Furyoku_Upgrade, ItemClassification.useful, boss = Names.En_Tao_Boss, vanilla_count=12),
    ItemData(Names.Tome_Page, ItemTypes.Furyoku_Upgrade, ItemClassification.useful, boss = Names.Lyzerg_Boss, vanilla_count=12),
    ItemData(Names.Tome_Page, ItemTypes.Furyoku_Upgrade, ItemClassification.useful, boss = Names.Michael_Boss, vanilla_count=12),
    ItemData(Names.Tome_Page, ItemTypes.Furyoku_Upgrade, ItemClassification.useful, boss = Names.Magister_Boss, vanilla_count=12),

    ItemData("Key 1",  ItemTypes.Key, ItemClassification.progression, lvl.WC1),
    ItemData("Key 2",  ItemTypes.Key, ItemClassification.progression, lvl.WC5),
    ItemData("Key 3",  ItemTypes.Key, ItemClassification.progression, lvl.SM1),
    ItemData("Key 4",  ItemTypes.Key, ItemClassification.progression, lvl.SM2),
    ItemData("Key 5",  ItemTypes.Key, ItemClassification.progression, lvl.SM3),
    ItemData("Key 6",  ItemTypes.Key, ItemClassification.progression, lvl.SM4),
    ItemData("Key 7",  ItemTypes.Key, ItemClassification.progression, lvl.JR2),
    ItemData("Key 8",  ItemTypes.Key, ItemClassification.progression, lvl.TG1),
    ItemData("Key 9",  ItemTypes.Key, ItemClassification.progression, lvl.TG2),
    ItemData("Key 10", ItemTypes.Key, ItemClassification.progression, lvl.IA2),
    ItemData("Key 11", ItemTypes.Key, ItemClassification.progression, lvl.IA4),
    ItemData("Key 12", ItemTypes.Key, ItemClassification.progression, lvl.IL1),
    ItemData("Key 13", ItemTypes.Key, ItemClassification.progression, lvl.IL2),
    #Todo: Stage with multiple keys
    
    ItemData(Names.Leaf,              ItemTypes.Consumable, ItemClassification.filler, vanilla_count=1), #Technically 3 leaves and none of the others, but its nicer to be able to get all
    ItemData(Names.Rock,              ItemTypes.Consumable, ItemClassification.filler, vanilla_count=1),
    ItemData(Names.Skeleton,          ItemTypes.Consumable, ItemClassification.filler, vanilla_count=1),
    ItemData(Names.Sushi,             ItemTypes.Bag, ItemClassification.filler, price=150,     weight=1,    object_id=4, vanilla_count=15),
    ItemData(Names.Hotdog,            ItemTypes.Bag, ItemClassification.filler, price=400,     weight=1,    object_id=5, vanilla_count=11),
    ItemData(Names.Burger,            ItemTypes.Bag, ItemClassification.filler, price=1000,    weight=2,    object_id=6, vanilla_count=9),
    ItemData(Names.Noodles,           ItemTypes.Bag, ItemClassification.filler, price=3000,    weight=3,    object_id=7, vanilla_count=3),
    ItemData(Names.Antidote,          ItemTypes.Bag, ItemClassification.filler, price=300,     weight=1,    object_id=8, vanilla_count=3),
    ItemData(f"2x {Names.Sushi}", ItemTypes.Bag, ItemClassification.filler, proxy_item=Names.Sushi, proxy_item_count=2, vanilla_count=12),
    ItemData(f"3x {Names.Sushi}", ItemTypes.Bag, ItemClassification.filler, proxy_item=Names.Sushi, proxy_item_count=3, vanilla_count=2),
    ItemData(f"4x {Names.Sushi}", ItemTypes.Bag, ItemClassification.filler, proxy_item=Names.Sushi, proxy_item_count=4, vanilla_count=1),
    ItemData(f"2x {Names.Hotdog}", ItemTypes.Bag, ItemClassification.filler, proxy_item=Names.Hotdog, proxy_item_count=2, vanilla_count=1),
    ItemData(f"2x {Names.Burger}", ItemTypes.Bag, ItemClassification.filler, proxy_item=Names.Burger, proxy_item_count=2, vanilla_count=7),
    ItemData(f"2x {Names.Noodles}", ItemTypes.Bag, ItemClassification.filler, proxy_item=Names.Noodles, proxy_item_count=2, vanilla_count=4),
    ItemData(f"4x {Names.Noodles}", ItemTypes.Bag, ItemClassification.filler, proxy_item=Names.Noodles, proxy_item_count=4, vanilla_count=2),
    # Small bronze coin = 10 yen, small silver coin = 100, large silver coin = 500
    # Converted to yen in item names for convenience, these are all variations that vanilla chests can give
    ItemData(f"20 {Names.Yen}", ItemTypes.Money, ItemClassification.filler, price=20, vanilla_count=3),
    ItemData(f"30 {Names.Yen}", ItemTypes.Money, ItemClassification.filler, price=30, vanilla_count=17),
    ItemData(f"40 {Names.Yen}", ItemTypes.Money, ItemClassification.filler, price=40, vanilla_count=19),
    ItemData(f"50 {Names.Yen}", ItemTypes.Money, ItemClassification.filler, price=50, vanilla_count=11),
    ItemData(f"60 {Names.Yen}", ItemTypes.Money, ItemClassification.filler, price=60, vanilla_count=11),
    ItemData(f"70 {Names.Yen}", ItemTypes.Money, ItemClassification.filler, price=70, vanilla_count=5),
    ItemData(f"80 {Names.Yen}", ItemTypes.Money, ItemClassification.filler, price=80, vanilla_count=12),
    ItemData(f"100 {Names.Yen}", ItemTypes.Money, ItemClassification.filler, price=100, vanilla_count=4),
    ItemData(f"200 {Names.Yen}", ItemTypes.Money, ItemClassification.filler, price=200, vanilla_count=13),
    ItemData(f"300 {Names.Yen}", ItemTypes.Money, ItemClassification.filler, price=300, vanilla_count=15),
    ItemData(f"400 {Names.Yen}", ItemTypes.Money, ItemClassification.filler, price=400, vanilla_count=9),
    ItemData(f"500 {Names.Yen}", ItemTypes.Money, ItemClassification.filler, price=500, vanilla_count=8),
    ItemData(f"600 {Names.Yen}", ItemTypes.Money, ItemClassification.filler, price=600, vanilla_count=1),
    ItemData(f"1000 {Names.Yen}", ItemTypes.Money, ItemClassification.filler, price=1000, vanilla_count=11),
    ItemData(f"1500 {Names.Yen}", ItemTypes.Money, ItemClassification.filler, price=1500, vanilla_count=4),
    ItemData(f"2000 {Names.Yen}", ItemTypes.Money, ItemClassification.filler, price=2000, vanilla_count=2),

    ItemData(Names.Poison_Trap,     ItemTypes.Trap, ItemClassification.trap),
    ItemData(Names.Freeze_Trap,     ItemTypes.Trap, ItemClassification.trap),
    ItemData(Names.Fire_Trap,       ItemTypes.Trap, ItemClassification.trap),
    ItemData(Names.Slow_Trap,       ItemTypes.Trap, ItemClassification.trap),
    ItemData(Names.Stop_Trap,       ItemTypes.Trap, ItemClassification.trap),
    #ItemData("Unknown Trap", ItemTypes.Trap, ItemClassification.trap),
    ItemData(Names.Power_Down_Trap, ItemTypes.Trap, ItemClassification.trap),
    ItemData(Names.Pacifist_Trap,   ItemTypes.Trap, ItemClassification.trap),
    ItemData(Names.Confusion_Trap,  ItemTypes.Trap, ItemClassification.trap),
]

itemDataDict = {item.name: item for item in itemData}

class FlagType:
    Event_Completed = "Event Completed"
    Boss_Started = "Boss Started"
    Boss_Completed = "Boss Completed"

class FlagData:
    def __init__(self, name, address, address_offset, bit, flag_type = "Collected"):
        self.name = name
        self.address = address
        self.address_offset = address_offset
        self.bit = bit
        self.flagType = flag_type
        
storyFlags = [
    FlagData(Names.Intro,                   0x1e30, 0, 1, FlagType.Event_Completed),
    FlagData(Names.Ryo_Boss,                0x1e30, 0, 2, FlagType.Boss_Started),
    FlagData(Names.Ryo_Boss,                0x1e30, 0, 3, FlagType.Boss_Completed),
    FlagData(Names.Shikigami_Event,         0x1e30, 0, 4, FlagType.Event_Completed),#Available/Completed?
    FlagData(Names.Trey_Boss,               0x1e30, 0, 5, FlagType.Boss_Started),
    FlagData(Names.Trey_Boss,               0x1e30, 0, 6, FlagType.Boss_Completed),
    FlagData(Names.Eliza_Boss,              0x1e30, 0, 7, FlagType.Boss_Started),

    FlagData(Names.Eliza_Boss,              0x1e31, 1, 0, FlagType.Boss_Completed),
    FlagData(Names.Light_Sword_Event,       0x1e31, 1, 1, FlagType.Event_Completed),
    FlagData(Names.Silva_Boss,              0x1e31, 1, 2, FlagType.Boss_Started),
    FlagData(Names.Silva_Boss,              0x1e31, 1, 3, FlagType.Boss_Completed),
    FlagData(Names.Joco_Boss,               0x1e31, 1, 4, FlagType.Boss_Started),
    FlagData(Names.Joco_Boss,               0x1e31, 1, 5, FlagType.Boss_Completed),
    FlagData(Names.Ponchi_and_Konchi_Event, 0x1e31, 1, 6, FlagType.Event_Completed),
    FlagData(Names.Lee_Pai_Long_Boss,       0x1e31, 1, 7, FlagType.Boss_Started),

    FlagData(Names.Lee_Pai_Long_Boss,       0x1e32, 2, 0, FlagType.Boss_Completed),
    FlagData(Names.Mosuke_Event,            0x1e32, 2, 1, FlagType.Event_Completed),
    FlagData(Names.Len_Tao_Boss,            0x1e32, 2, 2, FlagType.Boss_Started),
    FlagData(Names.Len_Tao_Boss,            0x1e32, 2, 3, FlagType.Boss_Completed),
    FlagData(Names.Zenki_and_Kohki_Event,   0x1e32, 2, 4, FlagType.Event_Completed),
    FlagData(Names.En_Tao_Boss,             0x1e32, 2, 5, FlagType.Boss_Started),
    FlagData(Names.En_Tao_Boss,             0x1e32, 2, 6, FlagType.Boss_Completed),
    FlagData(Names.Thunder_Sword_Event,     0x1e32, 2, 7, FlagType.Event_Completed),

    FlagData(Names.Lyzerg_Boss,             0x1e33, 3, 0, FlagType.Boss_Started),
    FlagData(Names.Lyzerg_Boss,             0x1e33, 3, 1, FlagType.Boss_Completed),
    FlagData(Names.Antiquity_Event,         0x1e33, 3, 2, FlagType.Event_Completed),
    FlagData(Names.Michael_Boss,            0x1e33, 3, 3, FlagType.Boss_Started),
    FlagData(Names.Michael_Boss,            0x1e33, 3, 4, FlagType.Boss_Completed),
    FlagData(Names.Mash_Event,              0x1e33, 3, 5, FlagType.Event_Completed),
    FlagData(Names.Magister_Boss,           0x1e33, 3, 6, FlagType.Boss_Started),
    FlagData(Names.Magister_Boss,           0x1e33, 3, 7, FlagType.Boss_Completed),

    FlagData(Names.Mephias_Boss,            0x1e34, 4, 0, FlagType.Boss_Completed),
    FlagData(Names.Spirit_of_Fire_or_Game_complete_Event, 0x1e34, 4, 1, FlagType.Event_Completed),
]

spiritCollectionFlags = [
    FlagData(Names.Amidamaru,       0x235b, 0, 1),
    FlagData(Names.Mosuke,          0x235b, 0, 3),
    FlagData(Names.Tokageroh,       0x235b, 0, 5),
    FlagData(Names.Corey,           0x235b, 0, 6),
    FlagData(Names.Eliza,           0x235b, 0, 7),

    FlagData(Names.Silver_Shield,   0x235c, 1, 0),
    FlagData(Names.Silver_Tail,     0x235c, 1, 1),
    FlagData(Names.Silver_Wing,     0x235c, 1, 2),
    FlagData(Names.Silver_Horn,     0x235c, 1, 3),
    FlagData(Names.Silver_Rod,      0x235c, 1, 4),
    FlagData(Names.Mic,             0x235c, 1, 6),
    FlagData(Names.Lee_Pai_Long,    0x235c, 1, 7),

    FlagData(Names.Bason,           0x235d, 2, 0),
    FlagData(Names.Grand_Tao_Dragon,0x235d, 2, 2),
    FlagData(Names.Chloe,           0x235d, 2, 3),
    FlagData(Names.Michael,         0x235d, 2, 4),
    FlagData(Names.Kanta,           0x235d, 2, 6),
    FlagData(Names.Gussy_Kenji,     0x235d, 2, 7),

    FlagData(Names.Tamegoroh,       0x235e, 3, 0),
    FlagData(Names.Shikigami,       0x235e, 3, 1),
    FlagData(Names.Frankensteiny,   0x235e, 3, 2),
    FlagData(Names.Ponchi,          0x235e, 3, 3),
    FlagData(Names.Konchi,          0x235e, 3, 4),
    FlagData(Names.Chimi_Moryo,     0x235e, 3, 5),
    FlagData(Names.Shaolin,         0x235e, 3, 6),
    FlagData(Names.Black_Raven,     0x235e, 3, 7),

    FlagData(Names.Tao_the_Great,   0x235f, 4, 0),
    FlagData(Names.Ian,             0x235f, 4, 1),
    FlagData(Names.Nizba,           0x235f, 4, 2),
    FlagData(Names.Dreisa,          0x235f, 4, 3),
    FlagData(Names.Yopia,           0x235f, 4, 4),
    FlagData(Names.Badbh,           0x235f, 4, 6),
    FlagData(Names.Vodianoi,        0x235f, 4, 7),

    FlagData(Names.Deht_the_Viking, 0x2360, 5, 0),
    FlagData(Names.Gororo,          0x2360, 5, 1),
    FlagData(Names.Zenki,           0x2360, 5, 2),
    FlagData(Names.Kohki,           0x2360, 5, 3),
    FlagData(Names.Golem,           0x2360, 5, 4),
    FlagData(Names.Orona,           0x2360, 5, 5),
    FlagData(Names.Pascal_Avaf,     0x2360, 5, 6),

    FlagData(Names.Yamagami,        0x2361, 6, 0),
    FlagData(Names.Gundari,         0x2361, 6, 1),
    FlagData(Names.Raphael,         0x2361, 6, 2),
    FlagData(Names.Gabriel,         0x2361, 6, 3),
    FlagData(Names.Uriel,           0x2361, 6, 4),
    FlagData(Names.Metatoron,       0x2361, 6, 5),
    FlagData(Names.Sariel,          0x2361, 6, 6),
    FlagData(Names.Remiel,          0x2361, 6, 7),

    FlagData(Names.Mash,            0x2362, 7, 0),
    FlagData(Names.Blaumro,         0x2362, 7, 1),
    FlagData(Names.Footballer,      0x2362, 7, 2),
    FlagData(Names.Shion_Shion,     0x2362, 7, 3),
    FlagData(Names.Blocks,          0x2362, 7, 4),
    FlagData(Names.Jen,             0x2362, 7, 5),
    FlagData(Names.Ashcroft,        0x2362, 7, 6),
    FlagData(Names.Jack,            0x2362, 7, 7),

    FlagData(Names.Chuck,           0x2363, 8, 0),
    FlagData(Names.Carlos_and_Joao, 0x2363, 8, 1),
    FlagData(Names.Antonio,         0x2363, 8, 2),
    FlagData(Names.Jose,            0x2363, 8, 3),
    FlagData(Names.Pancho,          0x2363, 8, 4),
    FlagData(Names.Zapata,          0x2363, 8, 5),
    FlagData(Names.Miguel,          0x2363, 8, 6),

    FlagData(Names.Magnescope,      0x2364, 9, 0),
    FlagData(Names.Mama,            0x2364, 9, 1),
    FlagData(Names.Cifer,           0x2364, 9, 2),
    FlagData(Names.Spirit_of_Fire,  0x2364, 9, 3),
    FlagData(Names.Matamune,        0x2364, 9, 4),
]

spiritCollectionFlagDict = {flagData.name: flagData for flagData in spiritCollectionFlags}

spiritSlotFlags = [
    FlagData(Names.Headphones,      0x2365, 0, 0),
    FlagData(Names.Right_Glove,     0x2365, 0, 1), #Start game with
    FlagData(Names.Left_Glove,      0x2365, 0, 2),
    FlagData(Names.Left_Sandal,     0x2365, 0, 3),
    FlagData(Names.Right_Sandal,    0x2365, 0, 4),
]

spiritSlotFlagDict = {flagData.name: flagData for flagData in spiritSlotFlags}

traps: Dict[str, hex] = {
    Names.Poison_Trap     : 0x0002,
    Names.Freeze_Trap     : 0x0004,#Broken?
    Names.Fire_Trap       : 0x0010,#No damage?
    Names.Slow_Trap       : 0x0040,
    Names.Stop_Trap       : 0x0080,
    "unknown"             : 0x00A0,#Something?
    Names.Power_Down_Trap : 0x0100,
    Names.Pacifist_Trap   : 0x0200,
    Names.Confusion_Trap  : 0x0400
}

class MemoryLocation:
    def __init__(self, name, address, byte_length, memory_domain):
        self.name = name
        self.address = address
        self.byte_length = byte_length
        self.memoryDomain = memory_domain

class MemoryLocations:
    def __init__(self):
        self.entries = [
            #Values
            MemoryLocation(MemoryKeys.CURRENT_SCREEN,             0x1DDD,     1,  MemoryDomainKeys.IWRAM),
            MemoryLocation(MemoryKeys.YOH_OBJECT,                 0x22b4,     4,  MemoryDomainKeys.IWRAM),
            MemoryLocation(MemoryKeys.EVENT_FLAGS,                0x1e30,     5,  MemoryDomainKeys.IWRAM),
            MemoryLocation(MemoryKeys.BAG_SLOTS,                  0x234b,     10, MemoryDomainKeys.IWRAM),
            MemoryLocation(MemoryKeys.BAG_WEIGHT,                 0x2355,     1,  MemoryDomainKeys.IWRAM),
            MemoryLocation(MemoryKeys.LEAF_COUNT,                 0x2358,     1,  MemoryDomainKeys.IWRAM),
            MemoryLocation(MemoryKeys.ROCK_COUNT,                 0x2359,     1,  MemoryDomainKeys.IWRAM),
            MemoryLocation(MemoryKeys.SKELETON_COUNT,             0x235a,     1,  MemoryDomainKeys.IWRAM),
            MemoryLocation(MemoryKeys.MONEY,                      0x2310,     4,  MemoryDomainKeys.IWRAM),
            MemoryLocation(MemoryKeys.HP,                         0x22b8,     2,  MemoryDomainKeys.IWRAM),
            MemoryLocation(MemoryKeys.MAX_HP,                     0x22ba,     2,  MemoryDomainKeys.IWRAM),
            MemoryLocation(MemoryKeys.MAX_HP_EXCL_BUFFS,          0x22bc,     2,  MemoryDomainKeys.IWRAM),
            MemoryLocation(MemoryKeys.MAX_SP,                     0x22c0,     2,  MemoryDomainKeys.IWRAM),
            MemoryLocation(MemoryKeys.MAGATAMA_AND_TOME_COUNT,    0x2366,     1,  MemoryDomainKeys.IWRAM),
            MemoryLocation(MemoryKeys.SPIRIT_COLLECTION,          0x235b,     11, MemoryDomainKeys.IWRAM),
            MemoryLocation(MemoryKeys.SPIRIT_SLOTS,               0x2365,     1,  MemoryDomainKeys.IWRAM),
            MemoryLocation(MemoryKeys.WEAPON_SLOT,                0x2356,     1,  MemoryDomainKeys.IWRAM),
            MemoryLocation(MemoryKeys.DEFENCE_SLOT,               0x2357,     1,  MemoryDomainKeys.IWRAM),

            #Flags
            MemoryLocation(MemoryKeys.ITEM_FLAGS,                 0x1ea8,     905, MemoryDomainKeys.IWRAM),
            MemoryLocation(MemoryKeys.KEY_FLAGS,                  0x1dde,     87, MemoryDomainKeys.IWRAM),
            MemoryLocation(MemoryKeys.SPIRIT_FLAGS,               0x232c,     10, MemoryDomainKeys.IWRAM), #Originally from 0x235b

            #Settings
            MemoryLocation(MemoryKeys.TOTEM_SPIRIT_LOCATION_MOD_1,          0x535e,     2, MemoryDomainKeys.ROM),
            MemoryLocation(MemoryKeys.TOTEM_SPIRIT_LOCATION_MOD_2,          0x536c,     2, MemoryDomainKeys.ROM),
            MemoryLocation(MemoryKeys.DISABLE_SPIRIT_SPLASH,                0x16422,    4, MemoryDomainKeys.ROM),

            #Mods
            MemoryLocation(MemoryKeys.DISABLE_VANILLA_HP_SP_PICKUP,         0x7c74,     2, MemoryDomainKeys.ROM),
            MemoryLocation(MemoryKeys.DISABLE_VANILLA_SPIRIT_SLOT_PICKUP,   0x7c7c,     2, MemoryDomainKeys.ROM),
            MemoryLocation(MemoryKeys.DISABLE_GROUNDED_PICKUP_MESSAGE,      0x6544,     2, MemoryDomainKeys.ROM),
            MemoryLocation(MemoryKeys.KEY_COLLECTION_BIT_MOD,               0x17000,    1, MemoryDomainKeys.ROM),
            MemoryLocation(MemoryKeys.TOME_SOFTLOCK_FIX, 0x3bde8, 2, MemoryDomainKeys.ROM),

            MemoryLocation(MemoryKeys.SPIRIT_FLAG_LOCATION_REGULAR_MOD,        0x8464,  1, MemoryDomainKeys.ROM),
            MemoryLocation(MemoryKeys.SPIRIT_FLAG_LOCATION_ENEMY_DROP_MOD,     0x6330,  1, MemoryDomainKeys.ROM),
            MemoryLocation(MemoryKeys.SPIRIT_FLAG_LOCATION_SPIRIT_TOTEM_MOD,   0x53a0,  1, MemoryDomainKeys.ROM),
            MemoryLocation(MemoryKeys.SPIRIT_FLAG_LOCATION_CUTSCENE_MOD,       0x8724,  1, MemoryDomainKeys.ROM),
            MemoryLocation(MemoryKeys.SPIRIT_FLAG_LOCATION_SAVE_LOAD_MOD,      0x1fc70, 1, MemoryDomainKeys.ROM),
            MemoryLocation(MemoryKeys.DISABLE_STARTING_SPIRIT_SLOT_UNLOCK,     0x8f16,  2, MemoryDomainKeys.ROM),
            MemoryLocation(MemoryKeys.DISABLE_SET_STARTING_SWORD,              0x8f22,  4, MemoryDomainKeys.ROM),
            MemoryLocation(MemoryKeys.DISABLE_SET_STARTING_SPIRIT,             0x8f1e,  2, MemoryDomainKeys.ROM),
            MemoryLocation(MemoryKeys.DISABLE_EQUIP_STARTING_SPIRIT,           0x8f30,  4, MemoryDomainKeys.ROM),
        ]

        # Create lookup dictionary for easy access
        self._lookup = {entry.name: entry for entry in self.entries}

    def get_entry(self, name:str):
        entry = self._lookup.get(name)
        return entry.address, entry.byte_length, entry.memoryDomain

    def make_write(self, name:str, value:int):
        entry = self._lookup.get(name)
        return entry.address, value.to_bytes(entry.byte_length, "little"), entry.memoryDomain
    
    def make_write_bytes(self, name:str, value:bytes):
        entry = self._lookup.get(name)
        return entry.address, value, entry.memoryDomain

weapon_progression_dict = [
    #("None?" , 0xFF),
    (Names.Wood_Sword , 0x00),
    (Names.Light_Sword, 0x01),
    (Names.Antiquity  , 0x02),
]

defence_progression_dict = [
    ("None"          , 0xFF),
    (Names.Lucky_Charm, 0x00),
    (Names.Bear_Claw, 0x01),
    (Names.Battle_Clothes, 0x02),
]

chest_addresses = [
    0x2613A0, 0x261490, 0x262254, 0x261458, 0x261480, 0x261870, 0x26205C, 0x26224C, 0x26230C, 0x2623E4, 
    0x262444, 0x263114, 0x25FF68, 0x260E90, 0x260F28, 0x261030, 0x261090, 0x261DBC, 0x261F94, 0x262064, 
    0x262314, 0x2623F4, 0x262FB4, 0x2600A4, 0x261488, 0x261658, 0x2616E0, 0x262F9C, 0x26311C, 0x2631C4, 
    0x2600AC, 0x26033C, 0x261BAC, 0x26090C, 0x260BB4, 0x261928, 0x26203C, 0x260584, 0x260594, 0x260E80, 
    0x260E88, 0x260F20, 0x260F58, 0x2612F0, 0x2615C8, 0x2616F0, 0x261CF4, 0x261CFC, 0x261D9C, 0x26231C, 
    0x2623D4, 0x262404, 0x260194, 0x2609E4, 0x261390, 0x261678, 0x2621D4, 0x262664, 0x262B04, 0x262E9C, 
    0x26309C, 0x26338C, 0x25FD08, 0x260F10, 0x261218, 0x2615D0, 0x261660, 0x261B18, 0x261BFC, 0x262024, 
    0x26232C, 0x262AB4, 0x262DA4, 0x262F74, 0x2609EC, 0x26265C, 0x262F84, 0x263384, 0x26057C, 0x2606FC, 
    0x261450, 0x261478, 0x2614E8, 0x261920, 0x261BF4, 0x261DC4, 0x262044, 0x26243C, 0x262AFC, 0x262E94, 
    0x262FA4, 0x25FD68, 0x25FE60, 0x25FED8, 0x25FF60, 0x26008C, 0x26031C, 0x26058C, 0x260F18, 0x261668, 
    0x2616E8, 0x261930, 0x261A28, 0x25FC48, 0x25FC50, 0x25FCB8, 0x25FDD0, 0x260054, 0x260134, 0x26018C, 
    0x2602CC, 0x260484, 0x2604BC, 0x260564, 0x2606EC, 0x2607AC, 0x2608A4, 0x260BC4, 0x262054, 0x2623DC, 
    0x260FB8, 0x261B10, 0x2623FC, 0x2630A4, 0x25FE58, 0x2612F8, 0x261300, 0x261398, 0x2613A8, 0x261670, 
    0x2616F8, 0x261B28, 0x261E04, 0x261F9C, 0x262034, 0x2621DC, 0x2623AC, 0x2623EC, 0x2631BC, 0x261B20, 
    0x261EC4, 0x25FC40, 0x25FC58, 0x25FCB0, 0x25FE50, 0x25FEE0, 0x26005C, 0x26006C, 0x26007C, 0x260244, 
    0x2602D4, 0x260324, 0x2607E4, 0x260914, 0x2609DC, 0x260B44, 0x260BBC, 0x261FA4, 0x26202C, 0x262F6C, 
    0x261B08, 0x262F7C, 0x260094, 0x2607A4, 0x260E48, 0x261220, 0x261388, 0x261FEC, 0x261FF4, 0x261FFC, 
    0x2621CC, 0x262324, 0x262D9C, 0x2603DC, 0x25FBD0, 0x25FC60, 0x25FD70, 0x25FE68, 0x2601A4, 0x2606F4, 
    0x26083C, 0x2612E8, 0x261308, 0x26204C, 0x262334, 0x25FF58, 0x260064, 0x260074, 0x260234, 0x2602C4, 
    0x26032C, 0x26055C, 0x26087C, 0x26089C, 0x261C04, 0x262AF4, 0x262FAC, 0x260574, 0x25FBD8, 0x260084, 
    0x26019C, 0x26023C, 0x2608D4, 0x25FBC8, 0x25FBE0, 0x26012C, 0x26022C, 0x260334, 0x260394, 0x2603E4, 
    0x2603EC, 0x26056C, 0x260874, 0x261EBC, 0x262D94,
]

#Todo: Fact-check flags
collectible_location_flags = [
    FlagData(f"{Names.Eastern_Cemetery} {Names.Chest} 1",0x1ea8, 0x1ea8 - 0x1ea8, 0, Names.Chest), 
    FlagData(f"{Names.Eastern_Cemetery} {Names.Chest} 2",0x1ea8, 0x1ea8 - 0x1ea8, 1, Names.Chest), 
    FlagData(f"{Names.Eastern_Cemetery} {Names.Chest} 3",0x1ea8, 0x1ea8 - 0x1ea8, 2, Names.Chest), 
    FlagData(f"{Names.Eastern_Cemetery} {Names.Chest} 4",0x1ea8, 0x1ea8 - 0x1ea8, 3, Names.Chest), 
    FlagData(f"{Names.Eastern_Cemetery} {Names.Chest} 5",0x1ea8, 0x1ea8 - 0x1ea8, 4, Names.Chest), 
    FlagData(f"{Names.Eastern_Cemetery} {Names.Chest} 6",0x1ea8, 0x1ea8 - 0x1ea8, 5, Names.Chest), 
    FlagData(f"{Names.Eastern_Cemetery} {Names.Chest} 7",0x1ea8, 0x1ea8 - 0x1ea8, 6, Names.Chest), 
    FlagData(f"{Names.Eastern_Cemetery} {Names.Chest} 8",0x1ea8, 0x1ea8 - 0x1ea8, 7, Names.Chest),
    FlagData(f"{Names.Eastern_Cemetery} {Names.Chest} 9",0x1eac, 0x1eac - 0x1ea8, 0, Names.Chest), 
    FlagData(f"{Names.Eastern_Cemetery} {Names.Chest} 10",0x1eac, 0x1eac - 0x1ea8, 1, Names.Chest), 
    FlagData(f"{Names.Eastern_Cemetery} {Names.Chest} 11",0x1eac, 0x1eac - 0x1ea8, 2, Names.Chest), 
    FlagData(f"{Names.Eastern_Cemetery} {Names.Chest} 12",0x1eac, 0x1eac - 0x1ea8, 3, Names.Chest), 
    FlagData(f"{Names.Eastern_Cemetery} {Names.Magatama_Bead} 1",0x1eac, 0x1eac - 0x1ea8, 4, Names.Magatama_Bead), 
    FlagData(f"{Names.Eastern_Cemetery} {Names.Magatama_Bead} 2",0x1eac, 0x1eac - 0x1ea8, 5, Names.Magatama_Bead), 
    FlagData(f"{Names.Eastern_Cemetery} {Names.Chest} 13",0x1eac, 0x1eac - 0x1ea8, 6, Names.Chest), 
    FlagData(f"{Names.Eastern_Cemetery} {Names.Chest} 14",0x1eac, 0x1eac - 0x1ea8, 7, Names.Chest),
    FlagData(f"{Names.Eastern_Cemetery} {Names.Chest} 15",0x1eb0, 0x1eb0 - 0x1ea8, 0, Names.Chest), 
    FlagData(f"{Names.Eastern_Cemetery} {Names.Headphones}",0x1eb0, 0x1eb0 - 0x1ea8, 1, Names.Headphones), 
    FlagData(f"{Names.Eastern_Cemetery} {Names.Chest} 16",0x1eb0, 0x1eb0 - 0x1ea8, 2, Names.Chest), 
    FlagData(f"{Names.Eastern_Cemetery} {Names.Chest} 17",0x1eb0, 0x1eb0 - 0x1ea8, 3, Names.Chest),
    FlagData(f"{Names.Eastern_Cemetery} {Names.Chest} 18",0x1eb0, 0x1eb0 - 0x1ea8, 4, Names.Chest),
    FlagData(f"{Names.Eastern_Cemetery} {Names.Chest} 19",0x1eb0, 0x1eb0 - 0x1ea8, 5, Names.Chest),
    FlagData(f"{Names.Eastern_Cemetery} {Names.Chest} 20",0x1eb0, 0x1eb0 - 0x1ea8, 6, Names.Chest),
    FlagData(f"{Names.Eastern_Cemetery} {Names.Chest} 21",0x1eb0, 0x1eb0 - 0x1ea8, 7, Names.Chest),
    #Todo: Add more?
    FlagData(f"{Names.Eastern_Cemetery} {Names.Magatama_Bead} 3",0x1eb4, 0x1eb4 - 0x1ea8, 0, Names.Magatama_Bead),
    FlagData(f"{Names.Northern_Fields} {Names.Chest} 1",0x1f28, 0x1f28 - 0x1ea8, 0, Names.Chest), 
    FlagData(f"{Names.Northern_Fields} {Names.Chest} 2",0x1f28, 0x1f28 - 0x1ea8, 1, Names.Chest), 
    FlagData(f"{Names.Northern_Fields} {Names.Chest} 3",0x1f28, 0x1f28 - 0x1ea8, 2, Names.Chest), 
    FlagData(f"{Names.Northern_Fields} {Names.Chest} 4",0x1f28, 0x1f28 - 0x1ea8, 3, Names.Chest), 
    FlagData(f"{Names.Northern_Fields} {Names.Chest} 5",0x1f28, 0x1f28 - 0x1ea8, 4, Names.Chest), 
    FlagData(f"{Names.Northern_Fields} {Names.Chest} 6",0x1f28, 0x1f28 - 0x1ea8, 5, Names.Chest), 
    FlagData(f"{Names.Northern_Fields} {Names.Chest} 7",0x1f28, 0x1f28 - 0x1ea8, 6, Names.Chest), 
    FlagData(f"{Names.Northern_Fields} {Names.Chest} 8",0x1f28, 0x1f28 - 0x1ea8, 7, Names.Chest),
    FlagData(f"{Names.Northern_Fields} {Names.Chest} 9",0x1f2c, 0x1f2c - 0x1ea8, 0, Names.Chest), 
    FlagData(f"{Names.Northern_Fields} {Names.Chest} 10",0x1f2c, 0x1f2c - 0x1ea8, 2, Names.Chest), 
    FlagData(f"{Names.Northern_Fields} {Names.Chest} 11",0x1f2c, 0x1f2c - 0x1ea8, 3, Names.Chest), 
    FlagData(f"{Names.Northern_Fields} {Names.Chest} 12",0x1f2c, 0x1f2c - 0x1ea8, 4, Names.Chest), 
    FlagData(f"{Names.Northern_Fields} {Names.Lucky_Charm}",0x1f2c, 0x1f2c - 0x1ea8, 5, Names.Lucky_Charm), 
    FlagData(f"{Names.Northern_Fields} {Names.Chest} 13",0x1f2c, 0x1f2c - 0x1ea8, 6, Names.Chest), 
    FlagData(f"{Names.Northern_Fields} {Names.Chest} 14",0x1f2c, 0x1f2c - 0x1ea8, 7, Names.Chest),
    FlagData(f"{Names.Northern_Fields} {Names.Chest} 15",0x1f30, 0x1f30 - 0x1ea8, 0, Names.Chest), 
    FlagData(f"{Names.Northern_Fields} {Names.Chest} 16",0x1f30, 0x1f30 - 0x1ea8, 1, Names.Chest), 
    FlagData(f"{Names.Northern_Fields} {Names.Magatama_Bead} 1",0x1f30, 0x1f30 - 0x1ea8, 2, Names.Magatama_Bead), 
    FlagData(f"{Names.Northern_Fields} {Names.Chest} 17",0x1f30, 0x1f30 - 0x1ea8, 3, Names.Chest), 
    FlagData(f"{Names.Northern_Fields} {Names.Chest} 18",0x1f30, 0x1f30 - 0x1ea8, 4, Names.Chest), 
    FlagData(f"{Names.Northern_Fields} {Names.Chest} 19",0x1f30, 0x1f30 - 0x1ea8, 5, Names.Chest), 
    FlagData(f"{Names.Northern_Fields} {Names.Chest} 20",0x1f30, 0x1f30 - 0x1ea8, 6, Names.Chest), 
    FlagData(f"{Names.Northern_Fields} {Names.Left_Glove}",0x1f30, 0x1f30 - 0x1ea8, 7, Names.Left_Glove),
    FlagData(f"{Names.Northern_Fields} {Names.Magatama_Bead} 2",0x1f34, 0x1f34 - 0x1ea8, 0, Names.Magatama_Bead), 
    FlagData(f"{Names.Northern_Fields} {Names.Chest} 21",0x1f34, 0x1f34 - 0x1ea8, 1, Names.Chest), 
    FlagData(f"{Names.Northern_Fields} {Names.Chest} 22",0x1f34, 0x1f34 - 0x1ea8, 2, Names.Chest), 
    FlagData(f"{Names.Northern_Fields} {Names.Chest} 23",0x1f34, 0x1f34 - 0x1ea8, 3, Names.Chest), 
    FlagData(f"{Names.Northern_Fields} {Names.Chest} 24",0x1f34, 0x1f34 - 0x1ea8, 4, Names.Chest), 
    FlagData(f"{Names.Northern_Fields} {Names.Chest} 25",0x1f34, 0x1f34 - 0x1ea8, 5, Names.Chest), 
    FlagData(f"{Names.Northern_Fields} {Names.Chest} 26",0x1f34, 0x1f34 - 0x1ea8, 6, Names.Chest), 
    FlagData(f"{Names.Northern_Fields} {Names.Chest} 27",0x1f34, 0x1f34 - 0x1ea8, 7, Names.Chest),
    FlagData(f"{Names.Northern_Fields} {Names.Chest} 28",0x1f38, 0x1f38 - 0x1ea8, 0, Names.Chest), 
    FlagData(f"{Names.Northern_Fields} {Names.Chest} 29",0x1f38, 0x1f38 - 0x1ea8, 1, Names.Chest), 
    FlagData(f"{Names.Northern_Fields} {Names.Leaf} 1",0x1f38, 0x1f38 - 0x1ea8, 2, Names.Leaf), 
    FlagData(f"{Names.Northern_Fields} {Names.Leaf} 2",0x1f38, 0x1f38 - 0x1ea8, 3, Names.Leaf), 
    FlagData(f"{Names.Northern_Fields} {Names.Leaf} 3",0x1f38, 0x1f38 - 0x1ea8, 4, Names.Leaf), 
    FlagData(f"{Names.Northern_Fields} {Names.Chest} 30",0x1f38, 0x1f38 - 0x1ea8, 5, Names.Chest), 
    FlagData(f"{Names.Northern_Fields} {Names.Chest} 31",0x1f38, 0x1f38 - 0x1ea8, 6, Names.Chest), 
    FlagData(f"{Names.Northern_Fields} {Names.Chest} 32",0x1f38, 0x1f38 - 0x1ea8, 7, Names.Chest),
    FlagData(f"{Names.Western_Cemetery} {Names.Chest} 1",0x1fa8, 0x1fa8 - 0x1ea8, 0, Names.Chest), 
    FlagData(f"{Names.Western_Cemetery} {Names.Magatama_Bead} 1",0x1fa8, 0x1fa8 - 0x1ea8, 1, Names.Magatama_Bead), 
    FlagData(f"{Names.Western_Cemetery} {Names.Chest} 2",0x1fa8, 0x1fa8 - 0x1ea8, 2, Names.Chest), 
    FlagData(f"{Names.Western_Cemetery} {Names.Chest} 3",0x1fa8, 0x1fa8 - 0x1ea8, 3, Names.Chest), 
    FlagData(f"{Names.Western_Cemetery} {Names.Chest} 4",0x1fa8, 0x1fa8 - 0x1ea8, 4, Names.Chest), 
    FlagData(f"{Names.Western_Cemetery} {Names.Chest} 5",0x1fa8, 0x1fa8 - 0x1ea8, 5, Names.Chest), 
    FlagData(f"{Names.Western_Cemetery} {Names.Chest} 6",0x1fa8, 0x1fa8 - 0x1ea8, 6, Names.Chest), 
    FlagData(f"{Names.Western_Cemetery} {Names.Chest} 7",0x1fa8, 0x1fa8 - 0x1ea8, 7, Names.Chest),
    FlagData(f"{Names.Western_Cemetery} {Names.Chest} 8",0x1fac, 0x1fac - 0x1ea8, 0, Names.Chest), 
    FlagData(f"{Names.Western_Cemetery} {Names.Chest} 9",0x1fac, 0x1fac - 0x1ea8, 1, Names.Chest), 
    FlagData(f"{Names.Western_Cemetery} {Names.Chest} 10",0x1fac, 0x1fac - 0x1ea8, 2, Names.Chest), 
    FlagData(f"{Names.Western_Cemetery} {Names.Right_Sandal}",0x1fac, 0x1fac - 0x1ea8, 3, Names.Right_Sandal), 
    FlagData(f"{Names.Western_Cemetery} {Names.Chest} 11",0x1fac, 0x1fac - 0x1ea8, 4, Names.Chest), 
    FlagData(f"{Names.Western_Cemetery} {Names.Chest} 12",0x1fac, 0x1fac - 0x1ea8, 5, Names.Chest), 
    FlagData(f"{Names.Western_Cemetery} {Names.Chest} 13",0x1fac, 0x1fac - 0x1ea8, 6, Names.Chest), 
    FlagData(f"{Names.Western_Cemetery} {Names.Magatama_Bead} 2",0x1fac, 0x1fac - 0x1ea8, 7, Names.Magatama_Bead),
    FlagData(f"{Names.Western_Cemetery} {Names.Chest} 14",0x1fb0, 0x1fb0 - 0x1ea8, 0, Names.Chest), 
    FlagData(f"{Names.Western_Cemetery} {Names.Chest} 15",0x1fb0, 0x1fb0 - 0x1ea8, 1, Names.Chest), 
    FlagData(f"{Names.Western_Cemetery} {Names.Chest} 16",0x1fb0, 0x1fb0 - 0x1ea8, 2, Names.Chest), 
    FlagData(f"{Names.Western_Cemetery} {Names.Chest} 17",0x1fb0, 0x1fb0 - 0x1ea8, 3, Names.Chest), 
    FlagData(f"{Names.Western_Cemetery} {Names.Chest} 18",0x1fb0, 0x1fb0 - 0x1ea8, 4, Names.Chest), 
    FlagData(f"{Names.Western_Cemetery} {Names.Chest} 19",0x1fb0, 0x1fb0 - 0x1ea8, 5, Names.Chest), 
    FlagData(f"{Names.Western_Cemetery} {Names.Chest} 20",0x1fb0, 0x1fb0 - 0x1ea8, 6, Names.Chest), 
    FlagData(f"{Names.Western_Cemetery} {Names.Chest} 21",0x1fb0, 0x1fb0 - 0x1ea8, 7, Names.Chest),
    FlagData(f"{Names.Western_Cemetery} {Names.Chest} 22",0x1fb4, 0x1fb4 - 0x1ea8, 0, Names.Chest), 
    FlagData(f"{Names.Western_Cemetery} {Names.Chest} 23",0x1fb4, 0x1fb4 - 0x1ea8, 1, Names.Chest), 
    FlagData(f"{Names.Western_Cemetery} {Names.Chest} 24",0x1fb4, 0x1fb4 - 0x1ea8, 2, Names.Chest), 
    FlagData(f"{Names.Western_Cemetery} {Names.Chest} 25",0x1fb4, 0x1fb4 - 0x1ea8, 3, Names.Chest), 
    FlagData(f"{Names.Western_Cemetery} {Names.Chest} 26",0x1fb4, 0x1fb4 - 0x1ea8, 4, Names.Chest), 
    FlagData(f"{Names.Western_Cemetery} {Names.Chest} 27",0x1fb4, 0x1fb4 - 0x1ea8, 5, Names.Chest), 
    FlagData(f"{Names.Western_Cemetery} {Names.Chest} 28",0x1fb4, 0x1fb4 - 0x1ea8, 6, Names.Chest), 
    FlagData(f"{Names.Western_Cemetery} {Names.Chest} 29",0x1fb4, 0x1fb4 - 0x1ea8, 7, Names.Chest),
    FlagData(f"{Names.Western_Cemetery} {Names.Chest} 30",0x1fb8, 0x1fb8 - 0x1ea8, 0, Names.Chest), 
    FlagData(f"{Names.Western_Cemetery} {Names.Chest} 31",0x1fb8, 0x1fb8 - 0x1ea8, 1, Names.Chest),
    FlagData(f"{Names.Southern_Mountains} {Names.Magatama_Bead} 1",0x2028, 0x2028 - 0x1ea8, 0, Names.Magatama_Bead), 
    FlagData(f"{Names.Southern_Mountains} {Names.Chest} 1",0x2028, 0x2028 - 0x1ea8, 1, Names.Chest), 
    FlagData(f"{Names.Southern_Mountains} {Names.Left_Sandal}",0x2028, 0x2028 - 0x1ea8, 2, Names.Left_Sandal), 
    FlagData(f"{Names.Southern_Mountains} {Names.Chest} 2",0x2028, 0x2028 - 0x1ea8, 3, Names.Chest), 
    FlagData(f"{Names.Southern_Mountains} {Names.Chest} 3",0x2028, 0x2028 - 0x1ea8, 4, Names.Chest), 
    FlagData(f"{Names.Southern_Mountains} {Names.Chest} 4",0x2028, 0x2028 - 0x1ea8, 5, Names.Chest), 
    FlagData(f"{Names.Southern_Mountains} {Names.Chest} 5",0x2028, 0x2028 - 0x1ea8, 6, Names.Chest), 
    FlagData(f"{Names.Southern_Mountains} {Names.Chest} 6",0x2028, 0x2028 - 0x1ea8, 7, Names.Chest),
    FlagData(f"{Names.Southern_Mountains} {Names.Chest} 7",0x202c, 0x202c - 0x1ea8, 0, Names.Chest), 
    FlagData(f"{Names.Southern_Mountains} {Names.Chest} 8",0x202c, 0x202c - 0x1ea8, 1, Names.Chest), 
    FlagData(f"{Names.Southern_Mountains} {Names.Chest} 9",0x202c, 0x202c - 0x1ea8, 2, Names.Chest), 
    FlagData(f"{Names.Southern_Mountains} {Names.Chest} 10",0x202c, 0x202c - 0x1ea8, 3, Names.Chest), 
    FlagData(f"{Names.Southern_Mountains} {Names.Magatama_Bead} 2",0x202c, 0x202c - 0x1ea8, 4, Names.Magatama_Bead), 
    FlagData(f"{Names.Southern_Mountains} {Names.Chest} 11",0x202c, 0x202c - 0x1ea8, 5, Names.Chest), 
    FlagData(f"{Names.Southern_Mountains} {Names.Chest} 12",0x202c, 0x202c - 0x1ea8, 6, Names.Chest), 
    FlagData(f"{Names.Southern_Mountains} {Names.Chest} 13",0x202c, 0x202c - 0x1ea8, 7, Names.Chest),
    FlagData(f"{Names.Southern_Mountains} {Names.Chest} 14",0x2030, 0x2030 - 0x1ea8, 1, Names.Chest),
    FlagData(f"{Names.Jungle_Ruins} {Names.Chest} 1",0x20a8, 0x20a8 - 0x1ea8, 0, Names.Chest), 
    FlagData(f"{Names.Jungle_Ruins} {Names.Chest} 2",0x20a8, 0x20a8 - 0x1ea8, 1, Names.Chest), 
    FlagData(f"{Names.Jungle_Ruins} {Names.Chest} 3",0x20a8, 0x20a8 - 0x1ea8, 2, Names.Chest), 
    FlagData(f"{Names.Jungle_Ruins} {Names.Chest} 4",0x20a8, 0x20a8 - 0x1ea8, 3, Names.Chest), 
    FlagData(f"{Names.Jungle_Ruins} {Names.Chest} 5",0x20a8, 0x20a8 - 0x1ea8, 4, Names.Chest), 
    FlagData(f"{Names.Jungle_Ruins} {"???"}",0x20a8, 0x20a8 - 0x1ea8, 5, "???"),
    FlagData(f"{Names.Jungle_Ruins} {Names.Chest} 6",0x20ac, 0x20ac - 0x1ea8, 0, Names.Chest), 
    FlagData(f"{Names.Jungle_Ruins} {Names.Chest} 7",0x20ac, 0x20ac - 0x1ea8, 1, Names.Chest), 
    FlagData(f"{Names.Jungle_Ruins} {Names.Chest} 8",0x20ac, 0x20ac - 0x1ea8, 2, Names.Chest), 
    FlagData(f"{Names.Jungle_Ruins} {Names.Chest} 9",0x20ac, 0x20ac - 0x1ea8, 3, Names.Chest), 
    FlagData(f"{Names.Jungle_Ruins} {Names.Chest} 10",0x20ac, 0x20ac - 0x1ea8, 4, Names.Chest), 
    FlagData(f"{Names.Jungle_Ruins} {Names.Chest} 11",0x20ac, 0x20ac - 0x1ea8, 5, Names.Chest), 
    FlagData(f"{Names.Jungle_Ruins} {Names.Chest} 12",0x20ac, 0x20ac - 0x1ea8, 6, Names.Chest), 
    FlagData(f"{Names.Jungle_Ruins} {Names.Chest} 13",0x20ac, 0x20ac - 0x1ea8, 7, Names.Chest),
    FlagData(f"{Names.Jungle_Ruins} {Names.Chest} 14",0x20b0, 0x20b0 - 0x1ea8, 0, Names.Chest), 
    FlagData(f"{Names.Jungle_Ruins} {Names.Magatama_Bead} 1",0x20b0, 0x20b0 - 0x1ea8, 1, Names.Magatama_Bead), 
    FlagData(f"{Names.Jungle_Ruins} {Names.Chest} 15",0x20b0, 0x20b0 - 0x1ea8, 2, Names.Chest), 
    FlagData(f"{Names.Jungle_Ruins} {Names.Chest} 16",0x20b0, 0x20b0 - 0x1ea8, 3, Names.Chest), 
    FlagData(f"{Names.Jungle_Ruins} {Names.Chest} 17",0x20b0, 0x20b0 - 0x1ea8, 4, Names.Chest), 
    FlagData(f"{Names.Jungle_Ruins} {Names.Chest} 18",0x20b0, 0x20b0 - 0x1ea8, 5, Names.Chest), 
    FlagData(f"{Names.Jungle_Ruins} {Names.Chest} 19",0x20b0, 0x20b0 - 0x1ea8, 6, Names.Chest), 
    FlagData(f"{Names.Jungle_Ruins} {Names.Chest} 20",0x20b0, 0x20b0 - 0x1ea8, 7, Names.Chest),
    FlagData(f"{Names.Jungle_Ruins} {Names.Chest} 21",0x20b4, 0x20b4 - 0x1ea8, 0, Names.Chest), 
    FlagData(f"{Names.Jungle_Ruins} {Names.Chest} 22",0x20b4, 0x20b4 - 0x1ea8, 1, Names.Chest), 
    FlagData(f"{Names.Jungle_Ruins} {Names.Chest} 23",0x20b4, 0x20b4 - 0x1ea8, 2, Names.Chest), 
    FlagData(f"{Names.Jungle_Ruins} {Names.Chest} 24",0x20b4, 0x20b4 - 0x1ea8, 3, Names.Chest), 
    FlagData(f"{Names.Jungle_Ruins} {Names.Chest} 25",0x20b4, 0x20b4 - 0x1ea8, 4, Names.Chest), 
    FlagData(f"{Names.Jungle_Ruins} {Names.Magatama_Bead} 2",0x20b4, 0x20b4 - 0x1ea8, 5, Names.Magatama_Bead), 
    FlagData(f"{Names.Jungle_Ruins} {Names.Chest} 26",0x20b4, 0x20b4 - 0x1ea8, 6, Names.Chest), 
    FlagData(f"{Names.Jungle_Ruins} {Names.Magatama_Bead} 3",0x20b4, 0x20b4 - 0x1ea8, 7, Names.Magatama_Bead),
    FlagData(f"{Names.Jungle_Ruins} {Names.Chest} 27",0x20b8, 0x20b8 - 0x1ea8, 0, Names.Chest), 
    FlagData(f"{Names.Jungle_Ruins} {Names.Chest} 28",0x20b8, 0x20b8 - 0x1ea8, 1, Names.Chest), 
    FlagData(f"{Names.Jungle_Ruins} {Names.Chest} 29",0x20b8, 0x20b8 - 0x1ea8, 2, Names.Chest), 
    FlagData(f"{Names.Jungle_Ruins} {Names.Chest} 30",0x20b8, 0x20b8 - 0x1ea8, 3, Names.Chest), 
    FlagData(f"{Names.Jungle_Ruins} {Names.Chest} 31",0x20b8, 0x20b8 - 0x1ea8, 4, Names.Chest), 
    FlagData(f"{Names.Jungle_Ruins} {Names.Chest} 32",0x20b8, 0x20b8 - 0x1ea8, 5, Names.Chest), 
    FlagData(f"{Names.Jungle_Ruins} {Names.Chest} 33",0x20b8, 0x20b8 - 0x1ea8, 6, Names.Chest), 
    FlagData(f"{Names.Jungle_Ruins} {Names.Chest} 34",0x20b8, 0x20b8 - 0x1ea8, 7, Names.Chest),
    FlagData(f"{Names.Jungle_Ruins} {Names.Chest} 35",0x20bc, 0x20bc - 0x1ea8, 0, Names.Chest),
    FlagData(f"{Names.Tao_Grounds} {Names.Chest} 1",0x2128, 0x2128 - 0x1ea8, 0, Names.Chest), 
    FlagData(f"{Names.Tao_Grounds} {Names.Chest} 2",0x2128, 0x2128 - 0x1ea8, 1, Names.Chest), 
    FlagData(f"{Names.Tao_Grounds} {Names.Chest} 3",0x2128, 0x2128 - 0x1ea8, 2, Names.Chest), 
    FlagData(f"{Names.Tao_Grounds} {Names.Chest} 4",0x2128, 0x2128 - 0x1ea8, 3, Names.Chest), 
    FlagData(f"{Names.Tao_Grounds} {Names.Chest} 5",0x2128, 0x2128 - 0x1ea8, 4, Names.Chest), 
    FlagData(f"{Names.Tao_Grounds} {Names.Chest} 6",0x2128, 0x2128 - 0x1ea8, 5, Names.Chest), 
    FlagData(f"{Names.Tao_Grounds} {Names.Chest} 7",0x2128, 0x2128 - 0x1ea8, 6, Names.Chest),
    FlagData(f"{Names.Tao_Grounds} {Names.Chest} 8",0x212c, 0x212c - 0x1ea8, 1, Names.Chest), 
    FlagData(f"{Names.Tao_Grounds} {Names.Chest} 9",0x212c, 0x212c - 0x1ea8, 2, Names.Chest), 
    FlagData(f"{Names.Tao_Grounds} {Names.Chest} 10",0x212c, 0x212c - 0x1ea8, 3, Names.Chest), 
    FlagData(f"{Names.Tao_Grounds} {Names.Bear_Claw}",0x212c, 0x212c - 0x1ea8, 4, Names.Bear_Claw), 
    FlagData(f"{Names.Tao_Grounds} {Names.Chest} 11",0x212c, 0x212c - 0x1ea8, 5, Names.Chest), 
    FlagData(f"{Names.Tao_Grounds} {Names.Chest} 12",0x212c, 0x212c - 0x1ea8, 6, Names.Chest), 
    FlagData(f"{Names.Tao_Grounds} {Names.Chest} 13",0x212c, 0x212c - 0x1ea8, 7, Names.Chest),
    FlagData(f"{Names.Tao_Grounds} {Names.Chest} 14",0x2130, 0x2130 - 0x1ea8, 0, Names.Chest), 
    FlagData(f"{Names.Tao_Grounds} {Names.Chest} 15",0x2130, 0x2130 - 0x1ea8, 1, Names.Chest), 
    FlagData(f"{Names.Tao_Grounds} {Names.Chest} 16",0x2130, 0x2130 - 0x1ea8, 2, Names.Chest),
    FlagData(f"{Names.Tao_Grounds} {Names.Magatama_Bead} 1",0x2134, 0x2134 - 0x1ea8, 4, Names.Magatama_Bead), 
    FlagData(f"{Names.Tao_Grounds} {Names.Chest} 17",0x2134, 0x2134 - 0x1ea8, 5, Names.Chest), 
    FlagData(f"{Names.Tao_Grounds} {Names.Chest} 18",0x2134, 0x2134 - 0x1ea8, 6, Names.Chest), 
    FlagData(f"{Names.Tao_Grounds} {Names.Chest} 19",0x2134, 0x2134 - 0x1ea8, 7, Names.Chest),
    FlagData(f"{Names.Tao_Grounds} {Names.Magatama_Bead} 2",0x2138, 0x2138 - 0x1ea8, 0, Names.Magatama_Bead), 
    FlagData(f"{Names.Tao_Grounds} {"???"}",0x2138, 0x2138 - 0x1ea8, 1, "???"),
    FlagData(f"{Names.Tao_Grounds} {"???"}",0x2138, 0x2138 - 0x1ea8, 2, "???"),
    FlagData(f"{Names.Tao_Grounds} {Names.Chest} 20",0x2138, 0x2138 - 0x1ea8, 3, Names.Chest), 
    FlagData(f"{Names.Tao_Grounds} {Names.Chest} 21",0x2138, 0x2138 - 0x1ea8, 4, Names.Chest), 
    FlagData(f"{Names.Tao_Grounds} {Names.Chest} 22",0x2138, 0x2138 - 0x1ea8, 5, Names.Chest), 
    FlagData(f"{Names.Tao_Grounds} {Names.Chest} 23",0x2138, 0x2138 - 0x1ea8, 6, Names.Chest), 
    FlagData(f"{Names.Tao_Grounds} {Names.Chest} 24",0x2138, 0x2138 - 0x1ea8, 7, Names.Chest),
    FlagData(f"{Names.Tao_Grounds} {Names.Chest} 25",0x213c, 0x213c - 0x1ea8, 0, Names.Chest), 
    FlagData(f"{Names.Tao_Grounds} {Names.Magatama_Bead} 3",0x213c, 0x213c - 0x1ea8, 1, Names.Magatama_Bead), 
    FlagData(f"{Names.Tao_Grounds} {Names.Chest} 26",0x213c, 0x213c - 0x1ea8, 2, Names.Chest), 
    FlagData(f"{Names.Tao_Grounds} {Names.Chest} 27",0x213c, 0x213c - 0x1ea8, 3, Names.Chest), 
    FlagData(f"{Names.Tao_Grounds} {Names.Chest} 28",0x213c, 0x213c - 0x1ea8, 4, Names.Chest), 
    FlagData(f"{Names.Tao_Grounds} {Names.Chest} 29",0x213c, 0x213c - 0x1ea8, 5, Names.Chest), 
    FlagData(f"{Names.Tao_Grounds} {Names.Chest} 30",0x213c, 0x213c - 0x1ea8, 6, Names.Chest),
    FlagData(f"{Names.Tao_Grounds} {Names.Chest} 31",0x213c, 0x213c - 0x1ea8, 7, Names.Chest),
    FlagData(f"{Names.Tao_Grounds} {Names.Chest} 32",0x2140, 0x2140 - 0x1ea8, 0, Names.Chest), 
    FlagData(f"{Names.Tao_Grounds} {Names.Chest} 33",0x2140, 0x2140 - 0x1ea8, 1, Names.Chest), 
    FlagData(f"{Names.Tao_Grounds} {Names.Chest} 34",0x2140, 0x2140 - 0x1ea8, 2, Names.Chest), 
    FlagData(f"{Names.Tao_Grounds} {Names.Chest} 35",0x2140, 0x2140 - 0x1ea8, 3, Names.Chest),
    FlagData(f"{Names.Industrial_Area} {Names.Chest} 1",0x21a8, 0x21a8 - 0x1ea8, 0, Names.Chest), 
    FlagData(f"{Names.Industrial_Area} {Names.Chest} 2",0x21a8, 0x21a8 - 0x1ea8, 1, Names.Chest), 
    FlagData(f"{Names.Industrial_Area} {Names.Battle_Clothes}",0x21a8, 0x21a8 - 0x1ea8, 2, Names.Battle_Clothes), 
    FlagData(f"{Names.Industrial_Area} {Names.Magatama_Bead} 1",0x21a8, 0x21a8 - 0x1ea8, 3, Names.Magatama_Bead), 
    FlagData(f"{Names.Industrial_Area} {Names.Magatama_Bead} 2",0x21a8, 0x21a8 - 0x1ea8, 4, Names.Magatama_Bead), 
    FlagData(f"{Names.Industrial_Area} {Names.Chest} 3",0x21a8, 0x21a8 - 0x1ea8, 5, Names.Chest), 
    FlagData(f"{Names.Industrial_Area} {Names.Chest} 4",0x21a8, 0x21a8 - 0x1ea8, 6, Names.Chest), 
    FlagData(f"{Names.Industrial_Area} {Names.Chest} 5",0x21a8, 0x21a8 - 0x1ea8, 7, Names.Chest),
    FlagData(f"{Names.Industrial_Area} {Names.Chest} 6",0x21ac, 0x21ac - 0x1ea8, 0, Names.Chest), 
    FlagData(f"{Names.Industrial_Area} {Names.Magatama_Bead} 3",0x21ac, 0x21ac - 0x1ea8, 1, Names.Magatama_Bead),
    FlagData(f"{Names.Ice_Lands} {Names.Magatama_Bead} 1",0x2228, 0x2228 - 0x1ea8, 0, Names.Magatama_Bead), 
    FlagData(f"{Names.Ice_Lands} {Names.Chest} 1",0x2228, 0x2228 - 0x1ea8, 1, Names.Chest), 
    FlagData(f"{Names.Ice_Lands} {Names.Chest} 2",0x2228, 0x2228 - 0x1ea8, 2, Names.Chest), 
    FlagData(f"{Names.Ice_Lands} {Names.Chest} 3",0x2228, 0x2228 - 0x1ea8, 3, Names.Chest), 
    FlagData(f"{Names.Ice_Lands} {Names.Chest} 4",0x2228, 0x2228 - 0x1ea8, 4, Names.Chest), 
    FlagData(f"{Names.Ice_Lands} {Names.Chest} 5",0x2228, 0x2228 - 0x1ea8, 5, Names.Chest), 
    FlagData(f"{Names.Ice_Lands} {Names.Magatama_Bead} 2",0x2228, 0x2228 - 0x1ea8, 6, Names.Magatama_Bead), 
    FlagData(f"{Names.Ice_Lands} {Names.Chest} 6",0x2228, 0x2228 - 0x1ea8, 7, Names.Chest),
    FlagData(f"{Names.Ice_Lands} {Names.Chest} 7",0x222c, 0x222c - 0x1ea8, 0, Names.Chest), 
    FlagData(f"{Names.Ice_Lands} {Names.Chest} 8",0x222c, 0x222c - 0x1ea8, 1, Names.Chest), 
    FlagData(f"{Names.Ice_Lands} {Names.Chest} 9",0x222c, 0x222c - 0x1ea8, 2, Names.Chest), 
    FlagData(f"{Names.Ice_Lands} {Names.Chest} 10",0x222c, 0x222c - 0x1ea8, 3, Names.Chest), 
    FlagData(f"{Names.Ice_Lands} {Names.Chest} 11",0x222c, 0x222c - 0x1ea8, 4, Names.Chest), 
    FlagData(f"{Names.Ice_Lands} {Names.Chest} 12",0x222c, 0x222c - 0x1ea8, 5, Names.Chest), 
    FlagData(f"{Names.Ice_Lands} {Names.Chest} 13",0x222c, 0x222c - 0x1ea8, 6, Names.Chest), 
    FlagData(f"{Names.Ice_Lands} {Names.Chest} 14",0x222c, 0x222c - 0x1ea8, 7, Names.Chest),
    FlagData(f"{Names.Ice_Lands} {Names.Chest} 15",0x2230, 0x2230 - 0x1ea8, 0, Names.Chest), 
    FlagData(f"{Names.Ice_Lands} {Names.Chest} 16",0x2230, 0x2230 - 0x1ea8, 1, Names.Chest), 
    FlagData(f"{Names.Ice_Lands} {Names.Chest} 17",0x2230, 0x2230 - 0x1ea8, 2, Names.Chest), 
    FlagData(f"{Names.Ice_Lands} {Names.Chest} 18",0x2230, 0x2230 - 0x1ea8, 3, Names.Chest), 
    FlagData(f"{Names.Ice_Lands} {Names.Chest} 19",0x2230, 0x2230 - 0x1ea8, 4, Names.Chest), 
    FlagData(f"{Names.Ice_Lands} {Names.Chest} 20",0x2230, 0x2230 - 0x1ea8, 5, Names.Chest), 
    FlagData(f"{Names.Ice_Lands} {Names.Chest} 21",0x2230, 0x2230 - 0x1ea8, 6, Names.Chest),
]

key_location_flags = [
    FlagData(f"{Names.Western_Cemetery} 1 {Names.Key}", 0x1df2, 0x1df2 - 0x1dde, 4, Names.Key),
    FlagData(f"{Names.Western_Cemetery} 5 {Names.Key}", 0x1df6, 0x1df6 - 0x1dde, 4, Names.Key),
    FlagData(f"{Names.Southern_Mountains} 1 {Names.Key}", 0x1dfc, 0x1dfc - 0x1dde, 4, Names.Key),
    FlagData(f"{Names.Southern_Mountains} 2 {Names.Key}", 0x1dfd, 0x1dfd - 0x1dde, 4, Names.Key),
    FlagData(f"{Names.Southern_Mountains} 3 {Names.Key}", 0x1dfe, 0x1dfe - 0x1dde, 4, Names.Key),
    FlagData(f"{Names.Jungle_Ruins} 2 {Names.Key}", 0x1e07, 0x1e07 - 0x1dde, 4, Names.Key),
    FlagData(f"{Names.Tao_Grounds} 1 {Names.Key}", 0x1e10, 0x1e10 - 0x1dde, 4, Names.Key),
    FlagData(f"{Names.Tao_Grounds} 2 {Names.Key}", 0x1e11, 0x1e11 - 0x1dde, 4, Names.Key),
    FlagData(f"{Names.Industrial_Area} 2 {Names.Key}", 0x1e1b, 0x1e1b - 0x1dde, 4, Names.Key),
]

spirit_location_flags = [
    FlagData(f"{Names.Inn} {Names.Intro} {Names.Amidamaru}",        0x232c, 0, 1),
    FlagData(f"{Names.Mosuke_Event} {Names.Mosuke}",                0x232c, 0, 3),
    FlagData(f"{lvl.EC4} {Names.Ryo_Boss} {Names.Tokageroh}",                 0x232c, 0, 5),
    FlagData(f"{lvl.NF4} {Names.Trey_Boss} {Names.Corey}",                    0x232c, 0, 6),
    FlagData(f"{lvl.WC6} {Names.Eliza_Boss} {Names.Eliza}",                   0x232c, 0, 7),
    FlagData(f"{lvl.WC8} {Names.Silver_Shield}",                    0x232d, 1, 0),
    FlagData(f"{lvl.SM7} {Names.Silver_Tail}",                      0x232d, 1, 1),
    FlagData(f"{lvl.WC1} {Names.Silver_Wing}",                      0x232d, 1, 2),
    FlagData(f"{lvl.NF2} {Names.Silver_Horn}",                      0x232d, 1, 3),
    FlagData(f"{lvl.EC4} {Names.Silver_Rod}",                       0x232d, 1, 4),
    FlagData(f"{lvl.JR6} {Names.Joco_Boss} {Names.Mic}",                      0x232d, 1, 6),
    FlagData(f"{lvl.TG3} {Names.Lee_Pai_Long_Boss} {Names.Lee_Pai_Long}",     0x232d, 1, 7),
    FlagData(f"{lvl.TG6} {Names.Len_Tao_Boss} {Names.Bason}",                 0x232e, 2, 0),
    FlagData(f"{lvl.TG8} {Names.En_Tao_Boss} {Names.Grand_Tao_Dragon}",       0x232e, 2, 2),
    FlagData(f"{lvl.IA3} {Names.Lyzerg_Boss} {Names.Chloe}",                  0x232e, 2, 3),
    FlagData(f"{lvl.IA5} {Names.Michael_Boss} {Names.Michael}",               0x232e, 2, 4),
    FlagData(f"{lvl.EC3} {Names.Kanta}",                            0x232e, 2, 6),
    FlagData(f"{lvl.EC2} {Names.Gussy_Kenji}",                      0x232e, 2, 7),
    FlagData(f"{lvl.NF7} {Names.Tamegoroh}",                        0x232f, 3, 0),
    FlagData(f"{lvl.NF6} {Names.Shikigami_Event} {Names.Shikigami}",          0x232f, 3, 1),
    FlagData(f"{lvl.WC3} {Names.Frankensteiny}",                    0x232f, 3, 2),
    FlagData(f"{lvl.WC8} {Names.Ponchi_and_Konchi_Event} {Names.Ponchi}",     0x232f, 3, 3),
    FlagData(f"{lvl.WC8} {Names.Ponchi_and_Konchi_Event} {Names.Konchi}",     0x232f, 3, 4),
    FlagData(f"{lvl.EC3} {Names.Chimi_Moryo}",                      0x232f, 3, 5),
    FlagData(f"{lvl.TG4} {Names.Shaolin}",                          0x232f, 3, 6),
    FlagData(f"{lvl.TG7} {Names.Black_Raven}",                      0x232f, 3, 7),
    FlagData(f"{lvl.TG9} {Names.Tao_the_Great}",                    0x2330, 4, 0),
    FlagData(f"{lvl.NF4} {Names.Ian}",                              0x2330, 4, 1),
    FlagData(f"{lvl.NF1} {Names.Nizba}",                            0x2330, 4, 2),
    FlagData(f"{lvl.WC1} {Names.Dreisa}",                           0x2330, 4, 3),
    FlagData(f"{lvl.WC4} {Names.Yopia}",                            0x2330, 4, 4),
    FlagData(f"{lvl.NF3} {Names.Badbh}",                            0x2330, 4, 6),
    FlagData(f"{lvl.NF3} {Names.Vodianoi}",                         0x2330, 4, 7),
    FlagData(f"{lvl.NF3} {Names.Deht_the_Viking}",                  0x2331, 5, 0),
    FlagData(f"{lvl.TG3} {Names.Gororo}",                           0x2331, 5, 1),
    FlagData(f"{lvl.IL2} {Names.Zenki_and_Kohki_Event} {Names.Zenki}",        0x2331, 5, 2),
    FlagData(f"{lvl.IL2} {Names.Zenki_and_Kohki_Event} {Names.Kohki}",        0x2331, 5, 3),
    FlagData(f"{lvl.IL2} {Names.Golem}",                            0x2331, 5, 4),
    FlagData(f"{lvl.JR5} {Names.Orona}",                            0x2331, 5, 5),
    FlagData(f"{lvl.IL1} {Names.Pascal_Avaf}",                      0x2331, 5, 6),
    FlagData(f"{lvl.SM3} {Names.Yamagami}",                         0x2332, 6, 0),
    FlagData(f"{lvl.TG8} {Names.Gundari}",                          0x2332, 6, 1),
    FlagData(f"{lvl.TG3} {Names.Raphael}",                          0x2332, 6, 2),
    FlagData(f"{lvl.SM3} {Names.Gabriel}",                          0x2332, 6, 3),
    FlagData(f"{lvl.IA2} {Names.Uriel}",                            0x2332, 6, 4),
    FlagData(f"{lvl.IA2} {Names.Metatoron}",                        0x2332, 6, 5),
    FlagData(f"{lvl.IA4} {Names.Sariel}",                           0x2332, 6, 6),
    FlagData(f"{lvl.IA4} {Names.Remiel}",                           0x2332, 6, 7),
    FlagData(f"{Names.Inn} {Names.Mash_Event} {Names.Mash}",                    0x2333, 7, 0),
    FlagData(f"{lvl.TG4} {Names.Blaumro}",                          0x2333, 7, 1),
    FlagData(f"{lvl.IA1} {Names.Footballer}",                       0x2333, 7, 2),
    FlagData(f"{lvl.IA1} {Names.Shion_Shion}",                      0x2333, 7, 3),
    FlagData(f"{lvl.IA1} {Names.Blocks}",                           0x2333, 7, 4),
    FlagData(f"{lvl.SM4} {Names.Jen}",                              0x2333, 7, 5),
    FlagData(f"{lvl.SM3} {Names.Ashcroft}",                         0x2333, 7, 6),
    FlagData(f"{lvl.JR4} {Names.Jack}",                             0x2333, 7, 7),
    FlagData(f"{lvl.JR1} or {lvl.JR4} {Names.Chuck}",               0x2334, 8, 0),
    FlagData(f"{lvl.SM7} {Names.Carlos_and_Joao}",                  0x2334, 8, 1),
    FlagData(f"{lvl.JR5} {Names.Antonio}",                          0x2334, 8, 2),
    FlagData(f"{lvl.SM3} {Names.Jose}",                             0x2334, 8, 3),
    FlagData(f"{lvl.TG3} {Names.Pancho}",                           0x2334, 8, 4),
    FlagData(f"{lvl.TG1} {Names.Zapata}",                           0x2334, 8, 5),
    FlagData(f"{lvl.IA4} {Names.Miguel}",                           0x2334, 8, 6),
    FlagData(f"{lvl.EC4} {Names.Magnescope}",                       0x2335, 9, 0),
    FlagData(f"{lvl.IL1} {Names.Mama}",                             0x2335, 9, 1),
    FlagData(f"{lvl.IL1} {Names.Cifer}",                            0x2335, 9, 2),
    FlagData(f"{lvl.IL3} {Names.Spirit_of_Fire_or_Game_complete_Event} {Names.Spirit_of_Fire}", 0x2335, 9, 3),
    FlagData(f"{lvl.IL2} {Names.Matamune}",                         0x2335, 9, 4),
]

#Ignoring spirit rewards since they are handled along with the regular spirits
boss_and_event_location_flags = [
    FlagData(f"{Names.Ryo_Boss} {Names.Tome_Page}",                0x1e30, 0, 3, FlagType.Boss_Completed),
    FlagData(f"{Names.Shikigami_Event} {Names.Tome_Page}",         0x1e30, 0, 4, FlagType.Event_Completed),
    FlagData(f"{Names.Trey_Boss} {Names.Tome_Page}",               0x1e30, 0, 6, FlagType.Boss_Completed),
    FlagData(f"{Names.Eliza_Boss} {Names.Tome_Page}",              0x1e31, 1, 0, FlagType.Boss_Completed),
    FlagData(f"{Names.Light_Sword_Event} {Names.Light_Sword}",     0x1e31, 1, 1, FlagType.Event_Completed),
    FlagData(f"{Names.Silva_Boss} {Names.Tome_Page}",              0x1e31, 1, 3, FlagType.Boss_Completed),
    FlagData(f"{Names.Joco_Boss} {Names.Tome_Page}",               0x1e31, 1, 5, FlagType.Boss_Completed),
    FlagData(f"{Names.Lee_Pai_Long_Boss} {Names.Tome_Page}",       0x1e32, 2, 0, FlagType.Boss_Completed),
    FlagData(f"{Names.Len_Tao_Boss} {Names.Tome_Page}",            0x1e32, 2, 3, FlagType.Boss_Completed),
    FlagData(f"{Names.En_Tao_Boss} {Names.Tome_Page}",             0x1e32, 2, 6, FlagType.Boss_Completed),
    FlagData(f"{Names.Thunder_Sword_Event} {Names.Thunder_Sword}", 0x1e32, 2, 7, FlagType.Event_Completed),
    FlagData(f"{Names.Lyzerg_Boss} {Names.Tome_Page}",             0x1e33, 3, 1, FlagType.Boss_Completed),
    FlagData(f"{Names.Antiquity_Event} {Names.Antiquity}",         0x1e33, 3, 2, FlagType.Event_Completed),
    FlagData(f"{Names.Michael_Boss} {Names.Tome_Page}",            0x1e33, 3, 4, FlagType.Boss_Completed),
    FlagData(f"{Names.Magister_Boss} {Names.Tome_Page}",           0x1e33, 3, 7, FlagType.Boss_Completed),
]