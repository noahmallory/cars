from flask import Flask, render_template

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Pictures page route
@app.route('/pictures')
def pictures():
    return render_template('pictures.html')

# About page route
@app.route('/about')
def about():
    return render_template('about.html')
    
@app.route('/cars')
def cars():
    return render_template('porsche.html')


@app.route('/bikes')
def ferrari():    
    return render_template('ferrari.html')
@app.route('/trucks')
def lamborghini():    
    return render_template('lamborghini.html')

if __name__ == '__main__':
    app.run(debug=True)
