import os
import csv
import io
from playwright.sync_api import sync_playwright

first_elements_list = os.environ.get(
