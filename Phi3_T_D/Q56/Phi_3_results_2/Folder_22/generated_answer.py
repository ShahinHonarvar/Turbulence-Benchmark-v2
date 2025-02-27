from collections import Counter

def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 21):
        substring = s[i:i + 22]
        if all((count == 1 for count in Counter(substring).values())):
            substrings.add(substring)
    return list(substrings)