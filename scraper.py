from Assests.friend import *
from Assests.Extrafuncs import *
from selenium import webdriver
from time import sleep

'''''''''''''''''''''''''''''''''''''''
Scrape user's data
'''''''''''''''''''''''''''''''''''''''


def scraper(username):
    browser_profile = webdriver.ChromeOptions()
    browser_profile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
    browser = webdriver.Chrome(options=browser_profile)
    friends = []

    # navigate to user's following list
    following_url = "https://letterboxd.com/" + username + "/following/"
    browser.get(following_url)

    while True: # There may be more than one page of friends
        # grab table
        table = browser.find_element_by_xpath('//*[@id="content"]/div/div/section/table/tbody')
        rows = table.find_elements_by_tag_name('tr')  # grab all rows
        for row in rows:
            browser2 = webdriver.Chrome(options=browser_profile)  # launch new window for friend
            new_friend = build_friend(row, browser2)
            browser2.close()

            # if no ratings are found in given friend, build_friend() returns None
            # hence, we check if it is None before appending
            if new_friend is not None:
                friends.append(new_friend)

            sleep(1)

        # check if more pages of friends
        if next_button(browser):
            browser.find_element_by_xpath('//*[@id="content"]/div/div/section/div[2]/div[2]/a').click()
            sleep(0.2)
        else: # no more pages of friends .. break
            break
            
    browser.close()
    return friends


def build_friend(some_friend, browser):
    cols = some_friend.find_elements_by_tag_name('td')
    ratings_link = cols[1].find_element_by_tag_name('a').get_attribute('href')
    ratings_link_2 = ratings_link + "ratings/"
    exceptions = 0

    # sometimes an exception is thrown during this part. If this is the case, simply retry
    while True:

        # if we continously get exceptions, letterboxd is likely having issues and 
        # we should quit the program
        if exceptions > 3:  
            print("Scraping failed...terminating.")
            exit(1)
        
        try:
            # navigate to friend's ratings page
            browser.get(ratings_link_2)
            films_ratings = dict()

            # ensure there are ratings present
            # No ratings will only occur when user has seen 0 films
            if no_ratings(browser):
                return None

            # maintain infinite loop until no more pages are found
            while True:

                # get main section of films and collect data
                film_section = browser.find_element_by_xpath('//*[@id="content"]/div/div/section/ul')
                films = film_section.find_elements_by_tag_name('li')

                # iterate through films on current page
                for film in films:
                    div = film.find_element_by_tag_name('div')
                    film_name = div.get_attribute('data-film-name')
                    ratings_div = film.find_element_by_tag_name('p').find_element_by_tag_name('span')
                    rating = ratings_div.text
                    rating = transform_ratings(rating)
                    if rating == -1:
                        continue
                    films_ratings[film_name] = rating

                # click next page if present
                if next_button(browser):
                    browser.find_element_by_xpath('//*[@id="content"]/div/div/section/div[2]/div[2]/a').click()
                    sleep(0.2)
                else:
                    break

            # navigate back to original
            some_list = ratings_link.split("/")
            new_friend = Friend(some_list[3], films_ratings)
            return new_friend
        except:
            exceptions += 1
            continue
