import os
import re
import pandas as pd
import time
import datetime
from etda_get_threat_actor import*
from etda_get_threat_actor_details import*
from etda_get_industry_choice import*
"""
#----------------------------Output File Directory Creation----------------------------#

now = datetime.datetime.now()
dt_string=now.strftime("%d-%m-%Y")

dt = datetime.datetime.today()
month_number = dt.month
year = dt.year

month_dict = {1: 'January', 2: 'Febuary', 3: 'March',
                  4: 'April', 5: 'May', 6: 'June',
                  7: 'July', 8: 'August', 9: 'September',
                  10: 'October', 11: 'November', 12: 'December'}

for key in month_dict:
    if month_number == key:
            month = month_dict[key]
    else:
        msg = "error"

filepath = "C:\\Users\\Admin\\Downloads\\Threat_actor" + "\\" + month + "_" + str(year) + "\\"

isExist = os.path.exists(filepath)

if isExist == False:

    os.mkdir(filepath)

else:

    error = "error"

output_filepath = filepath + str(dt_string)

#----------------------------Variables Declaration----------------------------#

dataframe_list = []

metadata = []

metadata_df = pd.DataFrame()

#----------------------------Get User Input----------------------------#

menu = menu()

print(menu)

while True:

    user_choice =int(input("Enter a industry number (1 to 41): "))

    if user_choice not in range(1, 42):

        print("Sorry, wrong selection")

        continue

    else:

        industry = industry_choice(user_choice)

        break
"""

url = "https://apt.etda.or.th/cgi-bin/listgroups.cgi"

#----------------------------Get Threat Actor----------------------------#

threat_actors_list, url_list = get_threat_actor(url)

# ----------------------------Get Threat Actor details----------------------------#

country_list, motivation_list, first_seen_list, sponsor_list, description_list, observed_sector_list, observed_countries_list, tools_list, information_list, mitre_attack_list, playbook_list = get_threat_actor_details(url_list)

print(len(country_list))
print(len(motivation_list))
print(len(first_seen_list))
print(len(sponsor_list))
print(len(description_list))
print(len(observed_sector_list))
print(len(observed_countries_list))
print(len(tools_list))
print(len(information_list))
print(len(mitre_attack_list))
print(len(playbook_list))


#----------------------------Create Dataframe----------------------------#
ta_information = {
        #'Threat Actor': threat_actors_list,
        #'URL': url_list,
        #'country' : country_list,
        #'motivation': motivation_list,
        #'first seen': first_seen_list,
        #'sponsor': sponsor_list,
        #'description': description_list,
        'observed sector' : observed_sector_list
        #'observed countries' : observed_countries_list,
        #'tools' : tools_list,
        #'information' : information_list,
        #'mitre attack' : mitre_attack_list,
        #'playbook' : playbook_list
    }
df = pd.DataFrame(ta_information)

df.to_excel("C:\\Users\\Admin\\Downloads\\Threat_actor\\etda_sector_all.xlsx")

#print("number of threat actors targetting " + str(industry) + ":" + str(len(df)))

#metadata.append("number of threat actors targetting " + str(industry) + ":" + str(len(df)))

#metadata_df["metadata"] = metadata

#metadata_df.to_excel(filepath + str(dt_string) + "_" + str(industry) + "_metadata.xlsx")
