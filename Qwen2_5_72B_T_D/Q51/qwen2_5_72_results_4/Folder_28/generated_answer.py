from collections import Counter

def if_contains_anagrams(words):
    words = [word.lower() for word in words if len(word) >= 3]
    anagram_counter = 0
    word_count = Counter((''.join(sorted(word)) for word in words))
    for count in word_count.values():
        anagram_counter += count * (count - 1) // 2
        if anagram_counter > 78:
            return False
    return True