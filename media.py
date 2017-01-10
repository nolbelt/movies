import webbrowser

class Movie():

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """Hier ist ein Kommentar
        Self:
        self bezeichnet das objekt, das erzeugt wird. in diesem bsp. zunaechst das objekt toy_story
        it is a convention that self is used by most Python programmers. Using the word self will make your code more readable to other programmers. So we encourage that you do so.
        Check out section 9.4 (https://docs.python.org/2.7/tutorial/classes.html#random-remarks)of the Python documentation for more information.
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube


    def show_trailer(self):
        """Fuction to open the webbrowser and show the url"""
        webbrowser.open(self.trailer_youtube_url)
