import requests

def heroku_query(query): # A simple function to use requests.post to make the API call. 
    

    
    request = requests.post('https://danadventure.herokuapp.com/graphql/', json={'query': query})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))
        
all_rooms_query = """{ rooms { id x y floor nTo sTo eTo wTo uTo dTo region description} }
    """

all_items_query = """{ items { noun skill id} }
    """

