
import pandas as pd
import json   #JSON output file generate karne ke liye.

def save_results(results, output_path):

    df = pd.DataFrame(results)

    df.to_csv(output_path, index=False)

    json_path = output_path.replace(".csv", ".json")

    with open(json_path, "w") as f: #JSON file write mode me open karuga.
        json.dump(results, f, indent=4)

        # indent=4 Meaning:-Pretty formatted JSON.
