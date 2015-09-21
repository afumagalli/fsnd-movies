import webbrowser

class Movie():
    """ This class provides a way to store movie related information """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, poster_image,
                trailer_youtube, director, cast, year):
        # initializes an instance of class Movie
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.director = director
        self.cast = cast
        self.year = year

    def show_trailer(self):
        # opens a movie's trailer (for testing, not needed to make page)
        webbrowser.open(self.trailer_youtube_url)
