scores={"John":85,"Sara":92,"Fraol":78}
new_dictionary={}
for key in scores:
  value=scores[key]
  new_dictionary[value]=key
print(new_dictionary)