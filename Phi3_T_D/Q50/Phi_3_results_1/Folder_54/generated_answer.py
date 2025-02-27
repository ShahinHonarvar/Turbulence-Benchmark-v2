from collections import defaultdict
import itertools

def if_contains_anagrams(strings_list):

    def custom_key(s):
        return ''.join(sorted(s)).lower()
    counts = defaultdict(int)
    anagram_pairs = 0
    for word in strings_list:
        if len(word) < 3:
            continue
        key = custom_key(word)
        counts[key] += 1
    for count in counts.values():
        anagram_pairs += count * (count - 1) // 2
    return anagram_pairs >= 74