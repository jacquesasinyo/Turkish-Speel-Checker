# generate_model_helper.py
class GenerateModelHelper:
    @staticmethod
    def create_text_conversion_request_model(input_text):
        return {'input': input_text}

    @staticmethod
    def create_text_conversion_response_model(output_text):
        return {'output': output_text}