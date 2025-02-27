from collections import defaultdict

def if_contains_anagrams(words):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    words = list(filter(lambda w: len(w) >= 3, words))
    anagrams = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        anagrams[sorted_word].append(word)
    return sum((len(group) // 2 for group in anagrams.values() if len(group) // 2 >= 3)) >= 6