import webbrowser
class Movie():

    """ This is documentation of my movie program"""
    
    def __init__(self,movie_title,movie_storyline,year,produced_by,released_by,directors,awards,poster_image,trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.year = year
        self.produced_by = produced_by
        self.released_by = released_by
        self.directors = directors
        self.awards = awards
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
