import os
import csv
import io
import itertools
import replicate

first_elm_list = os.environ.get("input_elm1", "")
second_elm_list = os.environ.get("input_elm2", "")
list1 = [item.strip() for item in first_elm_list.split("=") if item.strip()]
list2 = [item.strip() for item in second_elm_list.split("=") if item.strip()]

combined_list = []
for text_elm1, text_elm2 in itertools.product(list1, list2):
    formated_sims = f"{text_elm1} + {text_elm2} ="
    combined_list.append(formated_sims)

with open("simulation-results.csv", mode="w", newline="", encoding="utf-8-sig") as csv_file:
    writer = csv.writer(csv_file, delimiter=";")
    writer.writerow(["Input", "Output"])
    for index, present_sim in enumerate(combined_list, start=1):
        print(f"[{index}/{len(combined_list)}] Sending: {present_sim}")
        try:
            exit = replicate.run(
                "meta/llama-2-70b",
                input={
                    "prompt": present_prompt,
                    "max_new_tokens": 20,
                    "temperature": 0
                }
            )
            full_response = "".join(exit).strip()
            writer.writerow([present_prompt, full_response])
        except Exception as error:
            print(f"An error occurred at item {index}: {error}")
            writer.writerow([present_prompt, f"Error: {error}"])
            
print("Success! Here's the file with the result of the simulations.")
