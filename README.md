# Pandas Virtual Column Utility
A robust utility function for dynamically adding calculated columns to a pandas DataFrame based on string expressions.

## Overview
The `add_virtual_column` function allows users to perform basic arithmetic operations (addition, subtraction, multiplication) between two existing columns with an immutability and strict validation.

## Features
 * **Safe Data Handling:** Uses deep copy to ensure the original DataFrame remains untouched.
 * **Input Validation:** Enforces strict naming conventions for columns (letters and underscores only).
 * **Error Handling:** Returns an empty DataFrame instead of raising exceptions when encountering invalid inputs or incompatible data types.
 * **Modern Python:** Leverages Python 3.10+ match-case syntax for clean logic.

## Requirements
 * Python: 3.10 +
 * Libraries: pandas

## Installation
```Bash
pip install pandas
```

## Example of Usage
```Python
import pandas as pd
from solution import add_virtual_column 
```

## Prepare sample data
```Python
data = pd.DataFrame({
    'sales': [100, 200, 300],
    'costs': [40, 60, 80]
})
```
## Add a calculated 'profit' column
```Python
result_df = add_virtual_column(data, 'sales - costs', 'profit')

if not result_df.empty:
    print(result_df)
else:
    print("Validation failed or expression was invalid.")
```

## Design Decisions
* **Immutability:** Returns a deep copy of the data to prevent side effects and ensure the original DataFrame remains untouched.
* **Regex-based Parsing:** The function uses `re.split` and `re.match` to ensure that only authorized column names and operators are processed.
* **Comprehensive Error Handling:** A broad `try-except` block in the calculation phase catches `TypeError` or `ValueError` that might occur if columns contain non-numeric data, ensuring the application never crashes.