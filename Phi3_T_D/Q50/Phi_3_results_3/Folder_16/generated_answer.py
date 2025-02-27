import collections

def if_contains_anagrams(strings):
    anagram_pairs = 0
    filtered_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    counter = collections.Counter(filtered_strings)
    for count in counter.values():
        anagram_pairs += count * (count - 1) // 2
    return anagram_pairs >= 155