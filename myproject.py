from flask import Flask, render_template

app = Flask(__name__)

#index route
@app.route('/')
def index():
     return render_template('about.html')


#about page
@app.route('/about')
def about():
    return render_template('about.html')

#service
@app.route('/service')
def service():
    return render_template('service.html')

#clients
@app.route('/client')
def client():
   return render_template('client.html')

#careers
@app.route('/career')
def career():
   return render_template('career.html')

#contact
@app.route('/contact')
def contact():
   return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)

