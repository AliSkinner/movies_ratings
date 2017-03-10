# Movies/Ratings

## Tech used

* Python 2.7
* Django 1.10.5
* LESS
* Bootstrap 3
* Gulp
* HTML5
* LESS
* Git

## About

* App that pulls movies from BBC iPlayer API and gets their ratings from TheMovieDB.


## Running the app

```
cd movies_ratings
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
npm install
gulp
export THE_MOVIE_DB_KEY=[YOUR_API_KEY]
cd movies_ratings
python manage.py migrate
python manage.py runserver
```
Open `127.0.0.1:8000` in your browser.
