import json

from flask import Flask , render_template, jsonify
import boto3
import json
import boto_dynamo


app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")
@app.route('/sensors')
def sensors():
    #Get items here
    # return jsonify(boto_dynamo.get_items())
    # return boto_dynamo.get_items()
    temps = boto_dynamo.get_items()
    last_item = temps[-1]
    print(last_item)
    return render_template("sensors.html", data=temps, last=last_item)


if __name__ == "__main__":
    app.run()