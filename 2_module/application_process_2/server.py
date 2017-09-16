from flask import Flask, render_template, redirect, request, session
import queries


app = Flask(__name__)


@app.route('/')
def route_index():
    return render_template('index.html')


@app.route('/mentors')
def route_mentors():
    mentors = queries.get_mentor_data()
    return render_template('mentors.html', mentors=mentors)


@app.route('/all-school')
def route_all_school():
    mentors = queries.get_all_school()
    for row in mentors:
        if row['first_name'] == None and row['last_name'] == None:
            row['first_name'] = "No data"
            row['last_name'] = "No data"
    return render_template('allschool.html', mentors=mentors)


@app.route('/mentors-by-country')
def route_mentors_by_country():
    mentors = queries.get_mentors_by_country()
    return render_template('mentors_by_country.html', mentors=mentors)


@app.route('/contacts')
def route_contacts():
    mentors = queries.get_contacts()
    for row in mentors:
        if row['first_name'] == None and row['last_name'] == None:
            row['first_name'] = "No data"
            row['last_name'] = "No data"
    return render_template('contacts.html', mentors=mentors)


@app.route('/applicants')
def route_applicants():
    applicants = queries.get_applicants()
    return render_template('applicants.html', applicants=applicants)


@app.route('/applicants-and-mentors')
def route_applicants_mentors():
    applicants = queries.get_applicants_mentors()
    for row in applicants:
        if row['first_name'] == None and row['last_name'] == None:
            row['first_name'] = "No data"
            row['last_name'] = "No data"
    return render_template('applicants_mentors.html', applicants=applicants)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
