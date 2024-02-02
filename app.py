from flask import Flask, render_template,request
from weather import main as get_weather 


app = Flask(__name__)


headquarter_address = {}
headquarter_address['Street'] = 'Brüsseler Platz 1'
headquarter_address['City'] = 'Essen'
headquarter_address['Postcode'] = '45131'
headquarter_address['Country'] = 'Germany'
headquarter_address['admin1'] = 'North Rhine-Westphalia'


#Single route for flask app, if include_maximum=true is provided then additional values are returned
@app.route("/headquarter-weather")
def index():
    include_maximum = request.args.get('include_maximum')
    if include_maximum is not None:
        include_maximum = include_maximum.lower() in ['true']
    data = get_weather(headquarter_address,include_maximum)
    return render_template('index.html',data = data)



if __name__ == '__main__':
    app.run(debug=True)

