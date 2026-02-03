def remove_duplicates(file_path):
    import pandas as pd

    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Remove duplicate rows
    df_no_duplicates = df.drop_duplicates()

    return df_no_duplicates


print(remove_duplicates("Students_admission_records.csv"))
