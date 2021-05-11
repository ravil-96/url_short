# Coding Challenge: URL Shortener - Django

A django....

# Description & Task Requirements

Users can enter a URL and get shortened one back which redirects to their original URL. 

- [x] Users should be able to enter a url into an input box on your website's front page 
- [ ] Your backend will then generate a shortened path at which a User can access their url 
- [x] You must implement Python in some capacity in this application 
- [ ] Store this shortened path and it's longer counterpart in a database 
- [x] No login should be required to create a shortened URL 
- [ ] If User tries to access your website with a path you have stored in your database, they should get rerouted to the URL it relates to 
- [ ] If User tries to access your website with a path you do not have stored in your database, they should get rerouted to the homepage where they can create a new short URL 

# Installation & usage

### For our app to be run on your local machine:

Clone this repo and navigate to the root directory of this repo.   
`pipenv shell`   
`pipenv install`   
`python manage.py runserver`   

It should load on http://127.0.0.1:8000/    

To see our test suite:     
`pipenv run test`     

# Technologies
django

# Process
1. Create repo and link to local file
2. Bootstrap a django project using `django-admin startproject app`

# Bugs 
- [x] no bugs here!

# Wins & Challenges 

## Wins 
- Form works!

## Challenges 
- 
