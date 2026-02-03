import pandas as pd

csvFilePath = "Students_admission_records.csv"
outputFilePath = "Cleaned_Students_admission_records_JM.csv"

def delete_missing_values(csvFilePath, outputFilePath):
    '''Function to read a CSV file, delete rows with missing values, and save the cleaned data to a new CSV file.   
    Parameters: csvFilePath - path to the input CSV file
                outputFilePath - path to the output CSV file
    Returns: None
    '''

    # Read the CSV file into a DataFrame
    df = pd.read_csv(csvFilePath)
    # Drop rows with any missing values
    print(df.shape)
    df_cleaned = df.dropna()
    # Save the cleaned DataFrame to a new CSV file  
    df_cleaned.to_csv(outputFilePath, index=False)
    print(f"Cleaned data saved to {outputFilePath}")

    return

delete_missing_values(csvFilePath, outputFilePath)