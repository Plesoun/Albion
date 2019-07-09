#!/usr/bin/env python

"""
@author: jakub
"""
from src.creator import Creator
from src.database import PostgreSQL
from src.database import Items
import os


tracked_items = [
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
    "T6_ROCK",
    "T7_ROCK",
    "T5_ROCK",
    "T6_STONEBLOCK",
    "T7_STONEBLOCK",
    "T5_STONEBLOCK",
    "T5_MEAL_OMELETTE",
    "T7_MEAL_OMELETTE",
    "T6_MEAL_STEW",
    "T4_MEAL_STEW",
    "T7_MEAL_PIE",
    "T5_MEAL_PIE",
    "T6_MEAL_SANDWICH",
    "T4_MEAL_SANDWICH",
    "T1_CARROT",
    "T1_FARM_CARROT_SEED",
    "T7_FARM_CORN_SEED",
    "T6_FARM_POTATO_SEED",
    "T6_POTATO",
    "T7_CORN",
    "T8_PUMPKIN",
    "T8_FARM_PUMPKIN_SEED",
]

test = Creator(
    subset_name="tracked_items", item_of_interest=tracked_items, db_csv="db",
).create_frame()

PostgreSQL(username=os.environ["DB_USERNAME"], password=os.environ["DB_PASSWORD"], host=os.environ["DB_HOST"],
           schema="albion",).save_data(table_to_save=test, template=Items)
