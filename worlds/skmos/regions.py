from __future__ import annotations

from typing import TYPE_CHECKING
from BaseClasses import Entrance, Region
from .names import Names, AreaLevels
from .game_data import collectible_flags, levels

if TYPE_CHECKING:
    from .skmosworld import ShamanKingMasterOfSpiritsWorld

# A region is a container for locations ("checks"), which connects to other regions via "Entrance" objects.
# Many games will model their Regions after physical in-game places, but you can also have more abstract regions.
# For a location to be in logic, its containing region must be reachable.
# The Entrances connecting regions can have rules - more on that in rules.py.
# This makes regions especially useful for traversal logic ("Can the player reach this part of the map?")

# Every location must be inside a region, and you must have at least one region.
# This is why we create regions first, and then later we create the locations (in locations.py).


def create_and_connect_regions(world: ShamanKingMasterOfSpiritsWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: ShamanKingMasterOfSpiritsWorld) -> None:
    
    region_names = [
        Names.Eastern_Cemetery,
        Names.Northern_Fields,
        Names.Western_Cemetery,
        Names.Southern_Mountains,
        Names.Jungle_Ruins,
        Names.Tao_Grounds,
        Names.Industrial_Area,
        Names.Ice_Lands,
        Names.Map,
        Names.Inn,
    ]
    
    regions = [Region(region, world.player, world.multiworld) for region in region_names]
    world.multiworld.regions += regions


def connect_regions(world: ShamanKingMasterOfSpiritsWorld) -> None:
    # We have regions now, but still need to connect them to each other.
    # But wait, we no longer have access to the region variables we created in create_all_regions()!
    # Luckily, once you've submitted your regions to multiworld.regions,
    # you can get them at any time using world.get_region(...).
    #overworld = world.get_region(Names.Map)
    #top_left_room = world.get_region("Top Left Room")
    #bottom_right_room = world.get_region("Bottom Right Room")
    #right_room = world.get_region("Right Room")
    #final_boss_room = world.get_region("Final Boss Room")


    Eastern_Cemetery = world.get_region(Names.Eastern_Cemetery)
    Northern_Fields = world.get_region(Names.Northern_Fields)
    Western_Cemetery = world.get_region(Names.Western_Cemetery)
    Southern_Mountains = world.get_region(Names.Southern_Mountains)
    Jungle_Ruins = world.get_region(Names.Jungle_Ruins)
    Tao_Grounds = world.get_region(Names.Tao_Grounds)
    Industrial_Area = world.get_region(Names.Industrial_Area)
    Ice_Lands = world.get_region(Names.Ice_Lands)
    Inn = world.get_region(Names.Inn)
    Map = world.get_region(Names.Map)

    Map.connect(Inn)
    
    Inn.connect(Northern_Fields)
    Inn.connect(Eastern_Cemetery)
    Inn.connect(Southern_Mountains)
    Inn.connect(Western_Cemetery)

    Northern_Fields.connect(Eastern_Cemetery)
    Northern_Fields.connect(Inn)
    Northern_Fields.connect(Tao_Grounds)

    Eastern_Cemetery.connect(Northern_Fields)
    Eastern_Cemetery.connect(Jungle_Ruins)
    Eastern_Cemetery.connect(Inn)
    
    Jungle_Ruins.connect(Eastern_Cemetery)
    
    Industrial_Area.connect(Ice_Lands)
    Industrial_Area.connect(Southern_Mountains)
    
    Ice_Lands.connect(Industrial_Area)

    Southern_Mountains.connect(Inn)
    Southern_Mountains.connect(Industrial_Area)
    Southern_Mountains.connect(Western_Cemetery)
    
    Western_Cemetery.connect(Inn)
    Western_Cemetery.connect(Southern_Mountains)
    Western_Cemetery.connect(Tao_Grounds)
    
    Tao_Grounds.connect(Northern_Fields)
    Tao_Grounds.connect(Western_Cemetery)
    
    # Okay, now we can get connecting. For this, we need to create Entrances.
    # Entrances are inherently one-way, but crucially, AP assumes you can always return to the origin region.
    # One way to create an Entrance is by calling the Entrance constructor.
    #overworld_to_bottom_right_room = Entrance(world.player, "Overworld to Bottom Right Room", parent=overworld)
    #overworld.exits.append(overworld_to_bottom_right_room)

    # You can then connect the Entrance to the target region.
    #overworld_to_bottom_right_room.connect(bottom_right_room)

    # An even easier way is to use the region.connect helper.
    #overworld.connect(right_room, "Overworld to Right Room")
    #right_room.connect(final_boss_room, "Right Room to Final Boss Room")
    #overworld.connect(final_boss_room, "Worldmap to Final Boss Room")

    # The region.connect helper even allows adding a rule immediately.
    # We'll talk more about rule creation in the set_all_rules() function in rules.py.
    #overworld.connect(top_left_room, "Overworld to Top Left Room", lambda state: state.has("Key", world.player))
