import collections

def if_contains_anagrams(strings):
    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3 and (collections.Counter(strings[i].lower()) == collections.Counter(strings[j].lower())):
                anagram_pairs += 1
    return anagram_pairs >= 47