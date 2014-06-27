import movie_site
import fresh_tomatoes

toy_story = movie_site.Movie('toy story',
	'story of boy and toys',
	'http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
	'https://www.youtube.com/watch?v=vwyZH85NQC4')

avatar = movie_site.Movie('avatar', 
	'marine on alien planet',
	'http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar_Teaser_Poster.jpg',
	'http://www.youtube.com/watch?v=-9ceBgWV8io')

movies = [toy_story, avatar]
#fresh_tomatoes.open_movies_page(movies)

print movie_site.Movie.__doc__
print movie_site.Movie.__name__
print movie_site.Movie.__module__