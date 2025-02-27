from collections import Counter

def if_contains_anagrams(lst):

    def anagram_count(word):
        return Counter(sorted(word.lower()))
    anagrams = [anagram_count(word) for word in lst if len(word) >= 3]
    pairs = set()
    for i in range(len(anagrams)):
        for j in range(i + 1, len(anagrams)):
            if anagrams[i] == anagrams[j]:
                pairs.add(tuple(sorted([i, j])))
    return len(pairs) >= 52