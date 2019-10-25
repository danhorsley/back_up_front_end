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

auth_key = login()

def look(auth_key = auth_key):
    auth_key = login()['key']
    #print(auth_key)
    request = requests.post('https://danpatadv.herokuapp.com/look/', headers=\
{"Authorization" : f"Token {auth_key}"})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}".format(request.status_code))

def move(auth_key = auth_key,direct = 'n'):
    auth_key = login()['key']
    #print(auth_key)
    request = requests.post('https://danpatadv.herokuapp.com/move/', headers=\
{"Authorization" : f"Token {auth_key}"},json={'direction' : direct})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}".format(request.status_code))



def pick(auth_key = auth_key,obj = ''):
    auth_key = login()['key']
    #print(auth_key)
    request = requests.post('https://danpatadv.herokuapp.com/pick', headers=\
{"Authorization" : f"Token {auth_key}"},json={'pick up' : obj})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}".format(request.status_code))


def move_n(auth_key = auth_key):
    #auth_key = login()['key']
    #print(auth_key)
    request = requests.post('https://danpatadv.herokuapp.com/move/', headers=\
{"Authorization" : f"Token {auth_key}"},json={'direction' : 'n'})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}".format(request.status_code))

def move_s(auth_key = auth_key):
    #auth_key = login()['key']
    #print(auth_key)
    request = requests.post('https://danpatadv.herokuapp.com/move/', headers=\
{"Authorization" : f"Token {auth_key}"},json={'direction' : 's'})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}".format(request.status_code))


def move_e(auth_key = auth_key):
    #auth_key = login(auth_key = auth_key)['key']
    #print(auth_key)
    request = requests.post('https://danpatadv.herokuapp.com/move/', headers=\
{"Authorization" : f"Token {auth_key}"},json={'direction' : 'e'})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}".format(request.status_code))

def move_w(auth_key = auth_key):
    #auth_key = login()['key']
    #print(auth_key)
    request = requests.post('https://danpatadv.herokuapp.com/move/', headers=\
{"Authorization" : f"Token {auth_key}"},json={'direction' : 'w'})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}".format(request.status_code))

def move_u(auth_key = auth_key):
    #auth_key = login()['key']
    #print(auth_key)
    request = requests.post('https://danpatadv.herokuapp.com/move/', headers=\
{"Authorization" : f"Token {auth_key}"},json={'direction' : 'u'})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}".format(request.status_code))

def move_d(auth_key = auth_key):
    #auth_key = login()['key']
    #print(auth_key)
    request = requests.post('https://danpatadv.herokuapp.com/move/', headers=\
{"Authorization" : f"Token {auth_key}"},json={'direction' : 'd'})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}".format(request.status_code))

