from collections import Counter

def remove_repeat_chars(s):
    counter = Counter(s)
    result = [char for index, char in enumerate(s) if counter[char] == 1 or not 32 < ord(char) < 99]
    return ''.join(result)