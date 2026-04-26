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
country = input('enter your country \n')
if country in populations :
	print(f"The population of {country} is {populations[country]}")
else:
	print(f'no information on {country}')
