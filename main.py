from fpdf import FPDF, XPos, YPos
import pandas as pd

class PDF(FPDF):
    def header(self):
       
        self.image('logo.png', 10, 8, 20)  
        self.set_font('helvetica', 'B', 20)
        self.cell(80)
        self.cell(30, 10, 'Sales Analysis Report', new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
        self.ln(20)

    def footer(self):
        self.set_y(-15)
        self.set_font('helvetica', 'I', 10)
        self.cell(0, 10, f'page{self.page_no()}/{{nb}}', align='C')


df = pd.read_csv("data.csv")

total_sales = df["Sales"].sum()
average_sales = df["Sales"].mean()
total_records = len(df)

sales_by_product = df.groupby("Product")["Sales"].sum().to_dict()

#break down for sales_by_product

#grouped_data_product = df.groupby("Product")   # Step 1: Group by Product
#sales_column_product = grouped_data_product["Sales"]   # Step 2: Select Sales column
#sales_sum_product = sales_column_product.sum()         # Step 3: Sum sales per product
#sales_by_product = sales_sum_product.to_dict()         # Step 4: {'Jeans': 489950.19, 'Sarres': 504432.0, 'Shirts': 450317.07, 'Skirts': 497704.76, 'TShirts': 555438.68}

top_product = max(sales_by_product, key=sales_by_product.get)


sales_by_region = df.groupby("Region")["Sales"].sum().to_dict()

total_sales_fmt = round(total_sales)
average_sales_fmt = round(average_sales)
top_product_sales_fmt = round(sales_by_product[top_product])

pdf = PDF('P', 'mm', 'Letter')
pdf.add_page()
pdf.set_font("Times", size=16)


pdf.set_font('helvetica', 'B', 14)
pdf.cell(0, 10, "Key Metrics", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='L')
pdf.set_font("Times", size=16)

metrics_data = [
    ("Total Sales", f"${total_sales_fmt}"),
    ("Average Sales", f"${average_sales_fmt}"),
    ("Top Product", f"{top_product} (${top_product_sales_fmt})"),
    ("Number of Sales", str(total_records))
]

with pdf.table(align="LEFT", padding=1, col_widths=(50,100)) as table:
    for data_row in metrics_data:
        row = table.row()
        for datum in data_row:
            row.cell(datum)

pdf.ln(10)

#sub-header for Regional Sales table
pdf.set_font('helvetica', 'B', 14)
pdf.cell(0, 10, "Regional Sales", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='L')
pdf.set_font("Times", size=16)

region_data = [("Region", "Sales")]
for region, sales in sales_by_region.items():
    region_data.append((region, f"${sales}"))

with pdf.table() as table:
    for data_row in region_data:
        row = table.row()
        for datum in data_row:
            row.cell(datum)

pdf.ln(10)

# sub-header for Product Sales table
pdf.set_font('helvetica', 'B', 14)
pdf.cell(0, 10, "Product Sales", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='L')
pdf.set_font("Times", size=16)

products_data = [("Products", "Sales")]
for products, sales in sales_by_product.items():
    products_data.append((products, f"${sales}"))

with pdf.table() as table:
    for data_row in products_data:  
        row = table.row()
        for datum in data_row:
            row.cell(datum)

pdf.ln(15)
pdf.set_font('helvetica', 'B', 12)  
pdf.multi_cell(0, 8, "This report was generated automatically based on the latest sales data.\nFor any questions, please contact the analytics team.", align='L')
pdf.set_font("Times", size=16)


    
pdf.output("report.pdf")