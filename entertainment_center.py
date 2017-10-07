import media
import operator
import fresh_tomatoes as ft


def __main__():
    #links for poster URLs
    lak = "https://upload.wikimedia.org/wikipedia/en/6/66/Lakshya.jpg"
    lag = "https://upload.wikimedia.org/wikipedia/en/b/b6/Lagaan.jpg"
    rdb = "https://upload.wikimedia.org/wikipedia/en/5/5f/RDB_poster.jpg"
    lbs = "https://upload.wikimedia.org/wikipedia/en/d/d2/Bhagatsinghlegend.jpg"  # NOQA
    mi = "https://upload.wikimedia.org/wikipedia/en/8/82/Mr._India_1987_poster.jpeg"  # NOQA
    nd = "https://upload.wikimedia.org/wikipedia/en/9/94/Nayadaur2.jpg"
    k = "https://upload.wikimedia.org/wikipedia/en/8/85/KahaaniPoster.jpg"
    aw = "https://upload.wikimedia.org/wikipedia/en/7/77/A_Wednesday_Poster.JPG"  # NOQA
    g = "https://upload.wikimedia.org/wikipedia/en/6/6a/Gangs_of_Wasseypur_poster.jpg"  # NOQA
    
    # links for trailers 
    lak_link = "https://www.youtube.com/watch?v=YoKGmYyljmc"
    lag_link = "https://www.youtube.com/watch?v=oSIGQ0YkFxs"
    rdb_link = "https://www.youtube.com/watch?v=jW0Io8yB638"
    lbs_link = "https://www.youtube.com/watch?v=CY37_al1IRs"
    mi_link = "https://www.youtube.com/watch?v=G-Qeug86sQc"
    nd_link = "https://www.youtube.com/watch?v=EK8XSmikhtg"
    k_link = "https://www.youtube.com/watch?v=j1wEeuAosNM"
    aw_link = "https://www.youtube.com/watch?v=u7RmUrMo770"
    g_link = "https://www.youtube.com/watch?v=j-AkWDkXcMY"
    
    # declare a list for movies and add all the movies you want to display
    movies = []
    
    movies.append(media.movie("Lakshya", lak, lak_link))
    movies.append(media.movie("Lagaan", lag, lag_link))
    movies.append(media.movie("Rang De Basanti", rdb, rdb_link))
    movies.append(media.movie("Legend of Bhagat Singh", lbs, lbs_link)) 
    movies.append(media.movie("Mr. India", mi, mi_link))
    movies.append(media.movie("Naya Daur", nd, nd_link))
    movies.append(media.movie("Kahaani", k, k_link))
    movies.append(media.movie("A Wednesday!", aw, aw_link))
    movies.append(media.movie("Gangs of Wasseypur", g, g_link))
   
    # sort the movie list by title
    movies.sort(key=operator.attrgetter('title'))    
    ft.open_movies_page(movies)
    

__main__()