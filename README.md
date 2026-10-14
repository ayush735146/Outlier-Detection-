# Outlier Detection using a Box Plot
**Veda Technology — Level 1, Day 28**  
**Author: AYUSH RAJPUT**

## Objective
Create a box plot for a numerical variable and identify possible outliers.

## Tools
- Python
- Pandas
- Matplotlib
- Jupyter Notebook (optional)

## Dataset
`employee_salary_dataset.csv` is a small sample employee dataset. The numerical column analyzed is `Salary_LPA` (salary in lakhs per annum).

## How it works
1. Load the CSV file using Pandas.
2. Calculate Q1, Q3 and the interquartile range (IQR).
3. Set lower and upper limits using `Q1 - 1.5 × IQR` and `Q3 + 1.5 × IQR`.
4. Identify values outside these limits.
5. Draw and save a box plot.

## Run the project
```bash
pip install -r requirements.txt
python outlier_detection.py
```

The script creates `box_plot.png` and `identified_outliers.csv`.

## Finding
The sample data contains a salary value much higher than the rest. The IQR method flags it as a potential outlier. This is a signal to investigate, not proof that the value is wrong. A high salary may be genuine, so outliers should not be removed automatically.
