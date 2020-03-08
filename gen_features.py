#!/usr/bin/env python3

import sys
import argparse
import parser

def get_schema_lines(schema_file):
    parsed_lines = []
    data_no = -1
    features = []
    with open(schema_file) as df:
        for line in df:
            line = line.strip()
            cols = line.split()
            if not line or line.startswith('#') or line.startswith(';'):
                parsed_lines.append(line)
                continue
            if cols[0] == "import":
                parsed_lines.append(line)
                continue
            features.append(cols[0])
            if len(cols) < 2:
                data_no += 1
                parsed_lines.append("%s = INPUT[%s]" % (line, data_no))
                continue
            parsed_lines.append("%s = %s" % (cols[0], " ".join(cols[1:])))
    return features, parsed_lines


def get_parser_code(schema_file, parser_file_needed):
    """
    Builds a parser which can be used to generate data
    :return: Parser
    """
    features, parsed_lines = get_schema_lines(schema_file)
    code = "\n".join(parsed_lines)
    code += """


def computed_features():
    return ",".join([%s])
""" % ",".join(["str(%s)" % f for f in features])

    if parser_file_needed:
        name_parts = schema_file.split('.')
        if len(name_parts) > 1:
            parser_file = "%s.py" % '.'.join(name_parts[:-1])
        else:
            parser_file = "%s.py" % schema_file
        with open(parser_file, 'w') as fh:
            fh.write(code)

    return code


def parse_input():
    DESC = """
    Usage: %(prog)s [options] data_file
    """
    EXAMPLES = """
    eg: %(prog)s data_file
    """
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, description=DESC,
                                     epilog=EXAMPLES)
    parser.add_argument('-p', '--parser_code_file', help='Generate parser Code File', default=False, action="store_true")
    parser.add_argument('-s', '--schema_file', help='Schema File')
    parser.add_argument('data_file', help='Data File')
    if len(sys.argv) < 2:
        parser.parse_args(['-h'])
    args = parser.parse_args()
    return args


args = parse_input()
code = get_parser_code(args.schema_file, args.parser_code_file)
feat_parser = parser.suite(code).compile()
# Add helper function to code base
for line_no, line in enumerate(list(open(args.data_file))):
    INPUT = line.strip().split(',')
    eval(feat_parser)
    print(computed_features())
