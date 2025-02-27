from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram_pair(s1, s2):
        return len(s1) > 2 and len(s2) > 2 and (sorted(s1.lower()) == sorted(s2.lower()))
    anagrams_count = 0
    checked_pairs = set()
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if (i, j) not in checked_pairs and is_anagram_pair(strings[i], strings[j]):
                anagrams_count += 1
                checked_pairs.add((i, j))
    return anagrams_count >= 88