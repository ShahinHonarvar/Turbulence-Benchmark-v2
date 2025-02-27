from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    count = 0
    for s in strings:
        sorted_str = ''.join(sorted(s.lower()))
        anagram_dict[sorted_str].append(s)
    for key in anagram_dict:
        if len(anagram_dict[key]) > 1 and len(key) >= 3:
            count += sum((1 for _ in range(len(anagram_dict[key]) - 1)))
    return count >= 42