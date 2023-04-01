import pandas as pd

input_filepath = "C:\\Users\\Admin\\Downloads\\Threat_actor\\etda_sector_all.xlsx"

df = pd.read_excel(input_filepath)

sector_list = []

for index , row in df.iterrows():

    row = list(row["observed sector"].replace("['","").replace("']","").split(", "))

    for i in row:

        if i != "[]":

            sector_list.append(i)

        else:

            no_action = "no action"

df_sector = pd.DataFrame()
df_sector["Sector"] = sector_list




output_filepath = "C:\\Users\\Admin\\Downloads\\Threat_actor\\etda_sector_split.xlsx"
df_sector.to_excel(output_filepath, index=False)
