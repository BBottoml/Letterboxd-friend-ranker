from Assests.friend import *
from Assests.Extrafuncs import *
from bs4 import BeautifulSoup
import requests

'''''''''''''''''''''''''''''''''''''''
Scrape user's data
'''''''''''''''''''''''''''''''''''''''

# globals
_domain = "https://letterboxd.com"


def scraper(username):
    """
    Scrape's provided user's friend's data
    :param username: the main user's username
    :return: a list of dictionaries of the user's friends. Where each key entry is a film, and value is rating
    """
    friends = []

    # navigate to user's following list
    following_url = _domain + "/" + username + "/following/"

    while True:

        following_page = requests.get(following_url)

        # check to see page was downloaded correctly
        if following_page.status_code != 200:
            encounter_error("")

        soup = BeautifulSoup(following_page.content, 'html.parser')

        # grab table and corresponding rows
        table = soup.find("tbody")
        if table is None:
            encounter_error("Provided user has no friends. Terminating...")

        rows = table.find_all('tr')

        # iterate through friends
        for row in rows:
            cols = row.find_all('td')
            friend_name = cols[1].find('a')['href']
            ratings_link = _domain + friend_name + "ratings/"
            friend_name = friend_name.split("/")[1]
            ratings = scrape_ratings(ratings_link)
            if ratings is not None:
                friends.append(Friend(friend_name, ratings))

        # check if there is another page of friends
        next_button = soup.find('a', class_='next')
        if next_button is None:
            break
        else:
            following_url = _domain + next_button['href']

    return friends
