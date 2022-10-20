import json


def create_dict_from_file(file_name: str) -> dict:
    result = {}
    with open(file_name) as file:
        for line in file:
            tmp_line = json.loads(line)
            result[tmp_line['user_id']] = tmp_line['category']
    return result


def add_category(category_file_name: str, visit_file_name: str, result_file: str = 'funnel.csv'):
    purchases = create_dict_from_file(category_file_name)
    with open(visit_file_name) as visit_file:
        with open(result_file, 'a') as result_file:
            for line in visit_file:
                user_id, _ = line.split(',')
                if purchases.get(user_id):
                    new_line = line.rstrip() + ',' + purchases.get(user_id)
                    print(new_line, file=result_file)


def main():
    add_category('purchase_log.txt', 'visit_log.csv')


if __name__ == '__main__':
    main()
