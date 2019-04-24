import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story","A story of a boy and his toys that come to life","https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v=4KPTXpQehio")
#print(toy_story.storyline)
fast = media.Movie("needforspeed","some of angry and driver fast","https://upload.wikimedia.org/wikipedia/en/2/2d/The_Fate_of_The_Furious_Theatrical_Poster.jpg","https://www.youtube.com/watch?v=uisBaTkQAEs")
#print(fast.storyline)
#fast.show_trailer()
school_of_rock = media.Movie("School of rock","using rock music to learn","https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg","https://www.youtube.com/watch?v=3PsUJFEBC74")
pirates =media.Movie("pirates of caribbean","In 2000, Pirates of the Caribbean: Battle for Buccaneer Gold","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTS2KxJXmcW59cb6y4DGBENO_ivED1xl6purUaI0cCAOqbWcMY5","https://www.youtube.com/watch?v=a5V5C8mEVzY")
needforspeed =media.Movie("Need For speed","just driver fast if u can","https://upload.wikimedia.org/wikipedia/en/thumb/5/59/Need_for_Speed_No_Limits_cover_art.jpeg/220px-Need_for_Speed_No_Limits_cover_art.jpeg","https://www.youtube.com/watch?v=e73J71RZRn8")
whiplash =media.Movie("whiplash","Whiplash is a 2014 American drama film","http://t3.gstatic.com/images?q=tbn:ANd9GcS_IwW5-_mWA1PXiPG4qEhLC6Q3vntQd7Bzgs_YE7HHFifItn2T","https://www.youtube.com/watch?v=7d_jQycdQGo")
movies = [toy_story,fast,school_of_rock,pirates,needforspeed,whiplash]
#fresh_tomatoes.open_movies_page(movies)
print(media.Movie.vaild_ratings)
