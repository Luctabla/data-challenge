from flask import Flask, make_response, request
from utils import DataHelper

import config

app = Flask(__name__)
dh = DataHelper()

@app.route('/countries_by/', methods=['GET'])
def countries_by():
    """This view return countries with their index value,
     greater than the input value, using only life satisfaction
     index and total inequality"""

    indicator = request.args.get('indicator')
    index_value = request.args.get('index_value')

    try:
        dh.validate_filters(indicator, index_value)
    except:
        return make_response("Parameters error.", config.HTTP_400_BAD_REQUEST)

    response = dh.countries_by_indicator(indicator, index_value)
    df_list = response.to_json()
    return df_list

if __name__ == '__main__':
    app.run()