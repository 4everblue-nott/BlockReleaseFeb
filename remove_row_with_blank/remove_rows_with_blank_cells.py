def remove_blank(CSV_file):
    '''Takes a CSV file and removes rows containing blank cells'''
    import pandas as pd
    df = pd.read_csv(CSV_file)
    df_cleaned = df.dropna()
    import os
    dir_name, base_name = os.path.split(CSV_file)
    output_file = os.path.join(dir_name, 'cleaned_' + base_name)
    df_cleaned.to_csv(output_file, index=False)
    return output_file

