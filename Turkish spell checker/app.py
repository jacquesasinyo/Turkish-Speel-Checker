from flask import Flask, request, jsonify
from flasgger import Swagger
from processing_service import ProcessingService

app = Flask(__name__)
swagger = Swagger(app)
processing_service = ProcessingService()

@app.route('/convert', methods=['POST'])
def convert_text():
    """
    Convert ASCII text to Turkish
    ---
    parameters:
      - name: input
        in: body
        type: string
        required: true
        description: The ASCII input text
        schema:
          type: object
          required:
            - input
          properties:
            input:
              type: string
              example: Siirt
    responses:
      200:
        description: The converted Turkish text
        schema:
          type: object
          properties:
            output:
              type: string
              example: Siirt
      400:
        description: Invalid input
        schema:
          type: object
          properties:
            error:
              type: string
              example: No input text provided
    """
    data = request.get_json()
    input_text = data.get('input')
    if not input_text:
        return jsonify({'error': 'No input text provided'}), 400
    
    result = processing_service.process(input_text)
    return jsonify({'output': result})

if __name__ == '__main__':
    app.run(debug=True)