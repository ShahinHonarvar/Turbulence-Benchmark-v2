from collections import defaultdict

def if_contains_anagrams(strings):
    sorted_strings = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            sorted_strings[sorted_string].append(string)
    count = 0
    for values in sorted_strings.values():
        if len(values) >= 2:
            count += len(values) // 2
    return count >= 16