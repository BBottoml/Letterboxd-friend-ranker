from Assests.user import User
from Assests.commonality import *
import scraper as sc
import collections


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
    print("not be computed. Remark: if you do not have the csv")
    print("data file called ratings.csv from Letterboxd,")
    print("simply enter nothing when prompted for a file")
    print("(press enter) and your data will be scraped.")
    print("=====================================================")

    # prompt for info
    file_name = input("Enter the CSV file for your data: ")
    username = input("Enter your Letterboxd username: ")

    # create bot object
    current_user = User(file_name, username)

    # scrape data of user's friends
    friends = sc.scraper(username)

    # compute commonality for each friend
    results = commonality(current_user, friends)

    # sort dictionary
    scores = list(results.values())
    scores.sort()
    invert_results = {v: k for k, v in results.items()}

    # write report
    result_fn = "Commonality report for - " + current_user.username + ".txt"
    result_file = open(result_fn, "w")
    result_file.write("Letterboxd Friend Ranker - Report!\n\n")
    most_common = invert_results[scores[0]]
    result_file.write("You had the most in-common with: " + most_common + "\n\n")

    result_file.write("Here's how it all stacked-up\n\n")
    for score in scores:
        key = invert_results[score]
        result_file.write("User: " + key + "\tAvg. difference: " + str(score) + "\n")

    result_file.close()


if __name__ == "__main__":
    main()
