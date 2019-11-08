from flask import Flask, jsonify, abort

import get_json_response

# based on junior dev test, here: https://gist.github.com/thedaniel/f6e3e41644facd086341d875ea3f9715

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route('/vat/')
def vat_home():
    message = 'add one of these country codes to the end of your url: ' + str(codes)
    return message

@app.route('/vat/<country_code>', methods=["GET"])
def vat_app(country_code):
    response = get_json_response.get_response()

    codes = get_json_response.check_code_list(response)

    if response.status_code == 200:
        if country_code in codes:
            country = get_json_response.get_country(country_code, response)
            standard = get_json_response.get_standard_rate(country)
            return jsonify(country=country['name'], standard_rate=standard), 200
        else:
            return abort(404, 'Not a country- try again!')
    else:
        return abort(404, 'VAT json doesnt exist; sorry buddy')

@app.route('/thought-process')
def get_thought_process():
    with open('thought_process.txt', 'r') as f:
        content = f.read()
    return content

if __name__ == "__main__":
    app.run(debug=True, port=5000)
