#change items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)
print('\n')

thisdict.update({"year": 2020})
print(thisdict)