"""
Global Population Lookup Utility
Author: Daniel Kehinde
Description: This script allows users to query a dictionary of country 
populations. It handles case-sensitivity using .title() and formats 
large integers with commas for readability.
"""
populations = {
    "United States": 331449281,
    "Nigeria": 206139589,
    "India": 1380004385,
    "Kenya": 54771231,
    "Philippines": 111046913,
    "Ghana": 31255435,
    "Brazil": 213947263,
    "South Africa": 59622350,
    "Pakistan": 220892340,
    "Canada": 38008005
}

user_input = input("Enter the country name: ").strip().title()

if user_input in populations:
    pop_count = populations[user_input]
    print(f"The population of {user_input} is {pop_count:,}")
else:
    print(f"Data for '{user_input}' is not available in our database.")
