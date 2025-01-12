import sys
import json
import numpy as np
from datasets import Dataset


from .dataset import APPSDataset


def main():
    """Entry point for the application script"""
    print("Call your main application code here")

    apps = APPSDataset()
    ds = apps.dataset()

    # To handle large numbers
    sys.set_int_max_str_digits(0)

    some_stats(ds)


def some_stats(ds: Dataset):
    # for split in ["train", "test"]:
    split = "train"

    # Groups
    # difficulty
    # platform

    # Properties
    # num test
    # num answers
    # answer length

    properties = [
        "num_answers",
        "num_tests",
        "mean_answer_lines",
        "std_answer_lines",
    ][:]

    df = ds.to_pandas()

    df["solutions"] = df["solutions"].apply(
        lambda x: json.loads(x) if x else [],
    )
    df["num_answers"] = df["solutions"].apply(
        len,
    )
    df["input_output"] = df["input_output"].apply(
        lambda x: json.loads(x) if x else {"inputs": [], "outputs": []},
    )
    df["num_tests"] = df["input_output"].apply(
        lambda x: len(x["inputs"]),
    )

    df["mean_answer_lines"] = df["solutions"].apply(
        lambda x: np.mean([len(soln.split("\n")) for soln in x]),
    )
    df["std_answer_lines"] = df["solutions"].apply(
        lambda x: np.std([len(soln.split("\n")) for soln in x]),
    )

    platforms = df["url"].str.split(".")
    platforms0 = platforms.str[0].str.split("/").str[-1]
    platforms0[platforms0.isin(["open", "www"])] = platforms[
        platforms0.isin(["open", "www"])
    ].str[1]
    df["platform"] = platforms0

    all_dfs = [df]
    print("#" * 30)
    print(f"Printing stats for {split}")

    agg = df[properties].agg(["mean", "std", "median", "min", "max"])
    print("-" * 30)
    print("Entire Table")
    print(f"Size {len(df)=}")
    print(agg)

    for group_col in ["difficulty", "platform"]:
        agg = df.groupby(group_col)[properties].agg(
            ["mean", "std", "min", "max"],
        )
        agg["size"] = df.groupby(group_col).size()
        print("-" * 30)
        print(f"Grouped by {group_col}")
        print(agg)

    agg = df.groupby(["difficulty", "platform"])[properties].agg(
        ["mean", "std", "min", "max"],
    )
    agg["size"] = df.groupby(["difficulty", "platform"]).size()
    print("-" * 30)
    print("Grouped by difficulty and platform")
    print(agg)
