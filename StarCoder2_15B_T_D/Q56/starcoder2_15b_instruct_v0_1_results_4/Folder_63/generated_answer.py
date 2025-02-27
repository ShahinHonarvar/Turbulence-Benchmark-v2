import re

def all_substring_of_size_n(text):
    match = re.search('\\\\b\\\\d{1,9}\\\\b', text)
    if match:
        substring_length = int(match.group())
    else:
        raise ValueError('Substring length not found in text specification.')
    substrings = set()
    for i in range(len(text) - substring_length + 1):
        substring = text[i:i + substring_length]
        if len(set(substring)) == len(substring):
            substrings.add(substring)
    return list(substrings)