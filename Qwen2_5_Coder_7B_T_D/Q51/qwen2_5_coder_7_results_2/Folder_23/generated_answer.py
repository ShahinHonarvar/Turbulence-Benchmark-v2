from collections import defaultdict

def if_contains_anagrams(words):
    word_count = defaultdict(int)
    for word in words:
        if 3 <= len(word):
            sorted_word = ''.join(sorted(word.lower()))
            word_count[sorted_word] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in word_count.values()))
    return anagram_pairs <= 49