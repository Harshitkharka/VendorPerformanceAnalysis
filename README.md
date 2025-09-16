
***

# Vendor Sales Analysis

Vendor Sales Analysis provides meaningful insights into inventory and sales performance in the retail and wholesale sector. The project identifies underperforming brands, highlights top vendors, examines purchase impacts, and optimizes inventory strategies for increased profitability.

## Project Overview

This repository focuses on:
- **Identifying underperforming brands** that need promotions or price adjustments.
- **Determining top vendors** driving gross profit and sales.
- **Analyzing effects of bulk purchasing** on unit costs.
- **Assessing inventory turnover** to minimize holding costs and boost efficiency.
- **Comparing profitability variance** between high- and low-performing vendors.[2]

## Data Pipeline

- Data is extracted from a PostgreSQL inventory database with Python (`Dataingestion.py`).
- Extracted data are saved as CSV files and ingested into an SQLite database.
- Tables used: `begin_inventory`, `end_inventory`, `purchase_prices`, `purchases`, `sales`, and `vendor_invoice`.[1]

## Analysis

Conducted in a Jupyter notebook (`SalesAnalysis.ipynb`), the data analysis includes:
- Calculating total sales, profit margins, and stock turnover per brand/vendor.
- Identifying key metrics: sales quantity, gross profit, profit margin, and inventory efficiency.
- Applying pandas, numpy, matplotlib, and seaborn for data processing and visualization.[2]

## How to Run

1. **Database Extraction:**
   - Set up Postgres connection in `Dataingestion.py` (update credentials as needed).
   - Run `Dataingestion.py` to extract tables and populate `InventoryData/`.

2. **Data Analysis:**
   - Open `SalesAnalysis.ipynb` in Jupyter.
   - Follow the notebook for analysis and visualization.

## Requirements

- Python 3.x
- pandas, numpy, matplotlib, seaborn
- psycopg2 (for Postgres)
- sqlite3

Install dependencies:

```bash
pip install pandas numpy matplotlib seaborn psycopg2
```

## Insights Generated

- Brands and vendors with highest and lowest profit margins.
- Relationship between purchase quantities, costs, and gross margins.
- Inventory turnover rates for more effective stock management.

## License

MIT License (feel free to update as needed).

***

For questions or contributions, open an issue or submit a pull request.

[1](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/50359516/9757179d-31cd-4201-be1a-bcb44efb7190/Dataingestion.py)
[2](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/50359516/33f88da4-52f1-4dc5-a49c-1cd096370e05/SalesAnalysis.ipynb)
