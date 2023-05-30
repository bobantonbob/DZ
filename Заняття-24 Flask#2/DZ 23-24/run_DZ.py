from flask import Flask, request, render_template
from worker import working_route, working

app = Flask(__name__)
app.debug = True



@app.route("/")
def start():
    return render_template("index.html", working=working)



app.register_blueprint(working_route)

app.run()