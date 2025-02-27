from collections import defaultdict

def if_contains_anagrams(lst):
    strings_by_sorted = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            strings_by_sorted[sorted_word].append(word)
    anagram_count = sum((len(lst) > 1 for lst in strings_by_sorted.values()))
    return anagram_count >= 10