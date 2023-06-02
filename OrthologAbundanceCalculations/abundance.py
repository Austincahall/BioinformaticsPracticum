import pandas as pd
import openpyxl
# Read in the two Excel files
file1 = pd.read_excel('EcoliFullTable.xlsx')
file2 = pd.read_excel('H_pylori_Biomart_Full_Table.xlsx')

# Extract the 'eggNOG' column and its adjacent column (abundance) from each file
eggnog1 = file1[['eggNOG', 'Abundance']].values.tolist()
eggnog2 = file2[['eggNOG', 'Abundance']].values.tolist()

# Find the intersection of the two lists based on eggNOG values
common_eggnog = list(set([x[0] for x in eggnog1]).intersection(set([x[0] for x in eggnog2])))

# Create a dictionary to store the abundance values for each common eggNOG value
abundance_dict = {}

# Loop through each common eggNOG value
for eggNOG in common_eggnog:
    # Initialize the abundance value for this eggNOG
    abundance_dict[eggNOG] = [0, 0]  # [file1 abundance, file2 abundance]

    # Loop through each row in file1 and look for this eggNOG value
    for row in eggnog1:
        if row[0] == eggNOG:
            # Add the abundance value to the dictionary
            abundance_dict[eggNOG][0] += row[1]

    # Loop through each row in file2 and look for this eggNOG value
    for row in eggnog2:
        if row[0] == eggNOG:
            # Add the abundance value to the dictionary
            abundance_dict[eggNOG][1] += row[1]

# Print the abundance values for each common eggNOG value
for eggNOG in common_eggnog:
    print(f"{eggNOG}, {abundance_dict[eggNOG][0]} in file1, {abundance_dict[eggNOG][1]} in file2")


