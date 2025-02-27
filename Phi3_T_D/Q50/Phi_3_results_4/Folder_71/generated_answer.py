from collections import defaultdict

def if_contains_anagrams(lst):

    def are_anagrams(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    count = 0
    anagram_map = defaultdict(int)
    for i, word in enumerate(lst):
        word_lower = word.lower()
        for key in anagram_map:
            if are_anagrams(word_lower, key) and len(word) >= 3:
                count += 1
                break
        else:
            anagram_key = ''.join(sorted(word_lower))
            anagram_map[anagram_key] += 1
    return count >= 57