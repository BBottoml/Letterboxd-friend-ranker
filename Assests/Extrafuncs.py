from bs4 import BeautifulSoup
import requests

'''''''''''''''''''''''''''''''''''''''''''''''''''''
extra functions to be utilized throughout the 
program
'''''''''''''''''''''''''''''''''''''''''''''''''''''
_domain = "https://letterboxd.com"


def clean_data(some_str):
    """
    given some string, returns a string stripped of bad values
    :param some_str: string to be cleaned
    :return: cleaned string
    """
    # dictionary of bad values
    bad_vals = {
        'â€“': "-",
        "\n": "",
        "â€”": "-",
        "â€˜": "‘",
        "â€™": "’",
        "â€œ": "“",
        "â€": "”"
    }

    for key, value in bad_vals.items():
        some_str = some_str.replace(key, value)
    return some_str


def transform_ratings(some_str):
    """
    transforms raw star rating into float value
    :param: some_str: actual star rating
    :rtype: returns the float representation of the given star(s)
    """
    stars = {
        "★": 1,
        "★★": 2,
        "★★★": 3,
        "★★★★": 4,
        "★★★★★": 5,
        "½": 0.5,
        "★½": 1.5,
        "★★½": 2.5,
        "★★★½": 3.5,
        "★★★★½": 4.5
    }
    try:
        return stars[some_str]
    except:
        return -1


def scrape_ratings(ratings_link):
    """
    takes a ratings link for a user and returns a dictionary where the key is the film title and score is the
    value
    :param ratings_link
    :return ratings dictonary

    """

    film_ratings = dict()

    while True:

        ratings_page = requests.get(ratings_link)

        # check to see page was downloaded correctly
        if ratings_page.status_code != 200:
            encounter_error("")

        soup = BeautifulSoup(ratings_page.content, 'html.parser')
        # browser.get(following_url)

        # grab the main film grid
        table = soup.find('ul', class_='poster-list')
        if table is None:
            return None

        films = table.find_all('li')

        # iterate through friends
        for film in films:
            panel = film.find('div').find('img')
            film_name = panel['alt']
            stars = transform_ratings(film.find('p', class_='poster-viewingdata').get_text().strip())
            if stars == -1:
                continue
            film_ratings[film_name] = stars

        # check if there is another page of ratings
        next_button = soup.find('a', class_='next')
        if next_button is None:
            break
        else:
            ratings_link = _domain + next_button['href']
    return film_ratings


def encounter_error(custom_msg):
    if custom_msg == "":
        print("\nAn Error has been encountered. Please try again.")
    else:
        print("\n", custom_msg)
    exit(1)
