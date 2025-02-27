from collections import Counter

def if_contains_anagrams(words):
    word_count = Counter(words)
    anagram_pairs = 0
    for word, count in word_count.items():
        for other_word, other_count in word_count.items():
            if word.lower() != other_word.lower() and sorted(word.lower()) == sorted(other_word.lower()) and (len(word) >= 3):
                anagram_pairs += count * other_count
    return anagram_pairs // 2 >= 91