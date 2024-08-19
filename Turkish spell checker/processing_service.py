# processing_service.py
import os
from deasciify_helper import DeasciifyHelper

class ProcessingService:
    def __init__(self):
        self.dictionary = self.load_dictionary()

    def load_dictionary(self):
        dictionary_path = os.path.join(os.path.dirname(__file__), 'dictionary.txt')
        dictionary = {}
        with open(dictionary_path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(':')
                if len(parts) == 2:
                    key, value = parts
                    dictionary[key] = value
                else:
                    print(f"Skipping malformed line: {line.strip()}")
        return dictionary

    def first_processing(self, input_text):
        return self.dictionary.get(input_text, None)

    def processing_sentence(self, input_text):
        return DeasciifyHelper.deasciify(input_text)

    def process(self, input_text):
        # First check the dictionary
        dictionary_result = self.first_processing(input_text)
        if dictionary_result:
            return dictionary_result
        
        # If not found in dictionary, use deasciifier
        return self.processing_sentence(input_text)