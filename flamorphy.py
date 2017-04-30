import pymorphy2
import os
import sys

from flask import Flask

PROJECT_DIR, PROJECT_MODULE_NAME = os.path.split(
    os.path.dirname(os.path.realpath(__file__))
)

FLASK_JSONRPC_PROJECT_DIR = os.path.join(PROJECT_DIR, os.pardir)
if os.path.exists(FLASK_JSONRPC_PROJECT_DIR) \
        and not FLASK_JSONRPC_PROJECT_DIR in sys.path:
    sys.path.append(FLASK_JSONRPC_PROJECT_DIR)

from flask_jsonrpc import JSONRPC

morph = pymorphy2.MorphAnalyzer()

app = Flask(__name__)
jsonrpc = JSONRPC(app, '/api', enable_web_browsable_api=True)


@jsonrpc.method('flamorphy.index')
def index():
    return 'lol'


# (String) -> List
@jsonrpc.method('flamorphy.parse(String) -> String')
def parse(raw_str):
    response = []
    for word in raw_str.split():
        parse_results_bundle = {'word': word, 'results': []}
        for parse_result in morph.parse(word):
            parse_results_bundle['results'].append({
                'normal_form': parse_result.normal_form
            })
        response.append(parse_results_bundle)

    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
