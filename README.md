# Letterboxd Friend Ranker
SEE HOW MUCH YOU HAVE IN COMMON WITH YOUR FRIEND'S FILM TASTES

Letterboxd Friend Ranker takes a given user, scrapes all their corresponding friend's ratings data, and proceeds to compute and rank  the user's friends based on a commonality score. Each score is computed as such:  
<a href="url"><img src="https://raw.githubusercontent.com/BBottoml/Letterboxd-friend-ranker/master/Screenshot%20(71).png" align="center" height=30% width=30% ></a>


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

Lastly, you will need Chromedriver. This is a tool Google developed to automate/test web browsing. Please search and download the appropriate version. 

## Running and utilizing 

To run the program:

```
python3 main.py
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Selenium
* Chromedriver
* etc
