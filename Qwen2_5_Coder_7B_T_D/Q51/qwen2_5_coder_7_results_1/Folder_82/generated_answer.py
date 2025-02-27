from collections import defaultdict

def if_contains_anagrams(words):
    word_count = defaultdict(int)
    for word in words:
        word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            word_count[word] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in word_count.values() if count > 1))
    return anagram_pairs <= 40