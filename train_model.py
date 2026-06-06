
import pandas as pd
import joblib

from sklearn.pipeline import Pipeline  #Multiple ML steps ko ek pipeline me combine karta hai. pichhe padaya tha
from sklearn.feature_extraction.text import TfidfVectorizer   #Text ko numbers me convert karta hai.
from sklearn.naive_bayes import MultinomialNB

data = {
"text": [

    # Invoice
    "invoice payment gst amount total due",
    "tax invoice billing address payment status",
    "invoice number customer amount paid",
    "gst bill subtotal grand total invoice",
    "payment due date invoice amount tax",

    # Bank Statement
    "bank account statement debit credit balance",
    "transaction history withdrawal deposit account",
    "monthly bank statement transaction summary",
    "bank account balance credit debit",
    "statement period opening closing balance",

    # Contract
    "contract agreement terms conditions parties",
    "legal contract signed agreement details",
    "business agreement contract obligations clauses",
    "service contract terms payment agreement",
    "employment contract conditions responsibilities details",

    # Resume
    "python sql machine learning projects experience",
    "resume candidate education technical skills",
    "software engineer experience certifications internships",
    "data analyst skills projects resume profile",
    "candidate profile work experience education",

    # Report
    "business analysis report dashboard summary",
    "monthly performance report analytics insights",
    "sales report business intelligence dashboard",
    "annual report company performance summary",
    "project report analysis recommendations findings",

    # Medical Report
    "patient diagnosis prescription blood test report",
    "medical report doctor treatment prescription",
    "laboratory blood test patient diagnosis",
    "health report medical examination results",
    "patient treatment diagnosis clinical report",

    # Legal Document
    "court affidavit legal notice petition lawyer",
    "legal document court hearing affidavit",
    "petition lawyer case legal notice",
    "judicial affidavit legal case document",
    "court order advocate legal petition",

    # Offer Letter
    "offer letter joining date annual salary",
    "job offer employment salary benefits",
    "offer letter candidate joining details",
    "employment offer company annual package",
    "offer letter hr joining confirmation",

    # Research Paper
    "research methodology abstract conclusion references",
    "deep learning research paper experimental results",
    "scientific paper literature review methodology",
    "machine learning research findings analysis",
    "research publication abstract experimental study"
],

"category": [

    # Invoice
    "Invoice",
    "Invoice",
    "Invoice",
    "Invoice",
    "Invoice",

    # Bank Statement
    "Bank Statement",
    "Bank Statement",
    "Bank Statement",
    "Bank Statement",
    "Bank Statement",

    # Contract
    "Contract",
    "Contract",
    "Contract",
    "Contract",
    "Contract",

    # Resume
    "Resume",
    "Resume",
    "Resume",
    "Resume",
    "Resume",

    # Report
    "Report",
    "Report",
    "Report",
    "Report",
    "Report",

    # Medical Report
    "Medical Report",
    "Medical Report",
    "Medical Report",
    "Medical Report",
    "Medical Report",

    # Legal Document
    "Legal Document",
    "Legal Document",
    "Legal Document",
    "Legal Document",
    "Legal Document",

    # Offer Letter
    "Offer Letter",
    "Offer Letter",
    "Offer Letter",
    "Offer Letter",
    "Offer Letter",

    # Research Paper
    "Research Paper",
    "Research Paper",
    "Research Paper",
    "Research Paper",
    "Research Paper"
]}


df = pd.DataFrame(data)

model = Pipeline([
    ("tfidf", TfidfVectorizer()), # text covert to number
    ("classifier", MultinomialNB()) # navie bayes classifire hai
])

model.fit(df["text"], df["category"])

joblib.dump(model, "models/model.pkl")

print("ML Model Trained Successfully")
