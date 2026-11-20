import os
import csv
import io
import itertools
from playwright.sync_api import sync_playwright

first_elm_list = os.environ.get("input_elm1", "")
second_elm_list = os.environ.get("input_elm2", "")
list1 = [item.strip() for item in first_elm_list.split("=") if item.strip()]
list2 = [item.strip() for item in second_elm_list.split("=") if item.strip()]

combined_list = []
for text1, text2 in itertools.product(list1, list2):
    formated_sims = f"{text_elm1} + {text_elm2} ="
    combined_list.append(formated_sims)

print(f"Total of Combinations: {len(combined_list)}")
for item in combined_list:
    print(" ->", item)
