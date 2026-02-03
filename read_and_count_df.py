import pandas as pd

def read_csv(file_path):
    import csv
    data = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            data.append(row)
    return data

admission_pd = pd.read_csv("Students_admission_records.csv")

print(admission_pd.head())

count_missing = admission_pd.isnull().sum()
count_missing_as_percentage = (count_missing / len(admission_pd)) * 100
print("Missing values in each column:\n", count_missing)
print("\nMissing values as percentage of total rows:\n", count_missing_as_percentage)
    


