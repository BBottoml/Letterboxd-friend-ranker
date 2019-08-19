from Assests.Extrafuncs import *

'''''''''''''''''''''''''''''''''''''''''''''''''''''
user class to store data pertaining to user
'''''''''''''''''''''''''''''''''''''''''''''''''''''


class User:

    def __init__(self, file_name, username):
        """
        :param file_name: File name for data file (if applicable):
        :param username: Main user's username
        """
        self.username = username
        self.file_name = file_name
        self.ratings_link = "https://letterboxd.com/" + self.username + "/films/" + "ratings/"
        print("\nScraping main user data...\n")
        self.films_ratings = scrape_ratings(self.ratings_link)