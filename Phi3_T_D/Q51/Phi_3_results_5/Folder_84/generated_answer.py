from collections import Counter

def sorted_string(s):
    return ''.join(sorted(s.lower()))

def if_contains_anagrams(strings):
    counter = {}
    for string in strings:
        if len(string) < 3:
            continue
        key = sorted_string(string)
        if key in counter:
            pair = (string, counter[key][0])
            if counter[key] == 2:
                return False
            counter[key].append(string)
        else:
            counter[key] = [string]
    anagram_pairs = [key for key in counter if len(counter[key]) > 1 and len(counter[key]) * len(counter[key][0]) >= 3]
    max_pairs = len(anagram_pairs) * (len(anagram_pairs) - 1) // 2
    return max_pairs <= 16