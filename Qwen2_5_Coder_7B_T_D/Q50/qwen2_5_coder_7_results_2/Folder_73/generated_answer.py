from collections import Counter

def if_contains_anagrams(words):
    anagram_pairs = 0
    for word in words:
        if len(word) >= 3:
            word = word.lower()
            sorted_word = ''.join(sorted(word))
            word_counter = Counter(words)
            for other_word in words:
                if other_word.lower() != word and len(other_word) >= 3:
                    other_word = other_word.lower()
                    sorted_other_word = ''.join(sorted(other_word))
                    if sorted_word == sorted_other_word and word_counter[other_word] > 0:
                        anagram_pairs += 1
    return anagram_pairs >= 91