import pandas as pd
import numpy as np
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)



path = r"C:\Users\haryanto\PycharmProjects\pythonProject\scopus.csv"
df_scopus = pd.read_csv(path, sep=",", index_col="Link")
drop_cols = ["Abstract", "Source title", "Author full names", "Author(s) ID"]
df_scopus = df_scopus.drop(columns=drop_cols)

"""
Create dataframe for summarize the csv data
"""
#print(df_scopus.head())
df_summary = pd.DataFrame({
    "Duplicated": df_scopus.duplicated().sum(),
    "Missing value": df_scopus.isna().sum().sum(),
    "Data rows": df_scopus.shape}
)
print("Summary of Dataframe")
print(df_summary)

'''
Display missing and duplicated values if applicable
'''
print("")
print("Duplicated Summary")
print(df_scopus.duplicated().sum())

print("")
print("Missing summary")
print(df_scopus.isna().sum())



keywords = [
    "speed", "camera", ""

]










