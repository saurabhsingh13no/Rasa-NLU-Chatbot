from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
from apixu.client import ApixuClient

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet

class ActionWeather(Action):
    def name(self):
        return 'action_weather'

    def run(self,dispatcher, tracker, domain):
        api_key = "9b14178e623944e4b3631246181904"
        client = ApixuClient(api_key)

        loc = tracker.get_slot('location')
        current = client.getCurrentWeather(q=loc)

        country = current['location']['country']
        city = current['location']['name']
        condition = current['current']['condition']['text']
        temperature_c = current['current']['temp_c']
        humidity = current['current']['humidity']
        windspeed = current['current']['wind_mph']

        response = """It is currently {} in {} at the moment. The temperature " \
                   "is {} degrees, humidity is {}% and the wind speed is {} 
                   mph""".format(condition, city, temperature_c, humidity, windspeed)

        dispatcher.utter_message(response)
        return [SlotSet('location',loc)]
