'''''''''''''''''''''''''''''''''''''''''''''''''''''
extra functions to be utilized throughout the 
program
'''''''''''''''''''''''''''''''''''''''''''''''''''''


def clean_data(some_str):
    '''
    accepts a string a strips all bad characters
    '''

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
    try:
        browser.find_element_by_xpath('//*[@id="content"]/div/div/section/div[2]/div[2]/a')
        return True
    except:
        return False


def no_ratings(browser):
    try:
        table = browser.find_element_by_xpath('//*[@id="content"]/div/div/section/section')
        header = table.find_element_by_tag_name('h2').text
        return header == "No ratings yet"
    except:
        return False
