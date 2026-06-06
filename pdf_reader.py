import pdfplumber  #pdf me se text nikalone ke liye jo 
import warnings  # warinigs message ko manage karne ke liye
import logging   # program me kya chal ha usko record rakhne ke liye
logging.getLogger("pdfminer").setLevel(logging.ERROR)  #Error bas iss line me likhai ye baki chup rhe

warnings.filterwarnings("ignore")

def extract_text(pdf_path):
    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            try:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + " "
            except:
                continue   # skip broken pages

    return text.strip()