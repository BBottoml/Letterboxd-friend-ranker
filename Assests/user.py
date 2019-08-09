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
        self.films_ratings = dict()
        try:  # see if ratings file exists
            self.process_data()
        except FileNotFoundError:  # scrape data
            print("\nScraping main user data...\n")
            self.films_ratings = scrape_ratings(self.ratings_link)

    def process_data(self):
        """
        processes the data from provided input file
        :rtype: void
        """
        user_data = open(self.file_name, "r")

        # iterate line by line and pre-process data
        for line in user_data:
            temp_list = line.split(",")
            ratings_index = 4

            # occasionally movie title has comma; hence ratings is further in the list
            if len(temp_list) > 5:
                ratings_index = len(temp_list) - 1

            # store film as key, rating as value in dict
            self.films_ratings[clean_data(temp_list[1])] = clean_data(temp_list[ratings_index])

        user_data.close()  # close data file
        print("\nProcessing data...\n")
