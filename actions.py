from rasa_core.actions import Action
from rasa_core.events import Restarted
from rasa_core.actions.forms import (
    BooleanFormField,
    EntityFormField,
    FormAction,
    FreeTextFormField
)
from rasa_core_sdk.events import SlotSet
import httplib2
import requests

class ActionaskRestaurant(FormAction):
		RANDOMIZE=False
		@staticmethod
		def required_fields():
			return[
				EntityFormField("cuisine", "cuisine"),
				EntityFormField("location", "location")
				]
				
		def name(self):
			return "action_askrestaurant"
			
		def submit(self,dispatcher,tracker,domain):
			dispatcher.utter_message("your searching restaurants list")
			
				