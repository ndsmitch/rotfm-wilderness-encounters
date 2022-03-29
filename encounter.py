# Page 105 - Random wilderness encounters for rime of the frostmaiden

from dice import roll
def rolld(_int):
    """rolld('6') -> int = d6 roll"""
    return int(roll(f"d{_int}"))

def get_awakened_beast():
    BEASTS = {
        1: "polar bear",
        2: "arctic fox",
        3: "snowshoe hare",
        4: "snowy owl",
        5: "elk with glowing antlers (10-ft dim light)",
        6: "wooly rhinocerous",
        7: "saber-toothed tiger",
        8: "wolf",
    }
    return f"awakened {BEASTS[rolld(8)]}"

def get_frost_druid():
    FRIEND = {
        1: "pine tree",
        2: "mountain goat",
        3: "elk with glowing antlers (10-ft dim light)",
        4: "walrus",
    }
    return f"frost druid with an awakened {FRIEND[rolld(4)]}"

def get_goliaths():
    TRIBE = {
        1: "Skytower Akannathi",
        2: "Wyrmdon Thuunlakalaga",
    }
    return f"4 {TRIBE[rolld(2)]} goliaths"

def get_herd():
    HERD = {
        1: f"{int(roll('4d6'))} elk",
        2: f"{int(roll('4d6'))} elk",
        3: f"{int(roll('3d6'))} mammoths",
        4: f"{int(roll('3d6'))} mammoths",
        5: f"{int(roll('5d6'))} reindeer [one in six glow]",
        6: f"{int(roll('5d6'))} reindeer [one in six glow]",
    }
    SCHOOL = {
        1: f"{int(roll('3d6'))} killer whales",
        2: f"{int(roll('6d6'))} seals",
        3: f"{int(roll('6d6'))} seals",
        4: f"{int(roll('6d6'))} seals",
        5: f"{int(roll('6d6'))} walruses",
        6: f"{int(roll('6d6'))} walruses",
    }
    return f"{HERD[rolld(6)]} [{SCHOOL[rolld(6)]} if underwater]"

def get_humans():
    TRIBE = {
        1: "Bear tribe rehged nomads [indifferent]",
        2: "Bear tribe rehged nomads [indifferent]",
        3: "Bear tribe rehged nomads [indifferent]",
        4: "Bear tribe rehged nomads [indifferent]",
        5: "Bear tribe rehged nomads [indifferent]",
        6: "Elk tribe rehged nomads [indifferent]",
        7: "Elk tribe rehged nomads [indifferent]",
        8: "Elk tribe rehged nomads [indifferent]",
        9: "Elk tribe rehged nomads [indifferent]",
        10: "Elk tribe rehged nomads [indifferent]",
        11: "Elk tribe rehged nomads [indifferent]",
        12: "Elk tribe rehged nomads [indifferent]",
        13: "Elk tribe rehged nomads [indifferent]",
        14: "Tiger tribe rehged nomads [hostile]",
        15: "Tiger tribe rehged nomads [hostile]",
        16: "Tiger tribe rehged nomads [hostile]",
        17: "Tiger tribe rehged nomads [hostile]",
        18: "Wolf tribe rehged nomads [hostile]",
        19: "Wolf tribe rehged nomads [hostile]",
        20: "Wolf tribe rehged nomads [hostile]",
    }
    return f"{rolld(6)+4} {TRIBE[rolld(20)]}"


def get_yeti():
    YETI = {
        1: f"{rolld(4)} yeti",
        2: f"{rolld(4)} yeti",
        3: f"{rolld(4)} yeti",
        4: "abominable yeti",
        5: "abominable yeti",
        6: "yeti tyke",
    }
    return YETI[rolld(6)]


def get_encounter():
    encounter_roll = rolld(20)
    blizzard = rolld(20) >= encounter_roll

    ENCOUNTERS = {
        1: get_yeti(),
        2: get_goliaths(),
        3: f"{rolld(4)} crag cats",
        4: f"coldlight walker{' [+whisper]' if blizzard else ''}",
        5: "ice troll",
        6: get_frost_druid(),
        7: f"{rolld(4)+2} chardalyn berserkers [+ring]",
        8: "frost giant riding a mammoth",
        9: f"{rolld(6)+2} Battlehammer dwarves",
        10: "Arveiturace",
        11: "snowy owlbear",
        12: f"{rolld(4)+3} gnolls",
        13: "Orcs of the Many-Arrows Tribe (war chief, eye of gruumsh, half-ogre, 6 orcs) ",
        14: "4 goliath warriors",
        15: f"{'insane ' if blizzard else ''}chwinga",
        16: get_awakened_beast(),
        17: f"{int(roll('2d4'))} icewind kobolds",
        18: get_humans(), # TODO make fn
        19: get_herd(),
        20: "perytons",
    }

    result = ENCOUNTERS[rolld(20)]
    if blizzard:
        result = f"{result} in a blizzard"

    return result

def get_full_encounters():
    ENCOUNTER_TIMES = {
        1: f"at morning",
        2: f"at twilight",
        3: f"at night",
        4: f"at aurora",
    }

    REROLL = (
        f"{get_encounter()} {ENCOUNTER_TIMES[rolld(4)]}"
        f" AND {get_encounter()} {ENCOUNTER_TIMES[rolld(4)]}"
    )
    
    ENCOUNTERS = {
        key: f"{get_encounter()} {time}" 
        for key, time in ENCOUNTER_TIMES.items()
    }

    NUMBER_OF_ENCOUNTERS = {
        **ENCOUNTERS,
        5: REROLL,
        6: REROLL,
        7: "No encounter",
        8: "No encounter",
    }

    return NUMBER_OF_ENCOUNTERS[rolld(8)]

print(get_full_encounters())
# print(get_awakened_beast())
