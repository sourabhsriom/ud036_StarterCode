import media
import operator
import fresh_tomatoes as ft


def __main__():
    
    lak = "https://upload.wikimedia.org/wikipedia/en/6/66/Lakshya.jpg"
    lag = "https://upload.wikimedia.org/wikipedia/en/b/b6/Lagaan.jpg"
    rdb = "https://upload.wikimedia.org/wikipedia/en/5/5f/RDB_poster.jpg"
    lbs = "https://upload.wikimedia.org/wikipedia/en/d/d2/Bhagatsinghlegend.jpg"  # NOQA
    mi = "https://upload.wikimedia.org/wikipedia/en/8/82/Mr._India_1987_poster.jpeg"  # NOQA
    nd = "https://upload.wikimedia.org/wikipedia/en/9/94/Nayadaur2.jpg"
    k = "https://upload.wikimedia.org/wikipedia/en/8/85/KahaaniPoster.jpg"
    aw = "https://upload.wikimedia.org/wikipedia/en/7/77/A_Wednesday_Poster.JPG"  # NOQA
    g = "https://upload.wikimedia.org/wikipedia/en/6/6a/Gangs_of_Wasseypur_poster.jpg"  # NOQA
    
    # declare a list for movies and add all the movies you want to display
    movies = []
    
    movies.append(media.movie("Lakshya", lak, "https://www.youtube.com/watch?v=YoKGmYyljmc"))  # NOQA
    movies.append(media.movie("Lagaan", lag, "https://www.youtube.com/watch?v=oSIGQ0YkFxs"))  # NOQA
    movies.append(media.movie("Rang De Basanti", rdb, "https://www.youtube.com/watch?v=jW0Io8yB638"))  # NOQA
    movies.append(media.movie("Legend of Bhagat Singh", lbs, "https://www.youtube.com/watch?v=CY37_al1IRs"))  # NOQA
    movies.append(media.movie("Mr. India", mi, "https://www.youtube.com/watch?v=G-Qeug86sQc"))  # NOQA
    movies.append(media.movie("Naya Daur", nd, "https://www.youtube.com/watch?v=EK8XSmikhtg"))  # NOQA
    movies.append(media.movie("Kahaani", k, "https://www.youtube.com/watch?v=j1wEeuAosNM"))  # NOQA
    movies.append(media.movie("A Wednesday!", aw, "https://www.youtube.com/watch?v=u7RmUrMo770"))  # NOQA
    movies.append(media.movie("Gangs of Wasseypur", g, "https://www.youtube.com/watch?v=j-AkWDkXcMY"))  # NOQA
   
    # sort the movie list by title
    movies.sort(key=operator.attrgetter('title'))    
    ft.open_movies_page(movies)
    

__main__()
        