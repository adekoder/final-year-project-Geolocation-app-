from flask import render_template, request, jsonify, json
from . import main
from ..models import Location


def location_schema(locations):
    location_data = []
    for location in locations:
        location_data.append({
            'location_id': location.location_id,
            'location_name': location.location_name,
            'coordinate': location.coordinate,
        })
    return jsonify(locations=location_data), 200

@main.route('/')
def index():
    return render_template('main/index.html')

@main.route('/search', methods=['GET'])
def search():
    return render_template('main/search.html')

@main.route('/explore')
def explore():
    return render_template('main/explore.html')

@main.route('/locations', methods=['POST'])
def location():
    data =  request.get_json(force=True)
    location_name = data['location_name']
    query_param = "%{}%".format(location_name)
    print(query_param)
    locations = Location.query.filter(Location.location_name.like(query_param)).all()
    return location_schema(locations)

@main.route('/map/<string:coords>')
def show_map(coords):
    return render_template('main/maps.html', coords=coords)
 