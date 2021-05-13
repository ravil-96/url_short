# Coding Challenge: URL Shortener - Django

A django app designed to make your urls pretty and less of a hassle!

## Description & Task Requirements

Users can enter a URL e.g "https://www.hello-i-am-a-long-url.com" and get shortened one back e.g. "https://127.0.0.1:8000/UDHYX" which redirects to their original URL. 

- [x] Users should be able to enter a url into an input box on your website's front page 
- [x] Your backend will then generate a shortened path at which a User can access their url 
- [x] You must implement Python in some capacity in this application 
- [x] Store this shortened path and it's longer counterpart in a database 
- [x] No login should be required to create a shortened URL 
- [x] If User tries to access your website with a path you have stored in your database, they should get rerouted to the URL it relates to 
- [x] If User tries to access your website with a path you do not have stored in your database, they should get rerouted to the homepage where they can create a new short URL 

# Installation & usage

### For our app to be run on your local machine:

Clone this repo and navigate to the root directory of this repo.   
`pipenv shell`   
`pipenv install`   
`cd url_shortener`   
`python manage.py runserver`   

It should load on http://127.0.0.1:8000/        

# Technologies
django

# Process
1. Create repo and link to local file
2. Bootstrap a django project using `django-admin startproject app`
3. Set up root route '/' and '/<str:id>' for dynamic id 
4. Create a form with templating to ask users for URL and on submit POST URL to database and return a short URL path 
5. Create out of bounds routes and error handling
6. Styling and UI updates
7. Attempt to deploy to Heroku
8. Finalise and complete task requirements 

# Bugs 
- [x] there may be environment issues - delete and reinstall Pipfile.lock!

# Wins & Challenges 

## Wins 
- Form works!
- Random string generator is an easy and straightforward way to generate a short URL path 

## Challenges 
- Deployment via Heroku with Django - static files issues
- Redirecting link to new page without 'https://'
- Difficulties setting up test suite!
