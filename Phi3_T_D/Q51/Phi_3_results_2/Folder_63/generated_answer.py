from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagrams = defaultdict(int)
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                anagrams[strings[i].lower()] += 1
    return sum((1 for count in anagrams.values() if count >= 2)) <= 423