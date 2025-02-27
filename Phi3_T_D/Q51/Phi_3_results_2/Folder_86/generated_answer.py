from collections import Counter

def if_contains_anagrams(words):
    anagram_count = 0
    checked_pairs = set()
    for i, word_a in enumerate(words):
        for word_b in words[i + 1:]:
            if i < j:
                if sorted(word_a.lower()) == sorted(word_b.lower()) and word_a.lower() != word_b.lower() and (len(word_a) >= 3) and (len(word_b) >= 3):
                    if (i, j) not in checked_pairs and (j, i) not in checked_pairs:
                        anagram_count += 1
                        checked_pairs.add((min(i, j), max(i, j)))
    return anagram_count <= 48