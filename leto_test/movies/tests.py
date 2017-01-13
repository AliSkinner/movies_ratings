import datetime
from django.test import TestCase
from movies.lib.sorting.sort import sort_movies

class SortingTestCase(TestCase):
    """test sorting functionality"""
    def setUp(self):
        self.movie_1 = {
            'rating': 5.1,
            'available_from': datetime.datetime(2017, 1, 12, 0, 0),
            'title': u'The Other Man',
            'poster': 'http://ichef.bbci.co.uk/images/ic/480x270/p01h7zq9.jpg',
            'release_date': datetime.datetime(2008, 12, 25, 0, 0),
            'available_until': datetime.datetime(2017, 2, 11, 0, 0),
            'expire_string': u'29 days left to watch',
            'synopsis': u'Drama. Following the death of his wife, grieving \
                husband Peter finds evidence of adultery.',
            'run_time': '01:25:00'
        }
        self.movie_2 = {
            'rating': 6.3,
            'available_from': datetime.datetime(2017, 1, 05, 0, 0),
            'title': u'The Man Who Fell to Earth',
            'poster': 'http://ichef.bbci.co.uk/images/ic/480x270/p01jxw7c.jpg',
            'release_date': datetime.datetime(1976, 3, 18, 0, 0),
            'available_until': datetime.datetime(2017, 1, 30, 0, 0),
            'expire_string': u'17 days left to watch',
            'synopsis': u'Fantasy in which an alien visits Earth in search of \
                water for his dying planet.',
            'run_time': '02:20:00'
        }
        self.movie_3 = {
            'rating': 7,
            'available_from': datetime.datetime(2017, 1, 10, 0, 0),
            'title': u'Walesa: Man of Hope',
            'poster': 'http://ichef.bbci.co.uk/images/ic/480x270/p04my96t.jpg',
            'release_date': datetime.datetime(2013, 9, 5, 0, 0),
            'available_until': datetime.datetime(2017, 2, 9, 0, 0),
            'expire_string': u'27 days left to watch',
            'synopsis': u'Biopic of the Polish trade union leader Lech Walesa.',
            'run_time': '01:54:00'
        }

        self.movies = [
            self.movie_1,
            self.movie_2,
            self.movie_3
        ]

    def test_sort_recent(self):
        """test sorting by most recent"""
        self.assertEqual(
            sort_movies(self.movies, 'recent')[0],
            self.movie_1
        )

    def test_sort_old(self):
        """test sorting by oldest"""
        self.assertEqual(
            sort_movies(self.movies, 'old')[0],
            self.movie_2
        )

    def test_sort_rating_high(self):
        """test sorting by highest rating"""
        self.assertEqual(
            sort_movies(self.movies, 'high')[0],
            self.movie_3
        )

    def test_sort_rating_low(self):
        """test sorting by lowest rating"""
        self.assertEqual(
            sort_movies(self.movies, 'low')[0],
            self.movie_1
        )
