
import os #Folders/files access karne ke liye.
from pdf_reader import extract_text  #PDF se text nikalega.
from preprocessing import preprocess_text
from classifier import classify_document
from output_writer import save_results   #CSV/JSON save karega.
from logger import log_error   #Errors save karega.
import pandas as pd





INPUT_FOLDER = "input_pdfs"
OUTPUT_FILE = "output/results.csv"

def process_pdfs():
    results = []

    for file_name in os.listdir(INPUT_FOLDER):   #Folder ke sab files read karta hai.

        if not file_name.endswith(".pdf"): # 0nly pdf par deyan dena hai
            continue

        file_path = os.path.join(INPUT_FOLDER, file_name)

        try:
            text = extract_text(file_path)

            if not text.strip():                 #Blank PDF detect karta hai.
                raise ValueError("Empty PDF")

            processed_text = preprocess_text(text)

            category, confidence = classify_document(processed_text)

            results.append({
                "file_name": file_name,
                "category": category,
                "confidence_score": confidence,
                "status": "Success"
            })

        except Exception as e:

            log_error(file_name, str(e))

            results.append({
                "file_name": file_name,
                "category": "Unknown",
                "confidence_score": 0.0,
                "status": f"Error: {str(e)}"
            })

    save_results(results, OUTPUT_FILE)
    df = pd.DataFrame(results)

    print("\n PDF Classification Results:\n")
    print(df)

    print("PDF Classification Completed Successfully")

if __name__ == "__main__":
    process_pdfs()
