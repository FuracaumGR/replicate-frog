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
for text_elm1, text_elm2 in itertools.product(list1, list2):
    formated_sims = f"{text_elm1} + {text_elm2} ="
    combined_list.append(formated_sims)

print(f"Total of Combinations: {len(combined_list)}")
for item in combined_list:
    print(" ->", item)
for final_text in combined_list:
    print(f"Filling the website with: {final_text}")
    
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    try:
        page.goto("https://replicate.com/meta/llama-2-70b")
        page.fill("prompt", str(final_text))
        page.keyboard.press("Enter")
        page.wait_for_timeout(10000)
    except Exception as erro:
        print("Erro:", erro)
        page.screenshot(path="erro_tela.png")
        raise erro
    finally:
        browser.close()
