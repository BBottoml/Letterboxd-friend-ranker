'''''''''''''''''''''''''''''''''''''''''''''''''''''
extra functions to be utilized throughout the 
program
'''''''''''''''''''''''''''''''''''''''''''''''''''''


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


def next_button(browser):
    """
    given a selenium browser object, determines if there is a next button
    :param browser:
    :return: boolean
    """
    try:
        browser.find_element_by_xpath('//*[@id="content"]/div/div/section/div[2]/div[2]/a')
        return True
    except:
        return False


def no_ratings(browser):
    """
    given a selenium browser object, determines if given page has no ratings
    :param browser:
    :return: boolean
    """
    try:
        table = browser.find_element_by_xpath('//*[@id="content"]/div/div/section/section')
        header = table.find_element_by_tag_name('h2').text
        return header == "No ratings yet"
    except:
        return False
