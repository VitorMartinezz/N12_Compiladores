import csv
import json
import requests

finalresult = "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format("Name", "Height", "Mass", "Hair Color", "Skin Color", "Eye Color", "Birth Year", "Gender")

for x in range(20):
      try:
            resp = requests.get("https://swapi.dev/api/people/{}/".format(x + 1))
            Character = resp.json()
            print("Character {}".format(x + 1))
            print(Character["name"], Character["height"], Character["mass"], Character["hair_color"], Character["skin_color"],
            Character["eye_color"], Character["birth_year"], Character["gender"])
            finalresult += "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(Character["name"], Character["height"], Character["mass"], Character["hair_color"], Character["skin_color"],
                        Character["eye_color"], Character["birth_year"], Character["gender"])
      except: continue

arquivo = open("StarWarsCharacters.tsv", "w")
arquivo.write(finalresult)
arquivo.close()
