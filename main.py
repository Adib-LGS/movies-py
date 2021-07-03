from model import data
from controller.movies import Movies
from controller.sortmovies import SortMovies
from controller.dvdmovies import DVDMovies
from controller.vhfmovies import VHFMovies
from controller.library import Library

#def main():

lib = Library()
movies = lib.movies

print(movies)

#if __name__ == "__main__":
#    main()