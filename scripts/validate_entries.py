import argparse
import common


def main():

    parser = argparse.ArgumentParser(description='Validates entries in a JSON file')
    parser.add_argument('input_file', help='JSON file')
    parser.add_argument('--show-warnings', action='store_true', help='print warnings to the console')

    args = parser.parse_args()
    entries_from_json = common.read_issuer_entries_from_json_file(args.input_file)

    validation_results = common.validate_entries(entries_from_json)
    valid = common.analyze_results(validation_results, True, args.show_warnings)

    if valid:
        print('All entries are valid')
        exit(0)
    else:
        print('One or more entries are invalid')
        exit(1)

if __name__ == "__main__":
    main()