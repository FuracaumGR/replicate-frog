import os
import re
import csv
import html
import time
import requests
import itertools
import replicate

private_mode = os.environ.get("private", "false").lower() == "true"
if private_mode:
    link_dpaste = os.environ.get("input_dpaste", "").strip().rstrip("/")
    if not link_dpaste.endswith("/raw"):
        link_dpaste =+ "/raw"

    response = requests.get(link_dpaste)
    response.raise_for_status()
    unchanged_text = response.text

    lines = [line for line in unchanged_text.strip().splitlines() if line.strip()]
    first_elm_list = lines.pop(0) if lines else ""
    second_elm_list = lines.pop(0) if lines else ""
    
else:
    first_elm_list = os.environ.get("input_elm1", "")
    second_elm_list = os.environ.get("input_elm2", "")
    
list1 = [item.strip() for item in first_elm_list.split("=") if item.strip()]
list2 = [item.strip() for item in second_elm_list.split("=") if item.strip()]

combined_list = []
for text_elm1, text_elm2 in itertools.product(list1, list2):
    true_first, true_second = sorted([text_elm1, text_elm2], key=str.lower)
    formated_sims_csv = f"{true_first} + {true_second} ="
    formated_sims_replicate = f"Water + Fire = Steam\nEarth + Water = Plant\nHuman + Robe = Judge\n Cow + Fire = Steak\nKing + Ocean = Poseidon\n{formated_sims_csv}"
    combined_list.append((formated_sims_replicate, formated_sims_csv))

total_items = len(combined_list)
interval = 10.5

with open("simulation-results.csv", mode="w", newline="", encoding="utf-8-sig") as csv_file:
    writer = csv.writer(csv_file, delimiter=";")
    writer.writerow(["Input", "Output"])
    for index, (present_replicate_sim, present_csv) in enumerate(combined_list, start=1):
        reqs_start = time.time()
        print(f"[{index}/{total_items}] Sending: {present_csv}")
        try:
            exit = replicate.run(
                "meta/llama-2-70b",
                input={
                    "prompt": present_replicate_sim,
                    "max_new_tokens": 20,
                    "temperature": 0
                }
            )
            full_response = "".join(exit).strip()
            writer.writerow([present_csv, full_response])
        except Exception as error:
            print(f"An error occurred at item {index}: {error}")
            writer.writerow([present_csv, f"Error: {error}"])

        if index < total_items:
            total_time = time.time() - reqs_start
            waiting_time = max(0.0, interval - total_time)
            time.sleep(waiting_time)
            
print("Success! Get the file with the simulations at Results.")
