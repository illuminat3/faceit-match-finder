import requests

def extractAccountId(username):
    idUrl = f"https://www.faceit.com/api/users/v1/nicknames/{username}"
    
    try:
        response = requests.get(idUrl)
        response.raise_for_status() 

        data = response.json()
        playerId = data['payload']['id']
        
        return playerId
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
    except KeyError:
        print("playerId not found in the response")
        return None
    
def extractMatchCount(userId):
    url = f"https://www.faceit.com/api/stats/v1/stats/users/{userId}/games/csgo"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  

        data = response.json()
        m1_value = data['lifetime']['m1']
        
        return m1_value
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
    except KeyError:
        print("m1 value not found in the response")
        return None
    
def isGameFound(user_id, match_count, t_score, ct_score):
    match_url = f"https://www.faceit.com/api/stats/v1/stats/time/users/{user_id}/games/csgo?page=0&size={match_count}"

    search_string_1 = f"\"i18\":\"{t_score}"
    search_string_2 = f"\"i18\":\"{ct_score}"
    
    response = requests.get(match_url)
    
    if response.status_code == 200:
        data_str = response.text

        found_1 = search_string_1 in data_str
        found_2 = search_string_2 in data_str

        return found_1 or found_2
            
    else:
        print(f"Failed to retrieve data, status code: {response.status_code}")
        return None