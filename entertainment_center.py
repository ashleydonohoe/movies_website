# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

# https://www.udacity.com/course/viewer#!/c-nd000/l-4185678656/e-991358856/m-1013629064

import media
import fresh_tomatoes

'''
Created instances for six movies, including their title, description, 
movie poster URL, YouTube trailer URL, release year, star review
rating, and IMDB link
'''

toy_story = media.Movie("Toy Story", 
	"A story of a boy and his toys that come to life",
	"http://cdn.collider.com/wp-content/uploads/toy-story-poster1.jpg",
	"https://www.youtube.com/watch?v=vwyZH85NQC4",
	1995,
	"5 stars",
	"http://www.imdb.com/title/tt0114709/")

eurotrip = media.Movie("Eurotrip",
	"Friends go on a crazy adventure overseas",
	"http://www.movie-poster-artwork-finder.com/posters/eurotrip-poster-artwork-scott-mechlowicz-jacob-pitts-michelle-trachtenberg.jpg",
	"https://www.youtube.com/watch?v=SeoX8MZd81E",
	2004,
	"4 stars",
	"http://www.imdb.com/title/tt0356150/"
)

the_year_dolly_parton_was_my_mom = media.Movie("The Year Dolly Parton Was My Mom",
	"A girl thinks Dolly Parton is her birth mother",
	"http://ia.media-imdb.com/images/M/MV5BMjA1MDc5MDQxN15BMl5BanBnXkFtZTcwMjE2MDI2NA@@._V1_SX640_SY720_.jpg",
	"https://www.youtube.com/watch?v=csdof52n5hc",
	2011,
	"4 stars",
	"http://www.imdb.com/title/tt1316624/")

camp_harlow = media.Movie("Camp Harlow",
	"A troubled girl has a change of heart",
	"http://i5.walmartimages.com/dfw/dce07b8c-84a2/k2-_f361cc22-51b3-41c0-8aec-5ea010221c4b.v1.jpg",
	"https://www.youtube.com/watch?v=c7BPofP6XEo",
	2014,
	"4 stars",
	"http://www.imdb.com/title/tt3184648/")

moonrise_kingdom = media.Movie("Moonrise Kingdom",
	"Two young kids fall in love and build their own kingdom",
	"http://t1.gstatic.com/images?q=tbn:ANd9GcTc9Qfqux_R9ycASZUOHD0R-1wNYeGYg-0Y9ICVmKOKekAGhplc",
	"https://www.youtube.com/watch?v=7N8wkVA4_8s",
	2012,
	"5 stars",
	"http://www.imdb.com/title/tt1748122/")

billy_madison = media.Movie("Billy Madison",
	"A grown man takes the challenge of going back to school",
	"http://www.gstatic.com/tv/thumb/movieposters/16468/p16468_p_v7_af.jpg",
	"https://www.youtube.com/watch?v=_-PZeKhMdiQ",
	1995,
	"5 stars",
	"http://www.imdb.com/title/tt0112508/")

# Array holding the six movies
movies = [toy_story, eurotrip, the_year_dolly_parton_was_my_mom,
		camp_harlow, moonrise_kingdom, billy_madison]

# Takes the list of movie instances to make an HTML file that will then open in browser
fresh_tomatoes.open_movies_page(movies)
