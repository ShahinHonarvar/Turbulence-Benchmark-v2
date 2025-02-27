from collections import Counter

def if_contains_anagrams(lst):

    def normalize_string(s):
        return Counter(s.lower())
    counts = {}
    for word in lst:
        if len(word) < 3:
            continue
        norm_word = normalize_string(word)
        key = tuple(sorted(norm_word.keys()))
        anagrams = counts.setdefault(key, [])
        if word not in anagrams:
            anagrams.append(word)
    anagram_pairs = 0
    for anagrams_list in counts.values():
        anagram_pairs += sum(range(len(anagrams_list) - 1))
    return anagram_pairs <= 147