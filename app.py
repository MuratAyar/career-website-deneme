from flask import Flask, render_template, jsonify

app = Flask(__name__, template_folder='template')

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'İstanbul',
        'salary': '10,000 TL'
    },
    {
        'id': 2,
        'title': 'Full Stack',
        'location': 'Ankara',
        'salary': '20,000 TL'
    },
    {
        'id': 3,
        'title': 'Goal Keeper',
        'location': 'İzmir',
        'salary': '30,000 TL'
    },
]


@app.route('/')
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Muratia')

@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
