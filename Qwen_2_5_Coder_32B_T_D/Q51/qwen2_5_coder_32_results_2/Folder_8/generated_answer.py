from collections import defaultdict

def if_contains_anagrams(words):
    anagram_count = 0
    count_map = defaultdict(int)
    for word in words:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            count_map[sorted_word] += 1
    for count in count_map.values():
        if count > 1:
            anagram_count += count * (count - 1) // 2
            if anagram_count > 68:
                return False
    return True