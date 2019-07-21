import math

'''''''''''''''''''''''''''''''''''''''''''''''''''''
computes commonality for each friend and returns
a sorted dictionary of ascending order. Remark:
lower the score the better (less difference) between
films. User and friend have to share at least
30 films
'''''''''''''''''''''''''''''''''''''''''''''''''''''


def commonality(main_user, friends):
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
