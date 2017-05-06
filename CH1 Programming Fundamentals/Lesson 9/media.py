import webbrowser
from PIL import Image

class Movie():
    '''This class provides a way to store movie info'''
    VALID_RATINGS = ['G','PG', 'PG-13', 'R']

    def __init__(self, title, storyline, poster_image,
                 youtube_trailer):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_trailer

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    def show_poster(self):
        image = Image.open(self.poster_image_url)
        image.show()

    def description(self):
        desc = "Title: %s\nStoryline: %s" % (self.title, self.storyline)
        return desc
