import re


def remove_unnecessary_spaces(details):
    for detail in details:
        details[detail] = re.sub(' +', ' ',details.get(detail).strip())
    return details

def capitalize_details(details):
    for detail in details:
        details[detail] = details.get(detail).upper()
    return details









