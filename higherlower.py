# accessing dictionary keys in a list by
# <list_name>[<list_index>][<dict_key>]

logo = """
.__     .__          .__                           
|  |__  |__|   ____  |  |__    ____  _______       
|  |  \ |  |  / ___\ |  |  \ _/ __ \ \_  __ \      
|   Y  \|  | / /_/  >|   Y  \\  ___/  |  | \/      
|___|  /|__| \___  / |___|  / \___  > |__|         
     \/     /_____/       \/      \/               
            .__                                    
            |  |    ____  __  _  __  ____  _______ 
            |  |   /  _ \ \ \/ \/ /_/ __ \ \_  __ \ 
            |  |__(  <_> ) \     / \  ___/  |  | \/
            |____/ \____/   \/\_/   \___  > |__|   
                                        \/           """

vs ="""
____   ____        
\   \ /   /  ______
 \   Y   /  /  ___/
  \     /   \___ \ 
   \___/   /____  >
                \/    """


# creating a list of items for comparison in the form of dictionary(key:value pairs)
data = [
    {
        'name':'Instagram',
        'follower_count':346,
        'description':'social media platform',
        'country':'United state'
    },
    {
        'name':'Cristiano Ronaldo',
        'follower_count':215,
        'description':'Footballer',
        'country':'Portugal'   
    },
    {
        'name':'Ariana Grande',
        'follower_count':183,
        'description':'Musician and actress',
        'country':'United state'
    },
    {
        'name':'Dwayne Johnson',
        'follower_count':181,
        'description':'actor and professional wrestler',
        'country':'United state'
    },
    {
        'name':'Kim Kardashian',
        'follower_count':167,
        'description':'reality TV personality and businesswoman',
        'country':'United state'
    },
    {
        'name':'Lionel Messi',
        'follower_count':149,
        'description':'Footballer',
        'country':'Argentina'
    },
    {
        'name':'Beyonce',
        'follower_count':145,
        'description':'musician',
        'country':'United state'
    },
    {
        'name':'Neymar',
        'follower_count':138,
        'description':'Footballer',
        'country':'Brasil'
    }
]

print(logo)
score = 0
for i in range(0,len(data)):
    print("compare A:" +' '+ data[i]['name']+', '+data[i]['description']+', '+data[i]['country'])
    print(vs)
    for j in range(i+1):
     print("Against B:" +' '+ data[j]['name']+', '+data[j]['description']+', '+data[j]['country'])    







