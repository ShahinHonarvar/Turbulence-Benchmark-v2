from collections import Counter

def if_contains_anagrams(lst):
    anagram_pairs = 0
    seen = set()
    for word in lst:
        word = word.lower()
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word))
        if sorted_word in seen:
            if (sorted_word, word) not in anagram_pairs and (word, sorted_word) not in anagram_pairs:
                anagram_pairs += 1
        seen.add(sorted_word)
    return anagram_pairs <= 2