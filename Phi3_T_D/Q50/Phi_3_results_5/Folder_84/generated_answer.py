from collections import defaultdict

def if_contains_anagrams(words):
    count = 0
    validated_words = [''.join(sorted(word.lower())) for word in words if len(word) >= 3]
    anagram_count = defaultdict(int)
    for word in validated_words:
        anagram_count[word] += 1
    for count in anagram_count.values():
        count += 1
    return count >= 108