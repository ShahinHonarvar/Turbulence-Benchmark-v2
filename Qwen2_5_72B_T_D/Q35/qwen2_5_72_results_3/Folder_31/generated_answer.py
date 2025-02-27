from collections import Counter

def remove_repeat_chars(s):
    counter = Counter(s)
    result = []
    for i, char in enumerate(s):
        if 33 < ord(char) < 78 and counter[char] > 1:
            continue
        result.append(char)
    return ''.join(result)