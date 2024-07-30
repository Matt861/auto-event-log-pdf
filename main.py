import json
import os
from pathlib import Path
from fillpdf import fillpdfs
from datetime import date

p = Path(__file__).resolve()


# Function to fill in the form fields in the PDF
def fill_pdf_form(input_pdf, pdf_data, output_pdf):
    # Get the existing form fields in the PDF
    form_fields = fillpdfs.get_form_fields(input_pdf)
    print("Form fields before updating:", form_fields)

    # Update the form fields with data from the JSON file
    for key in pdf_data:
        if key in form_fields:
            form_fields[key] = pdf_data[key]
            if "Date" in key:
                form_fields[key] = date.today()
        else:
            print(f"Warning: Key '{key}' not found in form fields")

    print("Form fields after updating:", form_fields)

    # Fill the PDF with the updated form fields
    fillpdfs.write_fillable_pdf(input_pdf, output_pdf, form_fields)


# Read data from JSON file
with open('input\\pdf_mapping_data.json', 'r') as f:
    data = json.load(f)

output_pdf_file_name = 'Orange-0.6.0-Infra-F-35 Software IS Event Log_Rev2024-04-01.pdf'
output_pdf_file_path = os.path.join('output', output_pdf_file_name)
input_pdf_file_name = 'F-35 Software IS Event Log_Rev2024-04-01_modified.pdf'
input_pdf_file_path = os.path.join('input', input_pdf_file_name)
source = Path(input_pdf_file_path)
destination = Path(output_pdf_file_path)
destination.write_bytes(source.read_bytes())

# Check the content of the data
print("Data from JSON:", data)

# Fill in the form fields in the PDF
fill_pdf_form(input_pdf_file_path, data, output_pdf_file_path)
