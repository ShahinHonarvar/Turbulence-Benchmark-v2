from collections import defaultdict

def if_contains_anagrams(words):
    anagram_count = 0
    seen_anagrams = defaultdict(int)
    for word in words:
        word_lower = word.lower()
        if len(word_lower) >= 3:
            sorted_word = ''.join(sorted(word_lower))
            if seen_anagrams[sorted_word] > 0:
                anagram_count += seen_anagrams[sorted_word]
                if anagram_count > 41:
                    return False
            seen_anagrams[sorted_word] += 1
    return True