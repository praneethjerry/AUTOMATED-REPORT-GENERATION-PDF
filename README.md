# AUTOMATED-REPORT-GENERATION-PDF

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: JERRY PRANEETH

*INTERN ID*: CT6WPYS

*DOMAIN*: PYTHON PROGRAMMING

*DURATION*: 6 WEEEKS

*MENTOR*: NEELA SANTOSH


This Python script generates a Sales Analysis Report in PDF format using the fpdf library. The report provides key sales metrics, sales breakdown by product and region, and an automated summary of the latest sales data.

📌 Features

Generates a professional Sales Report in PDF format.

Computes Total Sales, Average Sales, and Top Product.

Breaks down sales data by Product and Region.

Automatically formats and structures the report with tables.

Adds a company logo, title, and footer for professionalism.

🚀 Installation

Ensure you have Python 3 installed, then install dependencies:

pip install fpdf pandas

📂 Project Structure

📁 Sales_Report_Generator
│── 📄 script.py  # Main script to generate PDF
│── 📄 data.csv   # Sales data file (Required)
│── 📄 report.pdf # Generated PDF Report
│── 🖼️ logo.png   # Company logo (Optional)

📝 Usage

Ensure data.csv contains the required columns:

Product (string)

Region (string)

Sales (numeric)

Run the script:

python script.py

The report will be generated as report.pdf.

📊 Data Processing

Reads sales data from data.csv.

Computes total sales, average sales, and records count.

Groups data by Product and Region.

Identifies top-performing product.

📄 PDF Report Structure

Title & Logo

Key Sales Metrics

Regional Sales Table

Product Sales Table

Summary Note


🔧 Customization

Modify header() to change title and logo.

Adjust footer() to edit page numbering.

Modify table settings for custom formatting.

💡 Notes

Ensure data.csv exists with correct column names.

If logo.png is missing, remove self.image() in header().
