import requests

def heroku_query(query): # A simple function to use requests.post to make the API call. 
    

    
    request = requests.post('https://danpatadv.herokuapp.com/graphql/', json={'query': query})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))
        
all_rooms_query = """{ rooms { id x y floor nTo sTo eTo wTo uTo dTo region description itemdesc} }
    """

all_items_query = """{ items { noun skill id} }
    """
def login(username = 'danh', passwords = 'mudgame19'):
    request = requests.post('https://danpatadv.herokuapp.com/login/', 
                                    json={'username' : username, 'password' : passwords})
    
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}".format(request.status_code))

def look():
    auth_key = login()['key']
    #print(auth_key)
    request = requests.post('https://danpatadv.herokuapp.com/look/', headers=\
{"Authorization" : f"Token {auth_key}"})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}".format(request.status_code))

def move(direct = 'n'):
    auth_key = login()['key']
    #print(auth_key)
    request = requests.post('https://danpatadv.herokuapp.com/move/', headers=\
{"Authorization" : f"Token {auth_key}"},json={'direction' : direct})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}".format(request.status_code))

def pick(obj = ''):
    auth_key = login()['key']
    #print(auth_key)
    request = requests.post('https://danpatadv.herokuapp.com/pick', headers=\
{"Authorization" : f"Token {auth_key}"},json={'pick up' : obj})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}".format(request.status_code))

