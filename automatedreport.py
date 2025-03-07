# -*- coding: utf-8 -*-
"""automatedreport.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JfHSkJMEoXrW8FgsHm_sAAGlSN_XjiWS
"""

!pip install fpdf

import pandas as pd
from fpdf import FPDF

# Load data from a CSV file (replace 'data.csv' with your actual file)
data = pd.read_csv('/content/sample_data/california_housing_test.csv')

# Perform basic analysis
summary = data.describe()

# Generate a PDF report
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", style='B', size=16)
        self.cell(200, 10, "Data Analysis Report", ln=True, align='C')
        self.ln(10)

pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", size=12)

# Add summary statistics to PDF
pdf.cell(200, 10, "Summary Statistics:", ln=True, align='L')
pdf.ln(5)
for column in summary.columns:
    pdf.cell(0, 10, f"{column}: Mean={summary[column]['mean']:.2f}, Min={summary[column]['min']:.2f}, Max={summary[column]['max']:.2f}", ln=True)

# Save PDF
pdf.output("report.pdf")

print("Report generated: report.pdf")

