from collections import Counter

def if_contains_anagrams(words):
    word_count = []
    for word in words:
        if len(word) >= 3:
            count = Counter(word.lower())
            word_count.append((word, count))
    anagram_pairs = 0
    for i in range(len(word_count)):
        for j in range(i + 1, len(word_count)):
            if word_count[i][1] == word_count[j][1]:
                anagram_pairs += 1
    return anagram_pairs >= 144