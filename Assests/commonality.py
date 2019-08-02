import math

'''''''''''''''''''''''''''''''''''''''''''''''''''''
computes commonality for each friend and returns
a sorted dictionary of ascending order. Remark:
lower the score the better (less difference) between
films. User and friend have to share at least
30 films
'''''''''''''''''''''''''''''''''''''''''''''''''''''


def commonality(main_user, friends):
    """
    given a User object, and the scraped list of friends, computes
    and returns a list of the corresponding scores
    :param main_user: User object for main user
    :param friends: List of friends (typically returned from scraper
    :return: list of scores
    """
    main_user_ratings = main_user.films_ratings
    scores = dict()

    for friend in friends:
        score = compute(friend, main_user_ratings)
        if score == -1:
            continue
        friend.commonality = score
        scores[friend.username] = score

    return scores


def compute(some_friend, main_user_ratings):
    """
    takes a Friend and List of ratings for main user
    and computes the difference. If the main user and
    given friend do not share at least 30 films, -1
    is returned
    :param some_friend: Friend object
    :param main_user_ratings:
    :return: -1 or float difference
    """
    friend_ratings = some_friend.films_ratings
    shared_films = 0
    running_difference = 0

    for key, value in friend_ratings.items():
        try:
            main_user_rating = float(main_user_ratings[key])  # check to see if main user has also viewed film
            running_difference += math.fabs(main_user_rating - float(value))
            shared_films += 1
        except:
            pass

    if shared_films < 30:
        return -1
    else:
        return running_difference / shared_films
