import json
import argparse


def parser_config():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description='''\
            Read data from json file, set in first argument.
            Print it in pretty json format''')
    parser.add_argument('file_path', metavar='data.json', type=str,
                        help='path to the json file')
    return parser


def load_json_data(file_path):
    with open(file_path) as json_data:
        return json.load(json_data)


def pretty_print_json(data):
    return json.dumps(data, sort_keys=True, ensure_ascii=False, indent=4,
                      separators=(',', ': '))


if __name__ == '__main__':
    json_data = load_json_data(parser_config().parse_args().file_path)
    pretty_json_data = pretty_print_json(json_data)
    print(pretty_json_data)
