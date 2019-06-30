#!/usr/bin/env python

"""
@author: jakub
"""
from src import Creator

wood = [
    "T6_PLANKS",
    "T7_PLANKS",
    "T6_PLANKS_LEVEL1@1",
    "T7_PLANKS_LEVEL1@1",
    "T6_PLANKS_LEVEL2@2",
    "T7_PLANKS_LEVEL2@2",
    "T6_WOOD",
    "T7_WOOD",
    "T6_WOOD_LEVEL1@1",
    "T7_WOOD_LEVEL1@1",
    "T6_WOOD_LEVEL2@2",
    "T7_WOOD_LEVEL2@2",
]

hides = [
    "T6_HIDE",
    "T7_HIDE",
    "T6_HIDE_LEVEL1@1",
    "T7_HIDE_LEVEL1@1",
    "T6_HIDE_LEVEL2@2",
    "T7_HIDE_LEVEL2@2",
    "T6_LEATHER",
    "T5_LEATHER",
    "T5_LEATHER_LEVEL1@1",
    "T6_LEATHER_LEVEL1@1",
    "T5_LEATHER_LEVEL2@2",
    "T6_LEATHER_LEVEL2@2",
]

animals = [
    "T6_FARM_HORSE_BABY",
    "T4_FARM_HORSE_BABY",
    "T5_FARM_HORSE_BABY",
    "T3_FARM_HORSE_BABY",
    "T6_FARM_HORSE_GROWN",
    "T4_FARM_HORSE_GROWN",
    "T5_FARM_HORSE_GROWN",
    "T3_FARM_HORSE_GROWN",
    "T6_FARM_DIREWOLF_BABY",
    "T6_FARM_DIREWOLF_GROWN",
]

stone = [
    "T6_ROCK",
    "T7_ROCK",
    "T5_ROCK",
    "T6_STONEBLOCK",
    "T7_STONEBLOCK",
    "T5_STONEBLOCK",
]

consumables = [
    "T5_MEAL_OMELETTE",
    "T7_MEAL_OMELETTE",
    "T6_MEAL_STEW",
    "T4_MEAL_STEW",
    "T7_MEAL_PIE",
    "T5_MEAL_PIE",
    "T6_MEAL_SANDWICH",
    "T4_MEAL_SANDWICH",
]

crops = [
    "T1_CARROT",
    "T1_FARM_CARROT_SEED",
    "T7_FARM_CORN_SEED",
    "T6_FARM_POTATO_SEED",
    "T6_POTATO",
    "T7_CORN",
    "T8_PUMPKIN",
    "T8_FARM_PUMPKIN_SEED",
]


Creator(
    subset_name="wood", item_of_interest=wood
).update_frame()
Creator(
    subset_name="hides", item_of_interest=hides
).update_frame()
Creator(
    subset_name="animals", item_of_interest=animals
).update_frame()
Creator(
    subset_name="stone", item_of_interest=stone
).update_frame()
Creator(
    subset_name="consumables", item_of_interest=consumables
).update_frame()
Creator(
    subset_name="crops", item_of_interest=crops
).update_frame()
