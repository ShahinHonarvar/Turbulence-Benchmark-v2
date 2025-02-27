from collections import Counter
import re

def remove_repeat_chars(string):
    substring = string[32:44]
    char_counts = Counter(substring)
    for char, count in char_counts.most_common():
        if count > 1:
            string = re.sub(char, '', string)
    return string