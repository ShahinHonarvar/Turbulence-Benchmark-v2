from collections import Counter

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return Counter(s1) == Counter(s2)
    seen = set()
    anagram_count = 0
    for word in lst:
        word = word.lower()
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word))
        if sorted_word in seen:
            anagram_count += seen[sorted_word]
        seen[sorted_word] = seen.get(sorted_word, 0) + 1
    return anagram_count >= 86