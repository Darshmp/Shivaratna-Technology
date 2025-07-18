from flask import Flask, render_template, request  # Added request import

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/it-services')
def it_services():
    return render_template('it_services.html')

@app.route('/digital-marketing')
def digital_marketing():
    return render_template('digital_marketing.html')

@app.route('/ai-ml')
def ai_ml():
    return render_template('ai_ml.html')

@app.route('/mechanical-design')
def mechanical_design():
    return render_template('mechanical_design.html')

@app.route('/civil-planning')
def civil_planning():
    return render_template('civil_planning.html')

@app.route('/data-analytics')
def data_analytics():
    return render_template('data_analytics.html')

@app.route('/company-projects')
def company_projects():
    service = request.args.get('service', '')
    return render_template('company_projects.html', service=service)

@app.route('/student-projects')
def student_projects():
    service = request.args.get('service', '')
    return render_template('student_projects.html', service=service)

if __name__ == '__main__':
    app.run(debug=True)