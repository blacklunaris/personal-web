"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
from app import app
from flask import Flask
from flask import render_template, request, redirect, url_for, flash
from app import mail
from flask_mail import Message 
from flask_wtf import FlaskForm
from wtforms import StringField,Form,TextField,TextAreaField, validators,SubmitField
from wtforms.validators import InputRequired

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')
@app.route('/projects/')
def projects():
    """Render website's home page."""
    return render_template('projects.html')

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Personal Projects")
class contactForm(Form):
    name=StringField('name',validators=[InputRequired()])
    email=StringField('email',validators=[InputRequired()])
    subject=StringField('subject',validators=[InputRequired()])
    message=StringField('message',validators=[InputRequired()])
    @app.route('/contact',methods=('GET','POST'))
    def contact():
        form=contactForm(request.form)
        if request.method=='POST':
            sender=(request.form['name'],request.email['email'])
            subject=request.form['subject']
            msg=Message(subject,sender,recipients=["to@example.com"])
        
            msg.body=request.form['message']
    
            mail.send(msg)
            flash('Your email was sent successfully')
            return redirect(url_for('/'))
        
        return render_template('contact.html',form=form)
    
###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
