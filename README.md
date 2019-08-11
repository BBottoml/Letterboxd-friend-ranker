# Letterboxd Friend Ranker
SEE HOW MUCH YOU HAVE IN COMMON WITH YOUR FRIENDS' FILM TASTES

Letterboxd Friend Ranker takes a given user, scrapes all their corresponding friend's ratings data, and proceeds to compute and rank  the user's friends based on a commonality score. Each score is computed as such:  
<a href="url"><img src="https://raw.githubusercontent.com/BBottoml/Letterboxd-friend-ranker/master/Screenshot%20(71).png" align="center" height=35% width=35% ></a>

## Remarks:
I intend to implement more functionality; such as: clean charts illustrating difference between friends, predictions, further statistics and more. Additionally, I will be working on releasing a PyPI library for scraping Letterboxd data and a Java package. Lastly, I plan to rewrite the scraping aspect of the project using BeautifulSoup as Selenium is rather slow for scraping so much data. 

## Getting Started

It is recommended that you use a Python virtualenv to install dependencies.

### Installing

Step (i)

```
virtualenv some-proj
```

Step (ii)

Install the main dependency after activating the virtual environment 

```
pip3 install selenium
```

Step(iii)

Lastly, you will need Chromedriver. This is a tool Google developed to automate/test web browsing. Please search and download the appropriate version. <a href="http://chromedriver.chromium.org/">Here</a> is the link to Chromedriver. I have utilized this program on both an Ubuntu machine and a Windows machine. If I recall correctly, Selenium (the main dependency) recommends Chomredriver 14.xxx for Linux. I run the newest Chormedriver release on the Windows machine.  

## Running and utilizing 

To run the program:

```
python3 -u main.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* Selenium
* Chromedriver
