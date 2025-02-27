from collections import defaultdict

def if_contains_anagrams(words):
    anagram_count = defaultdict(int)
    anagrams = set()
    for word in words:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagrams:
                anagram_count[sorted_word] += 1
            else:
                anagrams.add(sorted_word)
    total_anagram_pairs = sum((count for count in anagram_count.values() if count > 0))
    return total_anagram_pairs <= 55