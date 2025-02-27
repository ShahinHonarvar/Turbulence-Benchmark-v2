from collections import defaultdict

def if_contains_anagrams(words):

    def is_anagram(a, b):
        return sorted(a) == sorted(b)
    anagram_dict = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            anagram_dict[''.join(sorted(word.lower()))].append(word)
    count = 0
    for word_list in anagram_dict.values():
        if len(word_list) > 1:
            count += len(word_list) * (len(word_list) - 1) // 2
            if count >= 155:
                return True
    return False