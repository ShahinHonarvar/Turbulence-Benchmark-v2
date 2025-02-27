from collections import Counter

def if_contains_anagrams(lst):

    def is_anagram(str1, str2):
        str1 = str1.lower()
        str2 = str2.lower()
        if len(str1) != len(str2):
            return False
        return Counter(str1) == Counter(str2)
    seen_anagrams = set()
    anagram_pairs = set()
    for word in lst:
        if len(word) < 3:
            continue
        for seen_word in seen_anagrams:
            if is_anagram(word, seen_word):
                anagram_pairs.add((min(word, seen_word), max(word, seen_word)))
                break
        seen_anagrams.add(word)
    return len(anagram_pairs) <= 41