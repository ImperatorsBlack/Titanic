import numpy as np
import pandas as pd

def iqr_outlier(array):
    per_75 = np.nanpercentile(array, 75)
    #     print(per_25)
    per_25 = np.nanpercentile(array, 25)
    iqr = per_75 - per_25
    #     print(iqr)
    upper_b = per_75 + (1.5 * iqr)
    lower_b = per_25 - (1.5 * iqr)
    #     print(iqr)
    return [i for i in array if i > upper_b or i < lower_b]

def basic_explanation(df):
    df.shape
    print("Shape:")
    print("Rows:{} Cols:{}".format(str(df.shape[0]),str(df.shape[1])))
    print("="*100)
    print("Info:")
    print(df.info())
    print("="*100)
    print("Descriptive statistics for numeric columns:")
    print(df.describe())
    print("="*100)
    print("Descriptive statistics for object columns:")
    print(df.describe(include='object'))
    print("="*100)
    null_df = pd.DataFrame(df.isnull().sum())
    null_df.columns = ['Count']
    print("Columns with null values:")
    print(null_df[null_df['Count']>0])
    print("="*100)
    print("Outliers:")
    df_num_cols = df.select_dtypes(exclude=['object']).columns
    for x in df_num_cols:
        print(x)
        print(iqr_outlier(df[x]))
        print("-"*100)

if __name__ == '__main__':
    df = pd.read_csv('titanic.csv')
    print(basic_explanation(df))