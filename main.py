
import requests,os

from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime,timedelta
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "LON"
data_manager=DataManager()
flight_search=FlightSearch()
sheet_data=data_manager.get_destination_data()

for prices in sheet_data:
    prices["iataCode"]=flight_search.get_destination_code(prices["city"])
    data_manager.update_destination_codes(prices["id"],prices["iataCode"])

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:

    flight=flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    if flight.price<destination["lowestPrice"]:
        NotificationManager(message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}.")
        