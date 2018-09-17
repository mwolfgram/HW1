## HW 1
## SI 364 F18
## 1000 points
## matthew wolfgram

#################################

## List below here, in a comment/comments, the people you worked with on this assignment AND any resources you used to find code (50 point deduction for not doing so). If none, write "None".
## Resources: I worked with Sam Lu, and also used the assigned readings and lecture code.

## [PROBLEM 1] - 150 points
## Below is code for one of the simplest possible Flask applications. Edit the code so that once you run this application locally and go to the URL 'http://localhost:5000/class', you see a page that says "Welcome to SI 364!"

import requests
import json

from flask import Flask , request #don't forget request here!!!
app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_to_you():
    return 'Hello!'

@app.route('/class')
def c_lass():
    return 'Welcome to SI 364!'

## [PROBLEM 2] - 250 points
## Edit the code chunk above again so that if you go to the URL 'http://localhost:5000/movie/<name-of-movie-here-one-word>' you see a big dictionary of data on the page. For example, if you go to the URL 'http://localhost:5000/movie/ratatouille', you should see something like the data shown in the included file sample_ratatouille_data.txt, which contains data about the animated movie Ratatouille. However, if you go to the url http://localhost:5000/movie/titanic, you should get different data, and if you go to the url 'http://localhost:5000/movie/dsagdsgskfsl' for example, you should see data on the page that looks like this:

@app.route('/movie/<name>')
def mov(name):
    url = "http://itunes.apple.com/search"
    params = {'media': 'movie', 'term': name}
    data_grab = requests.get(url, params = params)
    json_data = json.loads(data_grab.text)
    return data_grab.text #change this to json_data??

# {
#  "resultCount":0,
#  "results": []
# }

## You should use the iTunes Search API to get that data.
## Docs for that API are here: https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/
## Of course, you'll also need the requests library and knowledge of how to make a request to a REST API for data.

## Run the app locally (repeatedly) and try these URLs out!

## [PROBLEM 3] - 250 points

## Edit the above Flask application code so that if you run the application locally and got to the URL http://localhost:5000/question, you see a form that asks you to enter your favorite number.
## Once you enter a number and submit it to the form, you should then see a web page that says "Double your favorite number is <number>". For example, if you enter 2 into the form, you should then see a page that says "Double your favorite number is 4". Careful about types in your Python code!
## You can assume a user will always enter a number only.

@app.route('/question')
def entry():
    q = """<DOCTYPE html>
<html>
<body>
<div>
<form action = "/doubled" method = "GET">
    enter your favorite number:
    <input type= "text" name = "number" value = "0">
    <br> <br>
    <input type = "submit" value = "Submit"
<div>
</form>
</htm>
"""

    return q


@app.route('/doubled', methods = ['POST', 'GET'])
def double():
    if request.method == 'GET':
        user_number = request.args.get('number', '')
        x2_number = int(user_number)
        return "double your favorite number is {}.".format(str(x2_number*2))

## [PROBLEM 4] - 350 points

## Come up with your own interactive data exchange that you want to see happen dynamically in the Flask application, and build it into the above code for a Flask application, following a few requirements.

## You should create a form that appears at the route: http://localhost:5000/problem4form

## Submitting the form should result in your seeing the results of the form on the same page.

## What you do for this problem should:
# - not be an exact repeat of something you did in class
# - must include an HTML form with checkboxes and text entry
# - should, on submission of data to the HTML form, show new data that depends upon the data entered into the submission form and is readable by humans (more readable than e.g. the data you got in Problem 2 of this HW). The new data should be gathered via API request or BeautifulSoup.

# You should feel free to be creative and do something fun for you --
# And use this opportunity to make sure you understand these steps: if you think going slowly and carefully writing out steps for a simpler data transaction, like Problem 1, will help build your understanding, you should definitely try that!

# You can assume that a user will give you the type of input/response you expect in your form; you do not need to handle errors or user confusion. (e.g. if your form asks for a name, you can assume a user will type a reasonable name; if your form asks for a number, you can assume a user will type a reasonable number; if your form asks the user to select a checkbox, you can assume they will do that.)

# Points will be assigned for each specification in the problem.

@app.route('/problem4form', methods = ['POST', 'GET'])
def prelim():

    f = """<DOCTYPE html>
<html>
<h1> car brands and models </h1>
<body>
<form action = "/brandmodelinfo" method = "GET">
<div>
    enter a model year:
    <input type = "text" name = "year" value = "0"
    <br><br>
    <br><br>
    pick a manufacturer:
    <br> <br>
    <input type= "radio" name = "make" value = "Acura"> Acura <br>
    <input type= "radio" name = "make" value = "Aston Martin"> Aston Martin <br>
    <input type= "radio" name = "make" value = "Audi"> Audi <br>
    <input type= "radio" name = "make" value = "BMW"> BMW <br>
    <input type= "radio" name = "make" value = "Chevrolet"> Chevrolet <br>
    <input type= "radio" name = "make" value = "Dodge"> Dodge <br>
    <input type= "radio" name = "make" value = "Ferrari"> Ferrari <br>
    <input type= "radio" name = "make" value = "Fiat"> Fiat <br>
    <input type= "radio" name = "make" value = "Ford"> Ford <br>
    <input type= "radio" name = "make" value = "Honda"> Honda <br>
    <input type= "radio" name = "make" value = "Infiniti"> Infiniti <br>
    <input type= "radio" name = "make" value = "Lamborghini"> Lamborghini <br>
    <input type= "radio" name = "make" value = "Lexus"> Lexus <br>
    <input type= "radio" name = "make" value = "Maserati"> Maserati <br>
    <input type= "radio" name = "make" value = "Mazda"> Mazda <br>
    <input type= "radio" name = "make" value = "McLaren"> McLaren <br>
    <input type= "radio" name = "make" value = "Mercedes-Benz"> Mercedes-Benz <br>
    <input type= "radio" name = "make" value = "Nissan"> Nissan <br>
    <input type= "radio" name = "make" value = "Porsche"> Porsche <br>
    <input type= "radio" name = "make" value = "Subaru"> Subaru <br>
    <input type= "radio" name = "make" value = "Tesla"> Tesla <br>
    <input type= "radio" name = "make" value = "Toyota"> Toyota <br>
    <input type= "radio" name = "make" value = "Volkswagen"> Volkswagen <br>
    <input type= "radio" name = "make" value = "Volvo"> Volvo <br>
    <br> <br>
    <input type = "submit" value = "Submit"
</div>
</form>
</html>
"""
    return f

@app.route('/brandmodelinfo', methods = ['POST', 'GET'])
def getmakeinfo():
    if request.method == 'GET':
        arguments = request.args
        chosen_make = arguments.get("make")
        year = arguments.get('year') #what does this correspond to?

        baseurl = 'https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformakeyear/make/{}/modelyear/{}?format=json'.format(chosen_make, year)
        response = requests.get(baseurl)
        data = json.loads(response.text)

        model_list = []
        for x in data['Results']:
            for dict in x:
                try:
                    str_model_name = str(x["Model_Name"])
                    if str_model_name not in model_list:
                        model_list.append(str_model_name)

                except:
                    continue

        big_lst = range(len(model_list))

        big_str = " "
        for x in big_lst:
            if x != big_lst[-1]:
                element = str(model_list[x])
                big_str += element + "," + "\n"
            if x == big_lst[-1]:
                element = str(model_list[x])
                big_str += element + "\n"

        return "<h1> {} Models for {}: </h1> {}".format(chosen_make, year, big_str)


if __name__ == '__main__':
    app.run()
