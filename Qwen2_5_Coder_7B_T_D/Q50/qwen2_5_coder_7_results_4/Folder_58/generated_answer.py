from collections import defaultdict

def if_contains_anagrams(words):
    anagram_count = defaultdict(int)
    for word in words:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            anagram_count[sorted_word] += 1
    for count in anagram_count.values():
        if count >= 2:
            if count * (count - 1) // 2 >= 411:
                return True
    return False