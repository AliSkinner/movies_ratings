# Code Test for Leto

Ali Skinner: <awskinner26@gmail.com>

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

* I decided to use Django, as I am familiar with the framework and ecosystem.
* I chose to save time by using a generic view.
* As I only want to show fresh data from iPlayer, I decided not to to use Django's models/db, instead returning dictionaries of movie data. An alternative approach could have been to leverage Python's object classes. 
* I decided to use Django's local memory caching to save on the expensive api calls. The BBC is relatively quick, but iteration through 25 or so calls to The Movie DB is quite costly. The cache times out after 5 minutes, allowing a request to the page to fetch fresh data.
* I've opted for Gulp to handle compilation/minification/obfuscation of static assets.
* I've used Bootstrap pretty heavily throughout. It always surprises me how much styling is taken care of with little more than an additional css class!
* Some basic tests are in place to cover the movie sorting function.


## Running the app
Setup uses __*virtualenvwrapper*__

```
cd leto_code_test
mkvirtualenv code-test
workon code-test
pip install -r requirements.txt
npm install
gulp
export THE_MOVIE_DB_KEY=f6f6ac003f3b15245000d5b2ab33d706
cd leto_test
python manage.py migrate
python manage.py runserver
```
Open `127.0.0.1:8000` in your browser.
