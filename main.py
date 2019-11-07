from flask import Flask, jsonify, abort
import get_json

codes = get_json.check_code_list()

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route('/vat')
def vat_home():
    default = 'NL'
    return vat_app(default)

@app.route('/vat/<country_code>', methods=["GET"])
def vat_app(country_code):
    if country_code in codes:
        country = get_json.get_country(country_code)
        standard = get_json.get_standard_rate(country)
        return jsonify(country=country['name'], standard_rate=standard)
    else:
        return abort(404, 'Not a country- try again!')

