import requests

weather = requests.get("https://wttr.in/Pune?format=3")
print("Weather in Pune:", weather.text)

astro = requests.get("http://api.open-notify.org/astros.json")
data = astro.json()

print("People in space:", data["number"])

spacecraft = {}
for person in data["people"]:
    if person["craft"] in spacecraft:
        spacecraft[person["craft"]].append(person["name"])
    else:
        spacecraft[person["craft"]] = [person["name"]]

for craft, names in spacecraft.items():
    print(f"\n{craft}:")
    for name in names:
        print(" -", name)