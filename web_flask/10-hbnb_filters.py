"""10-hbnb_filters.py"""
import sys
sys.path.append('D:\\holbertonschool\\AirBnB_clone_v2')

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity


app = Flask(__name__)


@app.teardown_appcontext
def close(self):
    """ Close Session """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Get All States"""
    states = storage.all(State)
    cities = storage.all(City)
    amenities = storage.all(Amenity)
    return render_template('10-hbnb_filters.html', states=states, cities=cities, amenities=amenities)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")