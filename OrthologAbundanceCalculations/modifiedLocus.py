import pandas as pd




# read in first Excel file with eggNOG and missing Abundance data
df1 = pd.read_excel('updated_file_with_Pylori.xlsx')

# read in second Excel file with eggNOG and Abundance data
df2 = pd.read_excel('M. pneumoniae Full Table (1).xlsx')

# create a dictionary to store eggNOG as key and a list of abundance as value
abundance_dict = {}
for index, row in df2.iterrows():
    eggNOG_value = row['eggNOG']
    abundance_value = row['Abundance']
    if eggNOG_value not in abundance_dict:
        abundance_dict[eggNOG_value] = [abundance_value]
    else:
        abundance_dict[eggNOG_value].append(abundance_value)

# loop through each row in the first file and update missing values
for index, row in df1.iterrows():
    eggNOG_value = row['eggNOG']
    if pd.isna(row['Abundance']):
        if eggNOG_value in abundance_dict:
            abundance_sum = sum(abundance_dict[eggNOG_value])
            df1.at[index, 'Abundance'] = abundance_sum

# save the updated dataframe to a new file
df1.to_excel('EcoliProteinComplexesALLDATA.xlsx', index=False)

