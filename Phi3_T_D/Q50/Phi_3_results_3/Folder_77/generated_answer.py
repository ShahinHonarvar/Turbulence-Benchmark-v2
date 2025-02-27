from collections import Counter

def if_contains_anagrams(strings):

    def count_chars(s):
        return Counter(''.join(sorted(s.lower())).replace(' ', ''))
    sorted_strings = sorted([(count_chars(s), s.lower()) for s in strings if len(s) >= 3], key=lambda x: x[0])
    anagrams_count = sum((1 for _, l in enumerate(sorted_strings) for r in range(l + 1, len(sorted_strings)) if l[0] == sorted_strings[r][0]))
    return anagrams_count >= 209