# nesting in list and dictionaries

travel_log = [

{   "country": "france",
    "visits": 12,
    "cities": ["paris","lille","dijon"]
},

{   "country": "germany",
    "visits": 5,
    "cities": ['berlin','hamburg','stuttgart']
}

]
new_dict = {}
def add_new_country(country_visited,num_of_visits,cities_visited):
    
            new_dict["country"] = country_visited
            new_dict["visits"] =num_of_visits 
            new_dict["cities"] = cities_visited
            travel_log.append(new_dict)
            
        


add_new_country("russia", 2, ["moscow","saint petersburg"])
print(travel_log)