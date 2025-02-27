import re

def all_substring_of_size_n(text):
    substrings = re.findall('.{28}', text)
    return [substring for substring in substrings if len(set(substring)) == len(substring)]