from collections import defaultdict

def if_contains_anagrams(strings):
    sorted_by_length = lambda s: (''.join(sorted(s.lower())), len(s))
    anagram_dict = defaultdict(list)
    for string in strings:
        if len(string) < 3:
            continue
        key = sorted_by_length(string)
        anagram_dict[key].append(string)
    anagrams_count = sum((len(anagrams) * (len(anagrams) - 1) // 2 for anagrams in anagram_dict.values()))
    return anagrams_count <= 74