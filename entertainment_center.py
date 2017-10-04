import media
import operator

from media import movie
import fresh_tomatoes as ft
def __main__():
    
    # declare a list for movies and add all the movies you want to display
    
    movies = []
    
    movies.append(media.movie("Lakshya", "https://upload.wikimedia.org/wikipedia/en/6/66/Lakshya.jpg", "https://www.youtube.com/watch?v=YoKGmYyljmc"))
    movies.append(media.movie("Lagaan", "https://upload.wikimedia.org/wikipedia/en/b/b6/Lagaan.jpg", "https://www.youtube.com/watch?v=oSIGQ0YkFxs"))
    movies.append(media.movie("Rang De Basanti", "https://upload.wikimedia.org/wikipedia/en/5/5f/RDB_poster.jpg", "https://www.youtube.com/watch?v=jW0Io8yB638"))
    movies.append(media.movie("Legend of Bhagat Singh", "https://upload.wikimedia.org/wikipedia/en/d/d2/Bhagatsinghlegend.jpg", "https://www.youtube.com/watch?v=CY37_al1IRs"))
    movies.append(media.movie("Mr. India", "https://upload.wikimedia.org/wikipedia/en/8/82/Mr._India_1987_poster.jpeg", "https://www.youtube.com/watch?v=G-Qeug86sQc"))
    movies.append(media.movie("Naya Daur", "https://upload.wikimedia.org/wikipedia/en/9/94/Nayadaur2.jpg", "https://www.youtube.com/watch?v=EK8XSmikhtg"))
    movies.append(media.movie("Kahaani", "https://upload.wikimedia.org/wikipedia/en/8/85/KahaaniPoster.jpg", "https://www.youtube.com/watch?v=j1wEeuAosNM"))
    movies.append(media.movie("A Wednesday!", "https://upload.wikimedia.org/wikipedia/en/7/77/A_Wednesday_Poster.JPG", "https://www.youtube.com/watch?v=u7RmUrMo770"))
    movies.append(media.movie("Gangs of Wasseypur", "https://upload.wikimedia.org/wikipedia/en/6/6a/Gangs_of_Wasseypur_poster.jpg", "https://www.youtube.com/watch?v=j-AkWDkXcMY"))
   
    
    # sort the movie list by title
    movies.sort(key = operator.attrgetter('title'))
    
        
    ft.open_movies_page(movies)
    

__main__()
        