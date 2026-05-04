# FacturIA 🧾🤖
### Automated Invoice Data Extraction and Analysis

> Extract, structure, and analyze invoice data from PDFs using AI —
> turning unstructured documents into business-ready insights.

---

## 📌 Overview

FacturIA automates the extraction of key information from PDF invoices
using OpenAI's GPT-4o-mini model. The system processes invoices,
structures the data, stores it in a SQLite database, and visualizes
it through a Power BI dashboard — covering the full data pipeline
from raw document to actionable insight.

Built as part of a data analyst portfolio to demonstrate real-world
skills in data extraction, AI integration, Python processing, and
business intelligence reporting.

---

## ✨ Features

- 📄 **PDF Text Extraction** — Processes invoice files using PyMuPDF
- 🤖 **AI-Powered Structuring** — GPT-4o-mini parses and standardizes invoice data into CSV format
- 🔁 **Duplicate Prevention** — Tracks previously processed files to avoid redundant entries
- 🗄️ **Data Storage** — Persists structured data in a SQLite database
- 🧹 **Data Cleaning** — Handles data types, numeric conversions, and deduplication
- 📊 **Power BI Dashboard** — Ready-to-use dashboard for visualization and business reporting

**Extracted fields:**
`Invoice Date` · `Supplier Name` · `Concept` · `Amount` · `Currency`

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.8+ |
| AI Model | OpenAI GPT-4o-mini |
| Data Processing | Pandas · SQLAlchemy |
| PDF Extraction | PyMuPDF (Fitz) |
| Database | SQLite |
| Visualization | Power BI |
| Environment | Python-dotenv |

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/gfranco7/facturia.git
cd facturia
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a `.env` file in the root directory:
```
OPENAI_API_KEY=your_openai_api_key_here
```

### 5. Run the project
Place your PDF invoices in the `facturas/` directory and run:
```bash
python main.py
```

---

## 📂 Project Structure

```
facturia/
├── main.py           # Main processing script
├── funciones.py      # PDF extraction and structuring helpers
├── prompt.py         # AI prompt for consistent data extraction
├── requirements.txt  # Dependencies
├── facturas/         # Input PDF invoices
├── PowerBI/          # Power BI dashboard (.pbix)
└── facturas.db       # Generated SQLite database
```

---

## 🗃️ Database Schema

Table: `facturas`

| Field | Type | Description |
|---|---|---|
| `fecha_factura` | string | Invoice date (dd/mm/yyyy) |
| `proveedor` | string | Supplier name |
| `concepto` | string | Description |
| `importe` | float | Amount |
| `moneda` | string | Currency |
| `archivo` | string | Source file path |

---

## 🔮 Future Enhancements

- 🌐 Web interface for invoice uploading
- 🌍 Extended language and format support
- 🔗 Integration with additional BI tools
- ⚡ Batch processing optimizations

---

## 👤 Author

**Gean Franco Jacome**
Data Analyst & Full-Stack Developer

<a href="https://www.linkedin.com/in/geanfrancojacome/" target="_blank">
<img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" height="20" width="25" />
</a>
📧 gfrancojacome710@gmail.com

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.
