from collections import defaultdict

def if_contains_anagrams(words):
    anagram_dict = defaultdict(int)
    count = 0
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        anagram_dict[sorted_word] += 1
        count += anagram_dict[sorted_word] - 1
    return count >= 66