from citiesList import CitiesList

from flask import Flask, render_template

app = Flask(__name__)

cities = CitiesList()


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/Map/<root_city_name>')
def show_track_from(root_city_name):
    track = cities.get_best_track_from(root_city_name)

    return render_template("showMap.html", track=track)


@app.route('/Map')
def show_best_track():
    best_track = cities.get_best_track()

    return render_template("showMap.html", track=best_track)


if __name__ == '__main__':
    app.run()
