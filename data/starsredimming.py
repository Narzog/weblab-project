import json
# Data to be written
# Opening JSON file
f = open('constellations.lines.json')
x = open('sample.json')

data = json.load(f)
stardata = json.load(x)
coords = data["features"][0]["geometry"]["coordinates"]
constset = []

greek_constellation_IAU = [
    "And",
    "Aqr",
    "Aql",
    "Ara",
    "Ari",
    "Aur",
    "Boo",
    "Cnc",
    "CMa",
    "CMi",
    "Cap",
    "Cas",
    "Cen",
    "Cep",
    "Cet",
    "CrB",
    "CrA",
    "Crv",
    "Crt",
    "Cyg",
    "Del",
    "Dra",
    "Equ",
    "Eri",
    "Gem",
    "Her",
    "Hya",
    "Leo",
    "Lep",
    "Lib",
    "Lup",
    "Lyr",
    "Oph",
    "Ori",
    "Peg",
    "Per",
    "Psc",
    "PsA",
    "Sge",
    "Sgr",
    "Sco",
    "Ser",
    "Tau",
    "Tri",
    "UMa",
    "UMi",
    "Vir",
]
finalfeatureslist = {"type": "FeatureCollection", }

print(data)
dog = 1
# manipulatedstarjson =
for consta in data["features"]:
    if consta["id"] in greek_constellation_IAU:
        coords = consta["geometry"]["coordinates"]
        for i in range(len(coords)):
            for x in range(len(coords[i])):
                input = []
                input.append(coords[i][x][0])
                input.append(coords[i][x][1])
                constset.append(input)

# print(constset)

# stardictiony =
starcords = stardata["features"][0]["geometry"]["coordinates"]
featureslist = []
for x in range(len(stardata["features"])):
    starcords = stardata["features"][x]["geometry"]["coordinates"]
    if starcords in constset:
        stardata["features"][x]["properties"]["mag"] = 1.8
json_object = json.dumps(stardata, indent=1)
with open("hah.json", "w") as outfile:
    outfile.write(json_object)


# data["type"] = "HELLO"
# print(data)
# Serializing json
