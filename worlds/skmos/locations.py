from __future__ import annotations

from typing import TYPE_CHECKING
from BaseClasses import ItemClassification, Location
from .game_data import spiritData, itemData, collectible_location_flags, key_location_flags, spirit_location_flags
from .names import Names

if TYPE_CHECKING:
    from .skmosworld import ShamanKingMasterOfSpiritsWorld

item_table = spiritData + itemData
location_table = collectible_location_flags + key_location_flags + spirit_location_flags

LOCATION_NAME_TO_ID = {location.name: i+1 for i, location in enumerate(location_table)}

class ShamanKingMasterOfSpiritsLocation(Location):
    game = Names.Game_Name


# Let's make one more helper method before we begin actually creating locations.
# Later on in the code, we'll want specific subsections of LOCATION_NAME_TO_ID.
# To reduce the chance of copy-paste errors writing something like {"Chest": LOCATION_NAME_TO_ID["Chest"]},
# let's make a helper method that takes a list of location names and returns them as a dict with their IDs.
# Note: There is a minor typing quirk here. Some functions want location addresses to be an "int | None",
# so while our function here only ever returns dict[str, int], we annotate it as dict[str, int | None].
def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: ShamanKingMasterOfSpiritsWorld) -> None:
    create_regular_locations(world)
    #create_events(world)


def create_regular_locations(world: ShamanKingMasterOfSpiritsWorld) -> None:
    # Finally, we need to put the Locations ("checks") into their regions.
    # Once again, before we do anything, we can grab our regions we created by using world.get_region()
    #overworld = world.get_region(Names.Map)
    #top_left_room = world.get_region("Top Left Room")
    #bottom_right_room = world.get_region("Bottom Right Room")
    #right_room = world.get_region("Right Room")

    regions = world.get_regions()
    
    for region in regions:
        region.add_locations(get_location_names_with_ids([flag.name for flag in location_table if (flag.name.startswith(region.name) or region.name == Names.Inn)]), ShamanKingMasterOfSpiritsLocation)

    # One way to create locations is by just creating them directly via their constructor.
    #bottom_left_chest = ShamanKingMasterOfSpiritsLocation(
        #world.player, "Bottom Left Chest", world.location_name_to_id["Bottom Left Chest"], overworld
    #)

    # You can then add them to the region.
    #overworld.locations.append(bottom_left_chest)

    # A simpler way to do this is by using the region.add_locations helper.
    # For this, you need to have a dict of location names to their IDs (i.e. a subset of location_name_to_id)
    # Aha! So that's why we made that "get_location_names_with_ids" helper method earlier.
    # You also need to pass your overridden Location class.
    #bottom_right_room_locations = get_location_names_with_ids(
        #["Bottom Right Room Left Chest", "Bottom Right Room Right Chest"]
    #)
    #bottom_right_room.add_locations(bottom_right_room_locations, ShamanKingMasterOfSpiritsLocation)

    #top_left_room_locations = get_location_names_with_ids(["Top Left Room Chest"])
    #top_left_room.add_locations(top_left_room_locations, ShamanKingMasterOfSpiritsLocation)

    #right_room_locations = get_location_names_with_ids(["Right Room Enemy Drop"])
    #right_room.add_locations(right_room_locations, ShamanKingMasterOfSpiritsLocation)

    # Locations may be in different regions depending on the player's options.
    # In our case, the hammer option puts the Top Middle Chest into its own room called Top Middle Room.
    #top_middle_room_locations = get_location_names_with_ids(["Top Middle Chest"])
    #overworld.add_locations(top_middle_room_locations, ShamanKingMasterOfSpiritsLocation)
    #overworld.add_locations(LOCATION_NAME_TO_ID, ShamanKingMasterOfSpiritsLocation)

#def create_events(world: ShamanKingMasterOfSpiritsWorld) -> None:
    # Sometimes, the player may perform in-game actions that allow them to progress which are not related to Items.
    # In our case, the player must press a button in the top left room to open the final boss door.
    # AP has something for this purpose: "Event locations" and "Event items".
    # An event location is no different than a regular location, except it has the address "None".
    # It is treated during generation like any other location, but then it is discarded.
    # This location cannot be "sent" and its item cannot be "received", but the item can be used in logic rules.
    # Since we are creating more locations and adding them to regions, we need to grab those regions again first.
    #top_left_room = world.get_region("Top Left Room")
    #final_boss_room = world.get_region("Final Boss Room")

    # One way to create an event is simply to use one of the normal methods of creating a location.
    #button_in_top_left_room = ShamanKingMasterOfSpiritsLocation(world.player, "Top Left Room Button", None, top_left_room)
    #top_left_room.locations.append(button_in_top_left_room)

    # We then need to put an event item onto the location.
    # An event item is an item whose code is "None" (same as the event location's address),
    # and whose classification is "progression". Item creation will be discussed more in items.py.
    # Note: Usually, items are created in world.create_items(), which for us happens in items.py.
    # However, when the location of an item is known ahead of time (as is the case with an event location/item pair),
    # it is common practice to create the item when creating the location.
    # Since locations also have to be finalized after world.create_regions(), which runs before world.create_items(),
    # we'll create both the event location and the event item in our locations.py code.
    #button_item = items.APQuestItem("Top Left Room Button Pressed", ItemClassification.progression, None, world.player)
    #button_in_top_left_room.place_locked_item(button_item)

    # A way simpler way to do create an event location/item pair is by using the region.create_event helper.
    # Luckily, we have another event we want to create: The Victory event.
    # We will use this event to track whether the player can win the game.
    # The Victory event is a completely optional abstraction - This will be discussed more in set_rules().
    #final_boss_room.add_event(
        #"Final Boss Defeated", "Victory", location_type=ShamanKingMasterOfSpiritsLocation, item_type=items.APQuestItem
    #)

    # If you create all your regions and locations line-by-line like this,
    # the length of your create_regions might get out of hand.
    # Many worlds use more data-driven approaches using dataclasses or NamedTuples.
    # However, it is worth understanding how the actual creation of regions and locations works,
    # That way, we're not just mindlessly copy-pasting! :)
