import requests
import re

def get_threat_actor(url):

    # -------------------------Variable Declaration------------------------#
    #https: // apt.etda. or.th / cgi - bin / showcard.cgi?g = Aggah & n = 1
    main_url = "https://apt.etda.or.th/cgi-bin/showcard.cgi?g="

    threat_actors_list = []

    url_list = []

    #-------------------------Web Request-------------------------#

    page = requests.get(url)

    #download_statement = re.findall(r" or <a.href=.*title", page.text)


    #query = download_statement[0].split("\"")[1]

    threat_actors = re.findall(r"Show the card .* class", page.text)

    # -------------------------Iterate Web Content-------------------------#
    #count = 0
    for ta in threat_actors:

        #print("APT # ", str(count))

        #count += 1

        threat_actor = ta.split(" class")[0].split("for ")[1].replace('\"', '')

        threat_actors_list.append(threat_actor)

        #--------------------------threat actor url--------------------------#

        query = threat_actor.replace(',', "%2C").replace(" ", "%20")

        url_list.append(main_url + str(query))

    return threat_actors_list, url_list