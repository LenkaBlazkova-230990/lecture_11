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


# def pattern_search(sequential_data, searched_pattern):
#     length_of_searched_pattern = len(searched_pattern)
#     positions_set = set()
#
#     start_idx = 0
#     end_idx = length_of_searched_pattern
#
#     while end_idx < len(sequential_data):
#         if sequential_data[start_idx:end_idx] == searched_pattern:
#             position = start_idx + (length_of_searched_pattern // 2)
#             positions_set.add(position)
#
#         start_idx += 1
#         end_idx = start_idx + length_of_searched_pattern
#     # while end_idx < len(sequential_data):
#     #     for idx in range(length_of_searched_pattern):
#     #         if searched_pattern == sequential_data[idx:idx + length_of_searched_pattern]:
#     #             position = start_idx + (length_of_searched_pattern // 2)
#     #             positions_set.add(position)
#     #
#     #         start_idx += 1
#     #         end_idx = start_idx + length_of_searched_pattern
#
#     return positions_set


# upraveny algoritmus
def pattern_search(sequential_data, searched_pattern):
    length_of_searched_pattern = len(searched_pattern)
    positions_set = set()

    start_idx = 0
    end_idx = length_of_searched_pattern

    while end_idx < len(sequential_data):
        for idx_p in range(length_of_searched_pattern):
            if searched_pattern[idx_p] != sequential_data[start_idx + idx_p]:
                break
        else:
            positions_set.add(start_idx + length_of_searched_pattern // 2)

        start_idx += 1
        end_idx += 1

    return positions_set


def main():
    file_name = "sequential.json"
    # sequential_data = read_data(file_name, "unordered_numbers")
    sequential_data = read_data(file_name, "dna_sequence")
    # print(sequential_data)

    linear_search_results = linear_search(sequential_data, searched_number=0)
    # print(linear_search_results)

    searched_pattern = "ATA"
    pattern_search_results = pattern_search(sequential_data, searched_pattern)
    print(pattern_search_results)
    # pass


if __name__ == '__main__':
    main()
