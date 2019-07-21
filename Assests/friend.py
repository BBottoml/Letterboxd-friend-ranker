'''''''''''''''''''''''''''''''''''''''''''''''''''''
class to store data pertaining to user's friend
'''''''''''''''''''''''''''''''''''''''''''''''''''''


class Friend:

    def __init__(self, username, films_ratings):
        self.username = username
        self.films_ratings = films_ratings
        self.commonality = -1  # score computed for each friend
