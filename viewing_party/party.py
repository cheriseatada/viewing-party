import copy
# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title and genre and rating:
        return {"title": title, "genre": genre, "rating": rating}
    else:
        return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if title in movie.values():
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    sum = 0.0
    num_movies = len(user_data["watched"])
    if num_movies:
        for movie in user_data["watched"]:
            sum += movie["rating"]
        return sum / num_movies
    else:
        return sum

def get_most_watched_genre(user_data):
    genres_tally = {}
    most_watched = {"title": None, "times_watched": 0}
    for movie in user_data["watched"]:
        if movie["genre"] in genres_tally:
            genres_tally[movie["genre"]] += 1
        else:
            genres_tally[movie["genre"]] = 1
    for key, value in genres_tally.items():
        if most_watched["times_watched"] < value:
            most_watched["title"] = key
            most_watched["times_watched"] = value
    return most_watched["title"]
    

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    unique = copy.deepcopy(user_data["watched"])
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie in unique:
                unique.remove(movie)
    return unique

def get_friends_unique_watched(user_data):
    user_watched = copy.deepcopy(user_data["watched"])
    friends_unique = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in user_watched and movie not in friends_unique:
                friends_unique.append(movie)
    return friends_unique
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    recs = []
    user_watched = user_data["watched"]
    user_subs = user_data["subscriptions"]
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in user_watched and movie["host"] in user_subs:
                recs.append(movie)
    return recs

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    genre = get_most_watched_genre(user_data)
    recs = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in user_data["watched"] and movie["genre"] == genre:
                recs.append(movie)
    return recs

def get_rec_from_favorites(user_data):
    recs = copy.deepcopy(user_data["favorites"])
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie in recs:
                recs.remove(movie)
    return recs
