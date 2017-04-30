import pymorphy2
from flask_jsonrpc import JSONRPC

from app import app
from app.schemas import PyMorphyParseResultSchema, PyMorphyParseResultSchemaLight

jsonrpc = JSONRPC(app, '/api', enable_web_browsable_api=True)
morph = pymorphy2.MorphAnalyzer()

# app = Flask(__name__)
# jsonrpc = JSONRPC(app, '/api', enable_web_browsable_api=True)


@jsonrpc.method('flamorphy.parse(String, Boolean) -> Array')
def parse(raw_str, full=False):
    response = []
    dump_schema_class = PyMorphyParseResultSchema if full else PyMorphyParseResultSchemaLight

    for word in raw_str.split():
        parse_results_bundle = dump_schema_class(many=True).dump(morph.parse(word)).data
        response.append({
            'word': word,
            'parse': parse_results_bundle
        })
    return response


@jsonrpc.method('flamorphy.inflect(String, Array, Number, Boolean) -> Object')
def inflect(word, required_grammemes, parse_index=0, full=False):
    parse_results = morph.parse(word)
    parse_result = parse_results[parse_index]
    res = parse_result.inflect(frozenset(required_grammemes))
    dump_schema_class = PyMorphyParseResultSchema if full else PyMorphyParseResultSchemaLight

    response_data = dump_schema_class().dump(res).data
    return response_data


@jsonrpc.method('flamorphy.inflect_words(String, Array, Array, Boolean) -> Object')
def inflect_words(raw_str, required_grammemes_list, parse_indexes=None, full=False):
    words = raw_str.strip().split()
    if not parse_indexes:
        parse_indexes = [0] * len(words)
    if len(required_grammemes_list) != len(words):
        raise ValueError('`required_grammemes_list` length should be the same as word count % s' %
                         required_grammemes_list)
    if len(parse_indexes) != len(words):
        raise ValueError('`parse_indexes` length should be the same as word count % s' % parse_indexes)

    response = {'words': [], 'results': []}
    for word, required_grammemes, parse_index in zip(words, required_grammemes_list, parse_indexes):
        result = inflect(word, required_grammemes, parse_index, full=full)
        response['results'].append(result)
        response['words'].append(result.get('word', word))
    return response


# if __name__ == '__main__':
#     app.run(host='0.0.0.0', debug=True)
