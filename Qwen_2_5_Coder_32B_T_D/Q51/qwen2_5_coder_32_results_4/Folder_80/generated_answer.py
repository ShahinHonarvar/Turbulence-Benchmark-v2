from collections import Counter

def if_contains_anagrams(words):
    filtered_words = [word.lower() for word in words if len(word) >= 3]
    anagram_counts = Counter((''.join(sorted(word)) for word in filtered_words))
    return sum((count * (count - 1) // 2 for count in anagram_counts.values())) <= 255