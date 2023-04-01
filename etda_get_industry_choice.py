import pandas as pd

def menu():
    menu = \
        "1: Aerospace 2: Automotive 3: Aviation 4: Casinos and Gambling\n \
        5: Chemical 6: Construction 7: Critical Infrastructure 8: Defense\n \
        9: Education 10: Energy 11: Engineering 12: Entertainment \n\
        13: Financial 14: Food and Agriculture 15: Gaming 16: Government\n \
        17: Healthcare 18: High-Tech 19: Hospitality 20: IT \n \
        21: Industrial 22: Law enforcement 23: Manufacturing 24: Maritime and Shipbuilding\n \
        25: Media 26: Mining 27: NGOs 28: Non-profit organizations \n \
        29: Oil and gas 30: Online video game companies 31: Petrochemical 32: Pharmaceutical\n \
        33: Research 34: Retail 35: Satellites 36: Shipping and Logistics\n \
        37: Technology 38: Telecommunications 39: Think Tanks 40: Transportation\n \
        41: Utilities\n "

    return menu


def industry_choice(user_choice):

    industry_dict = {
    1: "Aerospace",
    2: "Automotive",
    3: "Aviation",
    4: "Casinos and Gambling",
    5: "Chemical",
    6: "Construction",
    7: "Critical Infrastructure",
    8: "Defense",
    9: "Education",
    10: "Energy",
    11: "Engineering",
    12: "Entertainment",
    13: "Financial",
    14: "Food and Agriculture",
    15: "Gaming",
    16: "Government",
    17: "Healthcare",
    18: "High-Tech",
    19: "Hospitality",
    20: "IT",
    21: "Industrial",
    22: "Law enforcement",
    23: "Manufacturing",
    24: "Maritime and Shipbuilding",
    25: "Media",
    26: "Mining",
    27: "NGOs",
    28: "Non-profit organizations",
    29: "Oil and gas",
    30: "Online video game companies",
    31: "Petrochemical",
    32: "Pharmaceutical",
    33: "Research",
    34: "Retail",
    35: "Satellites",
    36: "Shipping and Logistics",
    37: "Technology",
    38: "Telecommunications",
    39: "Think Tanks",
    40: "Transportation",
    41: "Utilities",
    }

    for key in industry_dict:

        if user_choice == key:

            industry = industry_dict[key]

    return industry