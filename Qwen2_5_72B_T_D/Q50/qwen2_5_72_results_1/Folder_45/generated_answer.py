from collections import Counter

def if_contains_anagrams(words):
    words = [word.lower() for word in words]
    words = [word for word in words if len(word) >= 3]
    anagram_dict = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        anagram_dict[sorted_word] = anagram_dict.get(sorted_word, 0) + 1
    anagram_counts = Counter(anagram_dict.values())
    pairs = 0
    for count in anagram_counts:
        if count > 1:
            pairs += anagram_counts[count] * (count * (count - 1)) // 2
    return pairs >= 277