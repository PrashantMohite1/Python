# dict

# invalid dict - (we cant add list as key), key must be imutable - str, int, tuple. 
# remove dict item 
# add dict item 
# change dict item


# loop through dict 
# check  if item present in dict 



d1 = {"name":"prashant", "age": 26}
print(d1)
print(type(d1))

print("Name : ", d1["name"])


d1.update({"city":"pune"})
# d1.update(("marks"))

# change dict item 
d1["age"] = 20 

print("updated dict : ", d1)

# valid and invalid , key must not be list - rest will be fine 

d2 = {"1" : "prashant mohite"}
d2 = {(1,2):"rakesh"}
# d3 = {["name", "age"], "prashant"}   # it will give us error because we cant pass list as a key
d3 = {"fav_colours": ["red","orange","green"]}

print(d1)
print(d2)
print(d3)


lp_dic1 = {"maths":59 , "science": 70 , "english": 90}

for i in lp_dic1:
    print(i)

for i in lp_dic1:
    print(i, ":", lp_dic1[i])

# check if key present in dict
print("maths" in lp_dic1)
print("geography" in lp_dic1)


