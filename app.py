from flask import Flask, render_template, jsonify

app = Flask(__name__, template_folder='template')

JOBS = [
    {
      'id': 1,
      'title': 'Volunteer BTK Internship',
      'location': 'Ankara, Turkey',
      'position': 'Software Developer',
      'description': 'We automatically detect the URLs in the notifications received by the USOM department, pass them through malware control, collect the necessary evidence through various URL Scan APIs and forward them to higher authorities for the removal of the site. The project is where we collect the essential evidence for removing a site.',
    },
    {
      'id': 2,
      'title': 'Compulsory Turkcell Internship',
      'location': 'Remote',
      'position': 'Software Developer',
      'description': 'I worked in a software developer team which is dedicated to update and upgrade the old version of customer service application of Turkcell on a large scale.My job was coding the unit testings for both old and new version of our applications services and checking if there is any bugs and if there is any, we could easily locate and patch them.',
    },
    {
      'id': 3,
      'title': 'Long Term Turkcell Internship',
      'location': 'Remote',
      'position': 'Software Developer',
      'description': 'I am currently working in this position...'
    },
]


@app.route('/')
def hello_world():
  return render_template('home.html', jobs=JOBS)

@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)

@app.route('/contact')
def contact():
  return render_template('contact.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
