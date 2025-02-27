from collections import defaultdict

def if_contains_anagrams(words):

    def count_chars(word):
        count = defaultdict(int)
        for char in word:
            count[char.lower()] += 1
        return tuple(sorted(count.items()))
    anagram_count = 0
    char_counts = {}
    for word in words:
        if len(word) < 3:
            continue
        char_count = count_chars(word)
        if char_count in char_counts:
            anagram_count += char_counts[char_count]
            char_counts[char_count] += 1
        else:
            char_counts[char_count] = 1
        if anagram_count > 210:
            return False
    return True