#!/usr/bin/env python

"""
@author: jakub
"""

import requests
import pandas as pd


class Creator:
    def __init__(
        self, subset_name=None, item_of_interest=None, db_csv=None
    ):
        self.subset_name = subset_name
        self.item_of_interest = item_of_interest
        if db_csv not in ('db', 'csv'):
         raise ValueError()
         print("Allowed values are either 'db' or 'csv'")
        self.db_csv = db_csv

    def create_frame(self):
        dataframe = pd.DataFrame(
            columns=[
                "buy_price_max",
                "buy_price_max_date",
                "buy_price_min",
                "buy_price_min_date",
                "city",
                "item_id",
                "quality",
                "sell_price_max",
                "sell_price_max_date",
                "sell_price_min",
                "sell_price_min_date",
            ]
        )

        for j in self.item_of_interest:
            response = requests.get(
                f"https://www.albion-online-data.com/api/v2/stats/prices/{j}"
            ).json()

            pre_df = pd.DataFrame.from_dict(response)
            dataframe = pd.concat(
                [dataframe, pre_df], sort=False
            )
            dataframe.drop(
                [
                    "buy_price_max_date",
                    "buy_price_min_date",
                ],
                axis=1,
                inplace=True,
            )
        if self.db_csv == "csv":
            dataframe.to_csv(
                    f"{self.subset_name}.csv", index=False
            )
        else:
            return dataframe

    def update_csv(self):
        dataframe = pd.read_csv(f"{self.subset_name}.csv")

        for j in self.item_of_interest:
            response = requests.get(
                f"https://www.albion-online-data.com/api/v2/stats/prices/{j}"
            ).json()
            pre_df = pd.DataFrame.from_dict(response)
            pre_df.drop(
                [
                    "buy_price_max_date",
                    "buy_price_min_date",
                ],
                axis=1,
                inplace=True,
            )
            dataframe = pd.concat(
                [dataframe, pre_df], sort=False
            )
            dataframe.drop_duplicates(
                [
                    "city",
                    "item_id",
                    "sell_price_min",
                    "sell_price_min_date",
                ],
                inplace=True,
            )
            dataframe.to_csv(
                        f"{self.subset_name}.csv", index=False
                    )

