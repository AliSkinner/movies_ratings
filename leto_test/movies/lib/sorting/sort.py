"""module to house sorting functions for movies"""

def sort_movies(movies, sort_by):
    """sorts list of movies by second arg"""
    if sort_by == 'recent':
        movies.sort(key=lambda x: x.get('available_from'), reverse=True)
    elif sort_by == 'old':
        movies.sort(key=lambda x: x.get('available_from'))
    elif sort_by == 'high':
        movies.sort(key=lambda x:x.get('rating'), reverse=True)
    elif sort_by == 'low':
        movies.sort(key=lambda x:x.get('rating'))
    return movies
