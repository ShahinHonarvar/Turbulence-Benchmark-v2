from collections import defaultdict

def if_contains_anagrams(strings):

    def char_count(s):
        count = defaultdict(int)
        for char in s.lower():
            if char.isalpha():
                count[char] += 1
        return frozenset(count.items())

    def are_anagrams(s1, s2):
        return char_count(s1) == char_count(s2)
    anagram_pairs = 0
    checked_pairs = set()
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                if are_anagrams(strings[i], strings[j]):
                    pair = frozenset((strings[i], strings[j]))
                    if pair not in checked_pairs:
                        anagram_pairs += 1
                        checked_pairs.add(pair)
                        if anagram_pairs > 36:
                            return False
    return True