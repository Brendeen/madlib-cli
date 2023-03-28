import re


def read_template(file_path):
    """
    This function will take in a file path
    and strip it into a string
    :param file_path: Argument/file
    :return: String of desired text file
    """
    with open(file_path, "r")as file:
        content = file.read()
        print(content)
        return content


def parse_template(content):
    """
    This function will take the previously
    stripped string, and use Regex to parse
    the string and return a modified string
    and tuple of the parsed words.
    :param content: Previous stripped string
    :return: Modified string and tuple
    """
    find_all_list = re.findall(r'{(.*?)}', content)
    new_string = re.sub(r'({.*?})', '{}', content)
    find_all_list = tuple(find_all_list)
    print(new_string)
    print(find_all_list)
    return new_string, find_all_list


def merge(new_string, find_all_list):
    final_string = new_string.format(*find_all_list)
    print(final_string)
    return final_string
