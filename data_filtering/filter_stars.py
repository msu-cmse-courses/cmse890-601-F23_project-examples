#!/usr/bin/env python
# coding: utf-8

import pandas as pd

bakers = pd.read_csv("bakers_raw.csv", index_col="rownames",
                     usecols=["rownames","series","baker","baker_full"])
results = pd.read_csv("results_raw.csv", index_col="rownames")

# In results_raw.csv, bakers are only identified by their first name.
# There may be duplicate first names; e.g., series 1 & 10 have a David.
# Add full competitor data to the results dataframe
old_rows = results.shape[0]
results = pd.merge(results, bakers, on=("series","baker"), how="inner")
assert old_rows == results.shape[0]

# how many times was a contestant the star baker?
star_bakers = results[results["result"] == "STAR BAKER"]
star_baker_results = star_bakers["baker_full"].value_counts().to_frame()

# who were the overall winners?
winners = results["result"] == "WINNER"
winner_names = results[winners]["baker_full"]

# Add column to star baker count marking whether or not the contestant won
star_baker_results["winner"] = star_baker_results.index.isin(winner_names)

star_baker_results.to_csv("star_baker_results.csv")
