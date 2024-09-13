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
    
def searchForGame(user_id, match_count):
    # Create the match URL
    match_url = f"https://www.faceit.com/api/stats/v1/stats/time/users/{user_id}/games/csgo?page=0&size={match_count}"
    
    # Define the search strings
    search_string_1 = "\"i18\":\"56"
    search_string_2 = "\"i18\":\"53"
    
    response = requests.get(match_url)
    
    if response.status_code == 200:
        data_str = response.text

        found_1 = search_string_1 in data_str
        found_2 = search_string_2 in data_str

        print(f"Search string 1 ('{search_string_1}') found: {found_1}")
        print(f"Search string 2 ('{search_string_2}') found: {found_2}")
            
        
    else:
        print(f"Failed to retrieve data, status code: {response.status_code}")

if __name__ == "__main__":
    username = "ErdNuckll"
    id = extractAccountId(username)
    matchCount = extractMatchCount(id)
    searchForGame(id, matchCount)