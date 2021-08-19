# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
# from rasa.actions.api import exceptions

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from unidecode import unidecode

from actions.api import StatusInvestAPI
from actions.api.helper import get_info, get_tag_type

class ActionGetInformations(Action):
    def name(self) -> Text:
        return "action_get_information"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, _) -> List[Dict[Text, Any]]:
        try:
            api = StatusInvestAPI()
            tag = tracker.get_slot('tag')
            f_idx = tracker.get_slot('f-idx')
            q_type = get_tag_type(tracker.get_slot('q-type'))
            print(tag, f_idx, q_type)
            response = api.query(q_type, tag)
            dispatcher.utter_message(f"Informações sobre {get_info(q_type, 'titulo', response)} - CNPJ {get_info(q_type, 'cnpj', response)}:\nO {f_idx} desse título é {get_info(q_type, f_idx, response)}")
        except Exception as e:
            dispatcher.utter_message(f"Desculpe. {e.message}")

        return []
