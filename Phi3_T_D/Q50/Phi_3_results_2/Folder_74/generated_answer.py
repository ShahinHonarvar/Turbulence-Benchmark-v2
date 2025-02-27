from collections import defaultdict

def if_contains_anagrams(lst):

    def normalize_str(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = defaultdict(int)
    for word in lst:
        if len(word) < 3:
            continue
        normalized = normalize_str(word)
        anagram_dict[normalized] += 1
    anagram_count = 0
    for count in anagram_dict.values():
        anagram_count += count * (count - 1) // 2
    return anagram_count >= 17