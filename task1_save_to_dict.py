import json


def create_dict_from_file(file_name: str) -> dict:
    result = {}
    with open(file_name) as file:
        for line in file:
            tmp_line = json.loads(line)
            result[tmp_line['user_id']] = tmp_line['category']
    return result


def print_dict_partial(dictionary: dict, num_items: int = 10):
    print('purchases:')

    for key, value in dictionary.items():
        if num_items == 0:
            break
        print(f'{key} {value}')
        num_items -= 1


def main():
    purchases = create_dict_from_file('purchase_log.txt')
    print_dict_partial(purchases)


if __name__ == '__main__':
    main()
