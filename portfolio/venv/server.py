from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)


def write_to_txt_file(data):
    with open('database/data.txt', mode='a') as database:
        file = database.write(f'{ data["email"] },{ data["subject"] },{ data["message"] }\n')


def write_to_csv_file(data):
    with open('database/data.csv', newline='', mode='a') as database:
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([data["email"], data["subject"], data["message"]])


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()

            # write_to_txt_file(data)
            write_to_csv_file(data)

            return render_template('thankyou.html', data=data)
        except:
            return 'An error occurred while saving into database.'
    else:
        return 'Something went wrong!'
