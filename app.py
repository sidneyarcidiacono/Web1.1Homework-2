from flask import Flask, request, render_template
import random

app = Flask(__name__)

def sort_letters(message):
    """A helper method to sort the characters of a string in alphabetical order
    and return the new string."""
    return ''.join(sorted(list(message)))


@app.route('/')
def homepage():
    """A homepage with handy links for your convenience."""
    return render_template('home.html')

@app.route('/froyo')
def choose_froyo():
    """Shows a form to collect the user's Fro-Yo order."""
    return render_template('froyo_form.html')

@app.route('/froyo_results')
def show_froyo_results():
    """Shows the user what they ordered from the previous page."""

    context = {
        'users_toppings':request.args.get('toppings').split(' '),
        'users_froyo_flavor': request.args.get('flavor')
    }

    return render_template('froyo_results.html', **context)

@app.route('/favorites')
def favorites():
    """Shows the user a form to choose their favorite color, animal, and city."""
    return """
    <form action="/favorites_results" method="GET">
        What is your favorite color? <br/>
        <input type="text" name="color"> <br/>
        <label for="animal">What is your favorite animal?</label> <br/>
        <input type="text" name="animal"> <br/>
        <label for="city">What is your favorite city?</label> <br/>
        <input type="text" name="city"> <br/>
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/favorites_results')
def favorites_results():
    """Shows the user a nice message using their form results."""
    user_fav_color = request.args.get('color')
    user_fav_animal = request.args.get('animal')
    user_fav_city = request.args.get('city')
    return f"Wow, I didn't know {user_fav_color} {user_fav_animal}s lived in {user_fav_city}!"

@app.route('/secret_message')
def secret_message():
    """Shows the user a form to collect a secret message. Sends the result via
    the POST method to keep it a secret!"""
    return """
    <form action="/message_results" method="POST">
        Tell me your secret message... </br>
        <input type="text" name="message"> </br>
        <input type="submit" value="Give me your secrets">
    </form>
    """

@app.route('/message_results', methods=['POST'])
def message_results():
    """Shows the user their message, with the letters in sorted order."""
    message = request.form.get('message')
    sorted_message = sort_letters(message)
    return f"Here's your secret message! </br> {sorted_message}"

@app.route('/calculator')
def calculator():
    """Shows the user a form to enter 2 numbers and an operation."""
    return render_template('calculator_form.html')

@app.route('/calculator_results')
def calculator_results():
    """Shows the user the result of their calculation."""

    result = 0
    operation = request.args.get('operation')
    user_first_number = int(request.args.get('operand1'))
    user_second_number = int(request.args.get('operand2'))

    if operation == 'add':
        result = user_first_number + user_second_number
    elif operation == 'subtract':
        result = user_first_number - user_second_number
    elif operation == 'multiply':
        result = user_first_number * user_second_number
    else:
        result = user_first_number / user_second_number

    context = {
        'user_first_number': user_first_number,
        'user_second_number': user_second_number,
        'operation': operation,
        'result': result
        }

    return render_template('calculator_results.html', **context)


# List of compliments to be used in the `compliments_results` route (feel free
# to add your own!)
# https://systemagicmotives.com/positive-adjectives.htm
list_of_compliments = [
    'awesome',
    'beatific',
    'blithesome',
    'conscientious',
    'coruscant',
    'erudite',
    'exquisite',
    'fabulous',
    'fantastic',
    'gorgeous',
    'indubitable',
    'ineffable',
    'magnificent',
    'outstanding',
    'propitioius',
    'remarkable',
    'spectacular',
    'splendiferous',
    'stupendous',
    'super',
    'upbeat',
    'wondrous',
    'zoetic'
]

@app.route('/compliments')
def compliments():
    """Shows the user a form to get compliments."""
    return render_template('compliments_form.html')

@app.route('/compliments_results')
def compliments_results():
    """Show the user some compliments."""
    wants_compliments = request.args.get('wants_compliments')
    users_name = request.args.get('users_name')
    user_compliments = ''
    num_compliments = int(request.args.get('num_compliments'))
    return_compliments = random.sample(list_of_compliments, k=num_compliments)

    context = {
        'users_name': users_name,
        'compliments': compliments,
        'num_compliments': num_compliments,
        'wants_compliments': wants_compliments,
        'list_of_compliments': list_of_compliments,
        'return_compliments': return_compliments
    }

    return render_template('compliments_results.html', **context)


if __name__ == '__main__':
    app.run()
