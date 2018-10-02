import fresh_tomatoes
import media

# Creating multiple instances of the Movie class
avatar = media.Movie("Avatar",
                     "http://www.gstatic.com/tv/thumb/v22vodart/3542039/p3542039_v_v8_ac.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

matrix = media.Movie("Matrix",
                     "http://www.gstatic.com/tv/thumb/v22vodart/22804/p22804_v_v8_as.jpg",
                     "https://www.youtube.com/watch?v=m8e-FF8MsqU")

forrest_gump = media.Movie("Forrest Gump",
                           "http://www.gstatic.com/tv/thumb/v22vodart/15829/p15829_v_v8_ab.jpg",
                           "https://www.youtube.com/watch?v=bLvqoHBptjg")

inception = media.Movie("Inception",
                        "http://www.gstatic.com/tv/thumb/v22vodart/7825626/p7825626_v_v8_ad.jpg",
                        "https://www.youtube.com/watch?v=d3A3-zSOBT4")

shutter_island = media.Movie("Shutter Island",
                             "http://www.gstatic.com/tv/thumb/v22vodart/3531967/p3531967_v_v8_am.jpg",
                             "https://www.youtube.com/watch?v=qdPw9x9h5CY")

catch_me = media.Movie("Catch me if you can",
                       "http://www.gstatic.com/tv/thumb/v22vodart/31064/p31064_v_v8_aa.jpg",
                       "https://www.youtube.com/watch?v=71rDQ7z4eFg")
# create a list of movie instances
movies = [avatar, matrix, forrest_gump, inception, shutter_island, catch_me]

# create the HTML page using movies list
fresh_tomatoes.open_movies_page(movies)
