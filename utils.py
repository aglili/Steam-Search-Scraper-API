import json
import re
from bs4 import BeautifulSoup
import requests

def scrape_steam_store_data(url: str):
    html = requests.get(url=url)

    # Check if the request was successful
    if html.status_code == 200:
        # Get the content of the response
        content = html.content

        # Create a BeautifulSoup object from the HTML content
        soup = BeautifulSoup(content, 'html.parser')

        # Create an empty dictionary to store game data
        game_data = {}

        # Find all 'a' tags that contain game information
        game_tags = soup.find_all('a', class_='search_result_row')

        # Loop through each game tag to extract information
        for game_tag in game_tags:
            # Extract specific data from each game tag
            title = game_tag.find('span', class_='title').text.strip()

            # Remove Unicode characters from the title
            title = re.sub(r'[^\x00-\x7F]+', '', title)

            # Extract the game URL
            game_url = game_tag.get('href')

            # Check for the existence of 'search_released' div
            release_date_elem = game_tag.find('div', class_='col search_released')
            release_date = release_date_elem.text.strip() if release_date_elem else "N/A"

            review_score_elem = game_tag.find('span', class_='search_review_summary')
            review_score = review_score_elem['data-tooltip-html'].replace('<br>', ' ') if review_score_elem else "N/A"

            final_price_elem = game_tag.find('div', class_='discount_final_price')
            final_price = final_price_elem.text.strip() if final_price_elem else "N/A"

            original_price_elem = game_tag.find('div', class_='discount_original_price')
            original_price = original_price_elem.text.strip() if original_price_elem else "N/A"

            discount_elem = game_tag.find('div', class_='discount_pct')
            discount = discount_elem.text.strip() if discount_elem else "N/A"

            # Create a dictionary for each game and add it to the game_data dictionary
            game_info = {
                'Title': title,
                'URL': game_url,
                'Release Date': release_date,
                'Review Score': review_score,
                'Final Price': final_price,
                'Original Price': original_price,
                'Discount': discount
            }
            game_data[title] = game_info


        # Return extracted data as JSON
        return game_data
    else:
        return None
    

def add_price_filter(url, price_filter):
    if price_filter == "under_10":
        return url + "&maxprice=10"
    elif price_filter == "under_15":
        return url + "&maxprice=15"
    elif price_filter == "under_20":
        return url + "&maxprice=20"
    elif price_filter == "under_40":
        return url + "&maxprice=40"
    elif price_filter == "under_60":
        return url + "&maxprice=60"
    elif price_filter == "under_100":
        return url + "&maxprice=100"
    else:
        return url
    

def add_os(url, os):
    if os == "windows":
        return url + "&os=win"
    elif os == "mac":
        return url + "&os=mac"
    elif os == "linux":
        return url + "&os=linux"
    else:
        return url
    


def add_search(url, search):
    return url + f"&term={search}"



def special_offers(url,specials:bool):
    if specials == True:
        return url + "&specials=1"
    return url

def add_tag(url, tag):
    if tag == "adventure":
        return url + "&tags=21"
    elif tag == "action":
        return url + "&tags=19"
    elif tag == "strategy":
        return url + "&tags=9"
    elif tag == "rpg":
        return url + "&tags=122"
    elif tag == "indie":
        return url + "&tags=492"
    elif tag == "simulation":
        return url + "&tags=599"
    elif tag == "casual":
        return url + "&tags=597"
    elif tag == "puzzle":
        return url + "&tags=1664"
    elif tag == "arcade":
        return url + "&tags=1773"
    elif tag == "platformer":
        return url + "&tags=1625"
    elif tag == "racing":
        return url + "&tags=699"
    elif tag == "sports":
        return url + "&tags=701"
    elif tag == "massively_multiplayer":
        return url + "&tags=128"
    elif tag == "family_friendly":
        return url + "&tags=5350"
    elif tag == "fighting":
        return url + "&tags=1743"
    elif tag == "board_games":
        return url + "&tags=1770"
    elif tag == "educational":
        return url + "&tags=599"
    return url
    

    
