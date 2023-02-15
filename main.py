#!/usr/bin/env python3
import random

# Data
overworld_areas = [
    "Kokiri Forest",
    "Lost Woods",
    "Sacred Forest Meadow",
    "Hyrule Field",
    "Lon-Lon Ranch",
    "Zora's River",
    "Zora's Domain",
    "Zora's Fountain",
    "Kakariko Village",
    "Graveyard",
    "Dampé's Grave",
    "Royal Family Tomb",
    "Castle Town",
    "Hyrule Castle",
    "Courtyard (Guards)",
    "Courtyard (Zelda)",
    "Outside Ganon's Castle",
    "Ganon's Tower",
    "Ganon's Tower Collapse Exterior",
    "Ganon's Tower Collapse Interior",
    "Ganon's Castle Collapse",
    "Lake Hylia",
    "Gerudo Valley",
    "Gerudo Fortress",
    "Haunted Wasteland",
    "Desert Colossus",
    "Death Mountain Trail",
    "Death Mountain Crater",
    "Goron City",
]

dungeon_areas = [
    "Inside the Deku Tree",
    "Dodongo's Cavern",
    "Jabu-Jabu's Belly",
    "Forest Temple",
    "Fire Temple",
    "Water Temple",
    "Shadow Temple",
    "Spirit Temple",
    "Gerudo Training Grounds",
    "Ice Cavern",
    "Bottom of the Well",
    "Ganon's Castle",
]

areas: list[str] = []

def main():
    include_overworld = True
    include_dungeons = False
    seed_count = 100000
    results: list[str] = []

    if include_overworld:
        areas.extend(overworld_areas)

    if include_dungeons:
        areas.extend(dungeon_areas)

    if len(areas) > 0 and seed_count > 0:
        for _ in range(seed_count):
            results.append(random.choice(areas))

    print(f"Result: {max(set(results), key=results.count)}")


if __name__ == "__main__":
    main()
