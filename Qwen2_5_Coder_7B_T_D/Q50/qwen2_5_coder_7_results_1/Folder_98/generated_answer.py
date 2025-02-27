from collections import Counter

def if_contains_anagrams(words):
    anagrams = {}
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
    anagram_pairs = sum([len(v) * (len(v) - 1) // 2 for v in anagrams.values() if len(v) > 1])
    return anagram_pairs >= 7