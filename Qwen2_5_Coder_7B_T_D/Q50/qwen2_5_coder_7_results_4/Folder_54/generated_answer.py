from collections import Counter

def if_contains_anagrams(strings):

    def count_anagrams(s):
        return sum(Counter(sorted(s.lower())).values()) >= 3
    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if count_anagrams(strings[i]) and count_anagrams(strings[j]) and (Counter(strings[i].lower()) == Counter(strings[j].lower())):
                anagram_pairs += 1
    return anagram_pairs >= 74