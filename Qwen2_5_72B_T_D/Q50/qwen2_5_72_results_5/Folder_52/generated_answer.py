from collections import Counter

def if_contains_anagrams(words):
    words = [word.lower() for word in words]
    filtered_words = [word for word in words if len(word) >= 3]
    sorted_words = [''.join(sorted(word)) for word in filtered_words]
    word_count = Counter(sorted_words)
    anagram_pairs = sum((count * (count - 1) // 2 for count in word_count.values()))
    return anagram_pairs >= 58