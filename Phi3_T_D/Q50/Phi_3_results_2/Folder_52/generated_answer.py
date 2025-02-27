from collections import defaultdict

def if_contains_anagrams(words):

    def count_chars(s):
        return ''.join(sorted(s.lower()))
    freq_map = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            sorted_chars = count_chars(word)
            freq_map[sorted_chars].append(word)
    anagram_pairs_count = 0
    for anagrams in freq_map.values():
        anagram_pairs_count += len(anagrams) * (len(anagrams) - 1) // 2
    return anagram_pairs_count >= 58