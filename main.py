from Assests.user import User
from Assests.commonality import *
import tkinter as tk 
import generate_report as gr
import scraper as sc

'''
Letterboxd friend ranker - main program
'''


def main():
    # output some information
    print("=====================================================")
    print("Welcome to Letterboxd Friend Ranker!")
    print("Instructions: This program compares you and")
    print("your friend's film taste. Once all the data has")
    print("been scraped and scores have been computed,")
    print("a report will be generated. The lower the avg.")
    print("difference, the better. If you and a friend do")
    print("not share at least 30 watched films, a score will")
    print("not be computed.")
    print("=====================================================\n")

    # prompt for info
    file_name = ""
    username = input("Enter your Letterboxd username: ")

    # create bot object
    current_user = User(file_name, username)

    # scrape data of user's friends
    print("Scraping friend data...\n")
    friends = sc.scraper(username)

    print("Computing scores...\n")
    # compute commonality for each friend
    results = commonality(current_user, friends)
    
    # write report
    print("Generating report...\n")
    gr.generate_report(results, current_user)

    print("Done! View the report in the current directory!")


if __name__ == "__main__":
    main()
