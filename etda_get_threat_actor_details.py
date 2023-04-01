import requests
import re
from urllib.request import urlopen
import json

country_list = []
motivation_list = []
first_seen_list = []
sponsor_list=[]
description_list = []
observed_sector_list = []
observed_countries_list = []
tools_list = []
information_list = []
mitre_attack_list = []
playbook_list = []

def get_threat_actor_details(url_list):

    # -------------------------Variable Declaration------------------------#

    detail_main_url = "https://apt.etda.or.th"

    count = 0
    for url in url_list:

        print("APT # ", str(count))

        count += 1

        # -------------------------Web Request-------------------------#

        page = requests.get(url)

        download_statement = re.findall(r" or <a.href=.*title", page.text)

        try:

            query = download_statement[0].split("\"")[1]

            response = urlopen(detail_main_url + query)

            data_json = json.loads(response.read())

            # -------------------------Get Data-------------------------#

            if "country" in data_json["values"][0]:
                #print(data_json["values"][0]["country"])
                country_list.append(data_json["values"][0]["country"])

            else:
                country_list.append("NIL")

            if "motivation" in data_json["values"][0]:
                #print(data_json["values"][0]["motivation"])
                motivation_list.append(data_json["values"][0]["motivation"])

            else:
                motivation_list.append("NIL")

            if "first-seen" in data_json["values"][0]:
                #print(data_json["values"][0]["first-seen"])
                first_seen_list.append(data_json["values"][0]["first-seen"])

            else:
                first_seen_list.append("NIL")


            if "sponsor" in data_json["values"][0]:
                #print(data_json["values"][0]["sponsor"])
                sponsor_list.append(data_json["values"][0]["sponsor"])
            else:
                sponsor_list.append("NIL")

            if "description" in data_json["values"][0]:
                #print(data_json["values"][0]["description"])
                description_list.append(data_json["values"][0]["description"])

            else:
                description_list.append("NIL")

            if "observed-sectors" in data_json["values"][0]:
                # print(data_json["values"][0]["observed-countries"])
                observed_sector_list.append(data_json["values"][0]["observed-sectors"])

            else:
                observed_countries_list.append("NIL")

            if "observed-countries" in data_json["values"][0]:
                #print(data_json["values"][0]["observed-countries"])
                observed_countries_list.append(data_json["values"][0]["observed-countries"])

            else:
                observed_countries_list.append("NIL")

            if "tools" in data_json["values"][0]:
                #print(data_json["values"][0]["tools"])
                tools_list.append(data_json["values"][0]["tools"])
            else:
                tools_list.append("NIL")


            if "information" in data_json["values"][0]:
                #print(data_json["values"][0]["information"])
                information_list.append(data_json["values"][0]["information"])
            else:
                information_list.append("NIL")


            if "mitre-attack" in data_json["values"][0]:
                #print(data_json["values"][0]["mitre-attack"])
                mitre_attack_list.append(data_json["values"][0]["mitre-attack"])
            else:
                mitre_attack_list.append("NIL")

            if "playbook" in data_json["values"][0]:
                #print(data_json["values"][0]["Playbook"])
                playbook_list.append(data_json["values"][0]["playbook"])
            else:
                playbook_list.append("NIL")

        except IndexError:

            continue



    return country_list, motivation_list, first_seen_list, sponsor_list, description_list, observed_sector_list, observed_countries_list, tools_list, information_list, mitre_attack_list, playbook_list