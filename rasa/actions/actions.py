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
    lower_type = q_type.lower()
    if lower_type in ['da', 'da ação', 'da acao']:
        return 1
    elif lower_type in ['do', 'do fundo']:
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
        return response.get('dividend_yield')
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
            response = api.query(get_tag_type(q_type), tag)
            dispatcher.utter_message(get_info(f_idx, response))
        except Exception as e:
            raise e

        return []
