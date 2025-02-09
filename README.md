
# **AUTOMATED REPORT GENERATION (PDF)**  

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: JERRY PRANEETH 

*INTERN ID*: CT6WPYS  

*DOMAIN*: PYTHON PROGRAMMING 

*DURATION*: 6 WEEKS  

*MENTOR*: NEELA SANTOSH  

---

## **📄 Project Overview**  
This Python script generates a **Sales Analysis Report** in PDF format using the `fpdf` library. The report provides key sales metrics, sales breakdowns by **product and region**, and an automated summary of the latest sales data.  

---

## **🚀 Features**  
✅ Generates a **professional** Sales Report in **PDF format**.  
✅ Computes **Total Sales, Average Sales, and Top Product**.  
✅ Breaks down sales data by **Product and Region**.  
✅ Automatically formats and structures the report with **tables**.  
✅ Adds a **company logo, title, and footer** for professionalism.  

---

## **⚙️ Installation**  
Ensure you have **Python 3** installed, then install dependencies:  
```bash
pip install fpdf pandas
```

---

## **📂 Project Structure**  
```
📁 Sales_Report_Generator/
│── 📄 main.py   # Main script to generate PDF
│── 📄 data.csv    # Sales data file (Required)
│── 📄 report.pdf  # Generated PDF Report
│── 🖼️ logo.png    # Company logo (Optional)
```

---

## **📝 Usage**  
### **Prepare the Data File**  
Ensure `data.csv` contains the following columns:  
- **Product** (string)  
- **Region** (string)  
- **Sales** (numeric)  

### **Run the Script**  
```bash
python script.py
```
The report will be generated as **`report.pdf`**.

---

## **📊 Data Processing**  
🔹 Reads sales data from **data.csv**.  
🔹 Computes **Total Sales, Average Sales, and Records Count**.  
🔹 Groups data by **Product and Region**.  
🔹 Identifies the **Top-Performing Product**.  

---

## **📄 PDF Report Structure**  
📌 **Title & Logo**  
📌 **Key Sales Metrics**  
📌 **Regional Sales Table**  
📌 **Product Sales Table**  
📌 **Summary Note**  

---

## **🔧 Customization**  
🛠 Modify **header()** to change the **title and logo**.  
🛠 Adjust **footer()** to edit **page numbering**.  
🛠 Modify **table settings** for **custom formatting**.  

---

## **Output**  


![Image](https://github.com/user-attachments/assets/0115ee47-da2f-42df-b5f0-c9d11c8a5315)

---

## **💡 Notes**  
⚠️ Ensure **data.csv** exists with correct column names.  
⚠️ If `logo.png` is missing, remove `self.image()` in `header()`.  



