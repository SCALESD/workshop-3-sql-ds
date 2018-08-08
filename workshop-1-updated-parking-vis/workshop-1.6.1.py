#!/usr/bin/python

# Plotting map points on Google Maps with interaction
#
# Run: bokeh serve workshop-1.6.py

from config import get_config
from constants import DEFAULT_ZOOM, SAN_DIEGO_COORDINATE, GASLAMP_BOUNDING_BOX
import datetime
from gmapplot import GoogleMapPlot
from parking.meter import Meter
from parking.transaction import Transaction


# Google requires you obtain and enable an API key:
#
#     https://developers.google.com/maps/documentation/javascript/get-api-key
#
# Replace the value in config.json below with your personal API key:
config = get_config()
plot = GoogleMapPlot(
    api_key=config['GoogleMapsAPIKey'],
    lat=SAN_DIEGO_COORDINATE[0],
    lng=SAN_DIEGO_COORDINATE[1],
    type="roadmap",
    zoom=DEFAULT_ZOOM
)


#poles = Meter.poles_in_gaslamp()
draw_xy = []

datasource = plot.draw_points_with_circle_glyph(draw_xy, attrs={'fill_color': 'blue', 'size': 3})
print("IN")

def update_plot(day):
    date = (datetime.datetime(2017, 1, 1) + datetime.timedelta(day - 1)).strftime('%Y-%m-%d')

    # Pass 1: Grab the transactions
    transactions = Transaction.transactions(date, GASLAMP_BOUNDING_BOX)
    print("Found {0} transactions...".format(len(transactions)))
    poles = set(map(lambda tran: (tran.pole['pole_id'], tran.pole['latitude'], tran.pole['longitude']), transactions))

    # Pass 2: Grab the poles
#     poles = Transaction.transaction_poles(date, GASLAMP_BOUNDING_BOX)
#     print("Found {0} poles...".format(len(poles)))
#     poles = map(lambda tran: list(tran.pole.values()), poles)

    draw_xy = [(pole[1], pole[2]) for pole in poles]

    plot.update(datasource, draw_xy)

plot.add_slider(start=1, end=365, step=1, init=1, title="Day", callback=update_plot)
update_plot(day=1)  # Slider is initialized to Day 1, make sure plot reflects that

plot.show()
