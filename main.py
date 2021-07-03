from model import data
from controller.movies import Movies
from controller.sortmovies import SortMovies

def main():

    main_movie_list = SortMovies(data.films)
    print(main_movie_list.generate_movies_by_type())





if __name__ == "__main__":
    main()