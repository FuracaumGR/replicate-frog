import os
import csv
import io
from playwright.sync_api import sync_playwright

first_elm_list = os.environ.get("input_elm1", "")
second_elm_list = os.environ.get("input_elm2", "")
virtual_file1 = io.StringIO(first_elm_list.strip())
virtual_file2 = io.StringIO(second_elm_list.strip())
read_csv1 = csv.reader(virtual_file1, delimeter='=')
read_csv2 = csv.reader(virtual_file2, delimeter='=')
