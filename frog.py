import os
import csv
import io
import itertools
from playwright.sync_api import sync_playwright

first_elm_list = os.environ.get("input_elm1", "")
second_elm_list = os.environ.get("input_elm2", "")
list1 = [line for line in csv.reader(io.StringIO(first_elm_list.strip()), delimeter='=') if line]
list2 = [line for line in csv.reader(io.StringIO(second_elm_list.strip()), delimeter='=') if line]

combined_list = []
for columns1, columns2 in interntools.product(list1, list2):
    text_elm1 = columns1[0].strip()
    text_elm2 = columns2[0].strip()
    formated_sims = f"{text_elm1} + {text_elm2} ="
    combined_list.append(formated_sims)

print(f"Total of Combinations: {len(combined_list)}")
for item in combined_list:
    print(" ->", item)
