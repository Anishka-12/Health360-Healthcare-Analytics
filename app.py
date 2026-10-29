from flask import Flask, render_template

app = Flask(__name__)

# Updated Tableau Public links supplied for the Health360 project.
DASHBOARD_URL = (
    'https://public.tableau.com/views/Health360-Healthcare-Analytics/'
    'SmartHealthcareAnalyticsPatientRiskLifestyleInsights'
    '?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link'
)
STORY_URL = (
    'https://public.tableau.com/views/Health360-Healthcare-Analytics-Story/'
    'SmartHealthcareAnalyticsPatientRiskLifestyleInsights'
    '?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link'
)


@app.route('/')
def home():
    return render_template('index.html', page='home', title='Home')


@app.route('/about')
def about():
    return render_template('index.html', page='about', title='About')


@app.route('/dashboard')
def dashboard():
    return render_template(
        'index.html', page='dashboard', title='Dashboard', tableau_url=DASHBOARD_URL
    )


@app.route('/story')
def story():
    return render_template(
        'index.html', page='story', title='Story', tableau_url=STORY_URL
    )


@app.route('/faq')
def faq():
    return render_template('index.html', page='faq', title='FAQ')


if __name__ == '__main__':
    app.run(debug=True)
