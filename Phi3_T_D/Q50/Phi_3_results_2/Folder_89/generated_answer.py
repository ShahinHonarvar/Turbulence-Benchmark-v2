from collections import defaultdict, Counter

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    count = 0
    for string in strings:
        if len(string) < 3:
            continue
        key = str(Counter(string.lower()))
        anagram_dict[key].append(string)
        count += len(anagram_dict[key]) * (len(anagram_dict[key]) - 1) // 2
    return count >= 36