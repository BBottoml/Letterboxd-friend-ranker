from Assests.Extrafuncs import *
from selenium import webdriver

'''''''''''''''''''''''''''''''''''''''''''''''''''''
user class to store data pertaining to user
'''''''''''''''''''''''''''''''''''''''''''''''''''''


class User:

    def __init__(self, file_name, username):
        self.username = username
        self.file_name = file_name
        self.films_ratings = dict()
        try:
            self.process_data()
        except:
            self.scrape_main_user()

    def process_data(self):
        '''
        processes the data from provided input file
        '''
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

    def scrape_main_user(self):
        print("\nScraping main user data...\n")
        browser_profile = webdriver.ChromeOptions()
        browser_profile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        browser = webdriver.Chrome(options=browser_profile)

        # navigate to main user's following list
        following_url = "https://letterboxd.com/" + self.username + "/films/" + "ratings/"
        browser.get(following_url)

        # check to see if user has no ratings
        if (no_ratings(browser)):
            print("Provided main user has no ratings\n")
            print("Exiting...\n")
            exit(1)

        # iterate through films
        while True:

            # get main section of films and collect data
            film_section = browser.find_element_by_xpath('//*[@id="content"]/div/div/section/ul')
            films = film_section.find_elements_by_tag_name('li')

            for film in films:
                div = film.find_element_by_tag_name('div')
                film_name = div.get_attribute('data-film-name')
                ratings_div = film.find_element_by_tag_name('p').find_element_by_tag_name('span')
                rating = ratings_div.text
                rating = transform_ratings(rating)
                if rating == -1:
                    continue
                self.films_ratings[film_name] = rating

            if next_button(browser):
                browser.find_element_by_xpath('//*[@id="content"]/div/div/section/div[2]/div[2]/a').click()
            else:
                break

        browser.close()
