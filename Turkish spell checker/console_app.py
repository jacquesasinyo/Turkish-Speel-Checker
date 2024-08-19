# console_app.py
import locale
from processing_service import ProcessingService

def set_app_language(language="tr_TR"):
    locale.setlocale(locale.LC_ALL, language)

def main():
    set_app_language()
    processing_service = ProcessingService()
    
    while True:
        sentence = input("Input: ")
        response = processing_service.process(sentence)
        print("Output:", response)
        input("Press Enter to continue...")

if __name__ == "__main__":
    main()