import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read CSV
df = pd.read_csv("data.csv", engine="python", quotechar='"', skipinitialspace=True)

# Optional: Show original column names for debug
# Clean and normalize column names
df.columns = (
    df.columns
    .str.replace('\xa0', '_', regex=False)        # fix weirexpd spaces
    .str.strip()
    .str.lower()
    .str.replace(' ', '_')
    .str.replace(r'[()]', '', regex=True)         # remove ()
    .str.replace(r'[^\w\s]', '', regex=True)      # remove punctuation like .
)

# Show cleaned column names

# Clean monetary columns
money_cols = ['actual_gross', 'adjusted_gross_in_2022_dollars', 'average_gross']
for col in money_cols:
    df[col] = df[col].str.replace(r"[$,†‡*a-e\[\]]", "", regex=True)
    df[col] = pd.to_numeric(df[col], errors="coerce").astype("Int64")

# Clean peak columns
df["peak"] = df["peak"].str.extract("(\d+)", expand=False)
df["peak"] = pd.to_numeric(df["peak"], errors="coerce").astype("Int64")

df["all_time_peak"] = df["all_time_peak"].str.extract("(\d+)", expand=False)
df["all_time_peak"] = pd.to_numeric(df["all_time_peak"], errors="coerce").astype("Int64")

# Fix types of other fields
df['artist'] = df['artist'].astype("string")
df['tour_title'] = df['tour_title'].astype("string")
df['years'] = df['years'].astype("string")
df['ref'] = df['ref'].str.findall(r'\d+').str.join(',')
df['ref'] = df["ref"].replace("", pd.NA)         # optional: blank to <NA>
df['ref'] = df['ref'].astype("string")           # this now sticks
df['shows'] = df['shows'].astype("Int64")



