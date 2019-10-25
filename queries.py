import requests

all_rooms_query = """{ rooms { id x y floor nTo sTo eTo wTo uTo dTo region description itemdesc} }
    """

all_items_query = """{ items { noun skill id} }"""

def login(username = 'danh', passwords = 'mudgame19'):
    request = requests.post('https://danpatadv.herokuapp.com/login/', 
                                    json={'username' : username, 'password' : passwords})
    
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}".format(request.status_code))

class my_query:
    def __init__(self):
        self.auth = login()['key']

    def heroku_query(self,query): # A simple function to use requests.post to make the API call. 
        

        
        request = requests.post('https://danpatadv.herokuapp.com/graphql/', json={'query': query})
        if request.status_code == 200:
            return request.json()
        else:
            raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))




    def look(self):
        #auth_key = login()['key']
        #print(auth_key)
        request = requests.post('https://danpatadv.herokuapp.com/look/', headers=\
    {"Authorization" : f"Token {self.auth}"})
        if request.status_code == 200:
            return request.json()
        else:
            raise Exception("Query failed to run by returning code of {}".format(request.status_code))

    def move(self ,direct = 'n'):
        auth_key = login()['key']
        #print(auth_key)
        request = requests.post('https://danpatadv.herokuapp.com/move/', headers=\
    {"Authorization" : f"Token {self.auth}"},json={'direction' : direct})
        if request.status_code == 200:
            return request.json()
        else:
            raise Exception("Query failed to run by returning code of {}".format(request.status_code))



    def pick(self, obj = ''):
        
        request = requests.post('https://danpatadv.herokuapp.com/pick', headers=\
    {"Authorization" : f"Token {self.auth}"},json={'pick up' : obj})
        if request.status_code == 200:
            return request.json()
        else:
            raise Exception("Query failed to run by returning code of {}".format(request.status_code))


    def move_n(self):
        
        request = requests.post('https://danpatadv.herokuapp.com/move/', headers=\
    {"Authorization" : f"Token {self.auth}"},json={'direction' : 'n'})
        if request.status_code == 200:
            return request.json()
        else:
            raise Exception("Query failed to run by returning code of {}".format(request.status_code))

    def move_s(self):
        
        request = requests.post('https://danpatadv.herokuapp.com/move/', headers=\
    {"Authorization" : f"Token {self.auth}"},json={'direction' : 's'})
        if request.status_code == 200:
            return request.json()
        else:
            raise Exception("Query failed to run by returning code of {}".format(request.status_code))


    def move_e(self):
        
        request = requests.post('https://danpatadv.herokuapp.com/move/', headers=\
    {"Authorization" : f"Token {self.auth}"},json={'direction' : 'e'})
        if request.status_code == 200:
            return request.json()
        else:
            raise Exception("Query failed to run by returning code of {}".format(request.status_code))

    def move_w(self):
        
        request = requests.post('https://danpatadv.herokuapp.com/move/', headers=\
    {"Authorization" : f"Token {self.auth}"},json={'direction' : 'w'})
        if request.status_code == 200:
            return request.json()
        else:
            raise Exception("Query failed to run by returning code of {}".format(request.status_code))

    def move_u(self):
        
        request = requests.post('https://danpatadv.herokuapp.com/move/', headers=\
    {"Authorization" : f"Token {self.auth}"},json={'direction' : 'u'})
        if request.status_code == 200:
            return request.json()
        else:
            raise Exception("Query failed to run by returning code of {}".format(request.status_code))

    def move_d(self):
        
        request = requests.post('https://danpatadv.herokuapp.com/move/', headers=\
    {"Authorization" : f"Token {self.auth}"},json={'direction' : 'd'})
        if request.status_code == 200:
            return request.json()
        else:
            raise Exception("Query failed to run by returning code of {}".format(request.status_code))

