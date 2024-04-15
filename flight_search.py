
import requests,os
from flight_data import FlightData

API_KEY=os.environ.get("API_KEY")
TEQUILA_ENDPOINT=os.environ.get("TEQUILA_ENDPOINT")

class FlightSearch:

    def get_destination_code(self,city):

        params={"term":city}
        header={"apikey":API_KEY}

        LOCATION_ENDPOINT=f"{TEQUILA_ENDPOINT}locations/query"
        response=requests.get(url=LOCATION_ENDPOINT,params=params,headers=header)

        response.raise_for_status()
        return response.json()["locations"][0]["code"]

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):

        params={
            "fly_from":origin_city_code,
            "fly_to":destination_city_code,
            "date_to":to_time.strftime("%d/%m/%Y"),
            "date_from":from_time.strftime("%d/%m/%Y")
        }

        response=requests.get(url=f"{TEQUILA_ENDPOINT}v2/search",params=params,headers=header)

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
        
        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )

        return flight_data
        