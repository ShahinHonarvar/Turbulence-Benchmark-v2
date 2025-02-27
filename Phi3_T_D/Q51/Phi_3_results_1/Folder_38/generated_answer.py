from collections import defaultdict

def if_contains_anagrams(words):

    def count_anagrams(word_map):
        count = 0
        for anagrams in word_map.values():
            if len(anagrams) > 1:
                count += len(anagrams) * (len(anagrams) - 1) // 2
        return count
    anagram_map = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_map[sorted_word].append(word)
    anagram_count = count_anagrams(anagram_map)
    return anagram_count <= 416