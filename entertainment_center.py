import media
import fresh_tomatoes

toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life",
    "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=vwyZH85NQC4",
    "John Lasseter",
    ["Tom Hanks", "Tim Allen", "Don Rickles", "Jim Varney"],
    1995)

avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY",
    "James Cameron",
    ["Sam Worthington", "Stephen Lang", "Sigourney Weaver"],
    2009)

pulp_fiction = media.Movie(
    "Pulp Fiction",
    "Gangsters in LA meet divine intervention",
    "https://upload.wikimedia.org/wikipedia/en/8/82/Pulp_Fiction_cover.jpg",
    "https://www.youtube.com/watch?v=s7EdQ4FqbhY",
    "Quentin Tarantino",
    ["John Travolta", "Samuel L. Jackson", "Uma Thurman", "Bruce Willis"],
    1994)

lego_movie = media.Movie(
    "The Lego Movie",
    "An unspecial construction worker tries to save the world",
    "https://upload.wikimedia.org/wikipedia/en/1/10/The_Lego_Movie_poster.jpg",
    "https://www.youtube.com/watch?v=fZ_JOBCLF-I",
    "Phil Lord",
    ["Chris Pratt", "Will Ferrell", "Elizabeth Banks", "Will Arnett"],
    2014)

jurassic_world = media.Movie(
    "Jurassic World",
    "Things go bad at a theme park filled with live dinosaurs",
    "https://upload.wikimedia.org/wikipedia/en/6/6e/Jurassic_World_poster.jpg",
    "https://www.youtube.com/watch?v=RFinNxS5KN4",
    "Colin Trevorrow",
    ["Chris Pratt", "Bryce Dallas Howard", "Vincent D'Onofrio", "Ty Simpkins"],
    2015)

inside_out = media.Movie(
    "Inside Out",
    "A young girls emotions deal with an impending disaster after moving to San Francisco",
    "https://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_%282015_film%29_poster.jpg",
    "https://www.youtube.com/watch?v=seMwpP0yeu4",
    "Pete Docter",
    ["Amy Poehler", "Phyllis Smith", "Bill Hader", "Lewis Black", "Mindy Kaling"],
    2015)

movies = [toy_story, avatar, pulp_fiction, lego_movie, jurassic_world, inside_out]
fresh_tomatoes.open_movies_page(movies)
