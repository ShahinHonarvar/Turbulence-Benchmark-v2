from collections import defaultdict

def if_contains_anagrams(words):
    anagrams_map = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            key = ''.join(sorted(word.lower()))
            anagrams_map[key].append(word)
    count = 0
    for key, word_list in anagrams_map.items():
        if len(word_list) > 1:
            count += len(word_list) * (len(word_list) - 1) // 2
    return count >= 312