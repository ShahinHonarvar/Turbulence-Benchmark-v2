from collections import defaultdict

def if_contains_anagrams(words):
    anagram_count = 0
    seen_anagrams = defaultdict(int)
    for word in words:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            seen_anagrams[sorted_word] += 1
            anagram_count += seen_anagrams[sorted_word] - 1
            if anagram_count > 40:
                return False
    return True