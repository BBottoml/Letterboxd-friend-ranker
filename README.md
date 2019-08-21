# Letterboxd Friend Ranker
SEE HOW MUCH YOU HAVE IN COMMON WITH YOUR FRIENDS' FILM TASTES

Letterboxd Friend Ranker takes a given user, scrapes all their corresponding friends' ratings data, and proceeds to compute and rank the user's friends based on a commonality score. Each score is computed as such:  
<a href="url"><img src="https://raw.githubusercontent.com/BBottoml/Letterboxd-friend-ranker/master/Screenshot%20(71).png" align="center" height=35% width=35% ></a>

## Remarks:
I intend to implement more functionality; such as: clean charts illustrating difference between friends, predictions,further statistics, GUI interface with Tkinter, and more. Additionally, I will be working on releasing a PyPI library for scraping Letterboxd data and a Java package. Update (8/8/19): Moved away from Selenium in favor of Beautiful Soup; significantly increases speed of data scraping. 

## Getting Started

It is recommended to use a virtualenv to install necessary dependencies. The following illustrates how to do so:

### Installing
Pre-setup:

You will need to have virtualenv and pip (the Python package manager) installed

```
apt-get install python3-pip
```

Then, install pip3

```
pip3 install virtualenv
```

Step (i)

Create and activate a virtualenv 

```
virtualenv some-name
```

Step (ii)

Install the necessary dependencies

```
pip3 install -r requirements.txt
```

## Running and utilizing 

To run the program:

```
python3 -u main.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details