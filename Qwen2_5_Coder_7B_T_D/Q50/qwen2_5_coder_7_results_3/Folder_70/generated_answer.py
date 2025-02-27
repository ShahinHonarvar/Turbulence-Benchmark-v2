from collections import Counter

def if_contains_anagrams(strings):

    def count_anagrams(s):
        return Counter(sorted(s.lower()))
    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3 and (count_anagrams(strings[i]) == count_anagrams(strings[j])):
                anagram_pairs += 1
    return anagram_pairs >= 189