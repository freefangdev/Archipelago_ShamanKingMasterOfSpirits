from dataclasses import dataclass
from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle

#Possible future options:
#- Remove keys, open all doors
#- Skip chests
#- Lower mandatory spirit costs to starting total
#- Save on level completion
#- Ghost spawning enemies get blue outline
#- All bosses required for final boss/gather everyone at the inn (all inn/Inn sanity)
#- Gotta cath em all goal 
#- Start spirit slot count
#- Gather all spirits for the cannon in one item
#- Disable splash art when using spirits
#- Allow cheat commands
#- Monster progression trap
#- Inventory weight expansion 5 - 10 (original) - 15 - 20 - 30?
#- Unlock item slots
#- Convert excessive items for full price
#- Disable Amidamaru rescue from pits, straight game over instead
    #Option 1: Usual behavior, get rescued
    #Option 2: Only rescue when you have Amidamaru
    #Option 3: Item
#- Add weaponless start, requires fixing behavior when weapon slot is FF
#- Backdash as item
#- Duck as item
#- Progressive sword

class DisableSplashArtWhenUsingSpirits(Toggle):
    """
    Disable elaborate activation animations when using spirits
    """

    display_name = "Disable elaborate activation animations when using spirits"

class EarlyTotemSpiritLocations(Toggle):
    """
    Enable Totem Spirit locations before Silva/Silver boss, 
    preventing excessive backtracking
    """

    display_name = "Enable Totem Spirit locations before Silva/Silver boss"

class GroupUtilitySpirits(Toggle):
    """
    Not implemented yet!
    Groups Tokageroh, Corey, Mic, and Lee Pai-Long together, 
    use any of these spirits plus a direction on the dpad to select which is used: 
    Neutral + activate = Tokageroh
    Up + activate = Corey
    Left or right + activate = Mic
    Down + activate = Lee Pai-Long
    
    And separately groups Cloe, Totem Attack and Grand Tao Dragon.
    Neutral + activate = Totem Attack
    Up, left or right + activate = Cloe
    Down + activate = Grand Tao Dragon
    """

    display_name = "Group Utility Spirits"

class TrapChance(Range):
    """
    Not implemented yet!
    Percentage chance that any given consumable item will be replaced by a Trap.
    """

    display_name = "Trap Chance"

    range_start = 0
    range_end = 100
    default = 0

@dataclass
class ShamanKingMasterOfSpiritsOptions(PerGameCommonOptions):
    early_totem_spirit_locations: EarlyTotemSpiritLocations
    group_utility_spirits: GroupUtilitySpirits
    trap_chance: TrapChance
    disable_splash_art_when_using_spirits: DisableSplashArtWhenUsingSpirits


# If we want to group our options by similar type, we can do so as well. This looks nice on the website.
option_groups = [
    OptionGroup(
        "Quality of life options",
        [
            EarlyTotemSpiritLocations,
            GroupUtilitySpirits,
            DisableSplashArtWhenUsingSpirits,
        ],
    ),
    OptionGroup(
        "Randomization Options",
        [
            TrapChance
        ],
    ),
]

option_presets = {
    "default": {
        "early_totem_spirit_locations": True,
        "group_utility_spirits": True,
        "disable_splash_art_when_using_spirits": True,
        "trap_chance": 0,
    },
    "purist": {
        "early_totem_spirit_locations": False,
        "group_utility_spirits": False,
        "disable_splash_art_when_using_spirits": False,
        "trap_chance": 0,
    },
}
