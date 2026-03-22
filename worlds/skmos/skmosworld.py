from collections.abc import Mapping
from typing import Any, Dict
from .names import Names

# Imports of base Archipelago modules must be absolute.
from worlds.AutoWorld import World

# Imports of your world's files must be relative.
from . import items, locations, regions, rules, web_world
from . import options as skmos_options

class ShamanKingMasterOfSpiritsWorld(World):
    game = Names.Game_Name

    options_dataclass = skmos_options.ShamanKingMasterOfSpiritsOptions
    options: skmos_options.ShamanKingMasterOfSpiritsOptions

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    origin_region_name = Names.Map
    def create_item(self, name: str) -> items.SkmosItem:
        return items.create_item_with_correct_classification(self, name)

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)
        
    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        return self.options.as_dict(
            "group_utility_spirits"
        )