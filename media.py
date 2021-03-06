# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define the class Movie. You could do this
# directly in entertainment_center.py but many developers keep their
# class definitions separate from the rest of their code. This also
# gives you practice importing Python files.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4185678656/m-1013629057

import webbrowser

class Movie():
    '''
    This class provides a way to store movie related information,
    including the title, storyline, release year, poster image
    URL, Youtube Trailer URL, star rating, and IMDB link
    '''

    def __init__(self, movie_title, movie_storyline, poster_image,
        trailer_youtube, release_year, review, imdb_link):
        ''' 
        initialize instance of class Movie with title,
        storyline, poster image url, Youtube trailer URL,
        release year, review rating, and IMDB link
        '''
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_year = release_year
        self.review = review
        self.imdb_link = imdb_link

    def show_trailer(self):
        '''
        Function to open the YouTube trailer for a movie
        in a web browser
        '''
        webbrowser.open(self.trailer_youtube_url)