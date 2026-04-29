# FacturIA: Automated Invoice Data Extraction and Analysis

## Overview

FacturIA is a data analysis project that automates the extraction of key information from PDF invoices using Artificial Intelligence. The system processes invoices, structures the extracted data, and stores it in a SQLite database for further analysis. This project demonstrates skills in data extraction, AI integration (OpenAI API), data processing with Python, and data visualization using PowerBI.

As part of a data analyst portfolio, this tool showcases the ability to handle unstructured data from real-world documents, transform it into structured datasets, and enable business insights through automated workflows.

## Features

- **PDF Text Extraction**: Extracts text from PDF invoices using PyMuPDF.
- **AI-Powered Data Structuring**: Utilizes OpenAI's GPT-4o-mini model to parse and structure invoice data into a standardized CSV format.
- **Duplicate Prevention**: Checks for previously processed files to avoid redundant entries.
- **Data Storage**: Saves extracted data to a SQLite database for persistence and querying.
- **Data Cleaning**: Handles data types, numeric conversions, and removes duplicates.
- **Visualization Ready**: Integrates with PowerBI for dashboard creation and analysis.

Extracted fields include:
- Invoice date (formatted as dd/mm/yyyy)
- Supplier name
- Concept/description
- Amount (with proper decimal formatting)
- Currency (euros, dollars, or others)

## Prerequisites

- Python 3.8 or higher
- OpenAI API key (required for data structuring)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/facturia.git
   cd facturia
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file in the root directory
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_openai_api_key_here
     ```

## Usage

1. Place your PDF invoices in the `facturas/` directory. Organize them into subfolders if desired (e.g., `facturas/01_January/invoice.pdf`).

2. Run the main script:
   ```
   python main.py
   ```

3. The script will process new PDFs, extract data, and append to the `facturas.db` database.

4. For visualization, open the PowerBI dashboard file (`PowerBI/Dashboard_FacturIA.pbix`) and connect to the `facturas.db` SQLite database.

## Database Schema

The data is stored in a SQLite database (`facturas.db`) with a table named `facturas`. The schema includes:
- `fecha_factura`: Invoice date (string)
- `proveedor`: Supplier name (string)
- `concepto`: Description (string)
- `importe`: Amount (float)
- `moneda`: Currency (string)
- `archivo`: File path for reference (string)

## Technologies Used

- **Python**: Core programming language
- **OpenAI API**: For AI-powered text structuring
- **Pandas**: Data manipulation and DataFrame handling
- **SQLAlchemy**: Database interactions
- **PyMuPDF (Fitz)**: PDF text extraction
- **Python-dotenv**: Environment variable management
- **PowerBI**: Data visualization and dashboard creation

## Project Structure

- `main.py`: Main script for processing invoices
- `funciones.py`: Helper functions for PDF extraction and data structuring
- `prompt.py`: AI prompt for consistent data extraction
- `requirements.txt`: Python dependencies
- `facturas/`: Directory for PDF invoices
- `PowerBI/`: PowerBI dashboard files
- `facturas.db`: SQLite database (generated)

## Limitations

- Requires valid OpenAI API key
- Currently supports Spanish/English invoice formats based on the prompt
- PDF quality may affect extraction accuracy
- Designed for Colombian Peso (COP) context but adaptable to other currencies

## Future Enhancements

- Support for additional languages and formats
- Web interface for uploading invoices
- Integration with other visualization tools
- Batch processing optimizations
- Advanced error handling and logging

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Gean Franco Jacome - Data Analyst Portfolio Project

For questions or collaborations, feel free to reach out.</content>
<parameter name="filePath">README.md
