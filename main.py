from model import data
from controller.movies import Movies

def main():

    main_movie_list = []
    main_movie_list.extend(data.films)
    print(len(main_movie_list))
    for i in main_movie_list:
        print(i)

    """movies = Movies(main_movie_list[:])
    print(movies)"""
    







if __name__ == '__main__':
    main()