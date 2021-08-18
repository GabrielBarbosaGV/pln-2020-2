# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from actions.api import StatusInvestAPI
from actions.api.exceptions import InvalidFundamentalistIndexException

def get_tag_type(q_type):
    if q_type.lower() in ['da', 'da ação', 'da acao']:
        return 1
    else:
        return 2

def get_info(f_idx, response):
    clean_text = f_idx.lower()
    if clean_text in ['preço', 'preco']:
        return response.get('current_price')
    elif clean_text in ['nome', 'empresa', 'titulo']:
        return response.get('title')
    elif clean_text in ['cnpj']:
        return response.get('cnpj')
    elif clean_text in ['dividend yield', 'dy', 'd.y.', 'dy.', 'd.y']:
        return response.get('indicators').get('D.Y')
    raise InvalidFundamentalistIndexException(f_idx)

class ActionGetInformations(Action):
    def name(self) -> Text:
        return "action_get_information"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, _) -> List[Dict[Text, Any]]:
        try:
            api = StatusInvestAPI()
            tag = tracker.get_slot('tag')
            f_idx = tracker.get_slot('f-idx')
            q_type = tracker.get_slot('q-type')
            print(tag, f_idx, q_type)
            response = api.query(tag, get_tag_type(q_type))
            dispatcher.utter_message(get_info(f_idx, response))
        except Exception as e:
            print(e)

        return []
