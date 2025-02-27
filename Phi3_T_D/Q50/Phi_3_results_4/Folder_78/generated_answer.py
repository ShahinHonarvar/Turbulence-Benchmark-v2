from collections import Counter

def if_contains_anagrams(strings):

    def anagram_key(s):
        return Counter(''.join(sorted((c for c in s.lower() if c.isalpha()))))
    count_anagrams = 0
    checked_pairs = set()
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if (i, j) not in checked_pairs and anagram_key(strings[i]) == anagram_key(strings[j]) and (len(strings[i]) >= 3) and (len(strings[j]) >= 3):
                count_anagrams += 1
                checked_pairs.add((i, j))
    return count_anagrams >= 79