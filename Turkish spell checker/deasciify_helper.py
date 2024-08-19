# deasciify_helper.py
from deasciifier import Deasciifier

class DeasciifyHelper:
    @staticmethod
    def deasciify(input_text):
        deasciifier = Deasciifier(input_text)
        return deasciifier.convert_to_turkish()