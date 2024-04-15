
import requests,os

SHEETY_ENDPOINT=os.environ.get("ENDPOINT")

class DataManager:

    def get_destination_data(self):
        response=requests.get(url=SHEETY_ENDPOINT)
        response.raise_for_status()
        return response.json()["prices"]

    def update_destination_codes(self,id,body):

        body={
            "price":{
                "iataCode":body
            }
        }

        response=requests.put(url=f"{SHEETY_ENDPOINT}/{id}",json=body)
        response.raise_for_status()
        