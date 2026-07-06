class Movie:
    def __init__(self, title, genre, director, year):
        self.__title = title
        self.__genre = genre
        self.__director = director
        self.__year = year

    def get_title(self):
        return self.__title

    def get_genre(self):
        return self.__genre

    def get_director(self):
        return self.__director

    def get_year(self):
        return self.__year


class StreamingService:
    def __init__(self, name):
        self.__name = name
        self.__catalog = {}

    def get_name(self):
        return self.__name

    def get_catalog(self):
        return self.__catalog

    def add_movie(self, movie):
        self.__catalog[movie.get_title()] = movie

    def delete_movie(self, title):
        if title in self.__catalog:
            del self.__catalog[title]


class StreamingGuide:
    def __init__(self):
        self.__streaming_services = []

    def add_streaming_service(self, service):
        self.__streaming_services.append(service)

    def delete_streaming_service(self, name):
        for service in self.__streaming_services:
            if service.get_name() == name:
                self.__streaming_services.remove(service)
                break

    def who_streams_this_movie(self, title):
        services = []
        movie_year = None

        for service in self.__streaming_services:
            catalog = service.get_catalog()

            if title in catalog:
                movie = catalog[title]
                services.append(service.get_name())
                movie_year = movie.get_year()

        if len(services) == 0:
            return None

        return {
            "title": title,
            "year": movie_year,
            "services": services
        }