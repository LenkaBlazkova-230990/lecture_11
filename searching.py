import os
import json


# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.

    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)

    if field not in {"unordered_numbers", "ordered_numbers", "dna_sequence"}:
        return None

    with open(file_path, 'r') as json_file:
        dictionary = json.load(json_file)

    sequence = dictionary[field]
    return sequence


def linear_search(sequential_data, searched_number):
    """
    Linear searching in unordered list

    :param sequential_data: (list) list of input numbers
    :param searched_number: (int) searched number
    :return: dictionary - positions of searched number and its count
    """
    indices_position = []
    count = 0

    for position, number in enumerate(sequential_data):
        if number == searched_number:
            indices_position.append(position)
            count += 1

    dict = {
        "positions": indices_position,
        "count": count
    }

    return dict


def main():
    file_name = "sequential.json"
    sequential_data = read_data(file_name, "unordered_numbers")
    # print(sequential_data)

    linear_search_results = linear_search(sequential_data, searched_number=0)
    print(linear_search_results)
    # pass


if __name__ == '__main__':
    main()