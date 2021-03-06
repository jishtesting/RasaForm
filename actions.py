# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any,Union, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
#
#
class ActionHelloWorld(FormAction):
    def name(self) -> Text:
        return "admission_form"
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        print("required slots(tracker: Tracker)")
        return  ["name","ssn","subject"]
    
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "name": [self.from_entity(entity="name", intent='name_entry'),
                     self.from_text()],
            "ssn": [self.from_entity(entity="ssn", intent="ssn_entry"),
                        self.from_text()],
            "subject": [self.from_entity( entity="subject", intent="subject_entry" ),
                        self.from_text()],
        }
    def submit(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(template="utter_submit")
        return []
