from collections import defaultdict

def if_contains_anagrams(words):
    letter_frequencies = defaultdict(lambda: defaultdict(int))
    for word in words:
        word = word.lower()
        if len(word) >= 3:
            for letter in word:
                if letter.isalpha():
                    letter_frequencies[word][letter] += 1
    anagram_pairs = 0
    for word1, freq1 in letter_frequencies.items():
        for word2, freq2 in letter_frequencies.items():
            if word1 != word2 and freq1 == freq2:
                anagram_pairs += 1
                if anagram_pairs > 25:
                    return False
    return True