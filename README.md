# Indian-Employee-data-analysis-using-Numpy-and-Pandas
Python data cleaning pipeline for an Indian employee dataset — handles missing values, duplicates, outliers, and invalid entries using pandas &amp; numpy.

## 🛠 Features

- **Missing Value Handling** — Fills missing `Salary` values with the column mean and missing `Performance Rating` values with the median
- **Infinite Value Handling** — Detects and replaces infinite values with NaN before imputation
- **Duplicate Removal** — Drops duplicate employee records
- **Negative Value Correction** — Replaces invalid negative salaries with the mean salary
- **Outlier Detection** — Removes salary outliers using the 3-standard-deviation rule
- **Clean Export** — Saves the cleaned dataset as a new CSV file

## 🧰 Tech Stack

- Python 3.13
- pandas
- numpy

## 📂 Project Structure
