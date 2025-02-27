from collections import defaultdict

def if_contains_anagrams(words):
    length_to_anagrams = defaultdict(set)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            length_to_anagrams[sorted_word].add(word)
    count = 0
    for anagrams in length_to_anagrams.values():
        for word1 in anagrams:
            for word2 in anagrams:
                if word1 != word2:
                    count += 1
                    if count >= 85:
                        return True
    return False