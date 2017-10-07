class movie:
    """Movie class defined to enable adding movie objects to a known data 
       structure. The class has the attributes title, a URL for its poster
       and a link for its trailer on youtube"""
    def __init__(self, title, poster, link):
        self.title = title
        self.poster_image_url = poster
        self.trailer_youtube_url = link