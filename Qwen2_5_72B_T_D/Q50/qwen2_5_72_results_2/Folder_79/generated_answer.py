from collections import Counter

def if_contains_anagrams(words):
    words = [word.lower() for word in words if len(word) >= 3]
    sorted_words = [''.join(sorted(word)) for word in words]
    count = Counter(sorted_words)
    anagram_pairs = sum((freq * (freq - 1) // 2 for freq in count.values()))
    return anagram_pairs >= 40