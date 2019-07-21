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

    # grab table
    table = browser.find_element_by_xpath('//*[@id="content"]/div/div/section/table/tbody')
    rows = table.find_elements_by_tag_name('tr')  # grab all rows
    rows_length = len(rows)

    for i in range(0, rows_length):
        user_friend = rows[i]
        friends.append(build_friend(user_friend, browser))

        # we need to navigate back and re-grab table, rows
        browser.get(following_url)
        table = browser.find_element_by_xpath('//*[@id="content"]/div/div/section/table/tbody')
        rows = table.find_elements_by_tag_name('tr')

        sleep(1)

    return friends


def build_friend(some_friend, browser):
    # navigate to friend's ratings page
    cols = some_friend.find_elements_by_tag_name('td')
    ratings_link = cols[1].find_element_by_tag_name('a').get_attribute('href')
    ratings_link_2 = ratings_link + "ratings/"
    browser.get(ratings_link_2)
    films_ratings = dict()

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
            films_ratings[film_name] = rating

        if next_button(browser):
            browser.find_element_by_xpath('//*[@id="content"]/div/div/section/div[2]/div[2]/a').click()
        else:
            break

    # navigate back to original
    some_list = ratings_link.split("/")
    new_friend = Friend(some_list[3], films_ratings)
    return new_friend
