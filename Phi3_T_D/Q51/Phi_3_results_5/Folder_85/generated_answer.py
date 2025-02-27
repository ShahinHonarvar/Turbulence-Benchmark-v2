from collections import defaultdict

def if_contains_anagrams(words):
    anagrams_dict = defaultdict(int)
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        anagrams_dict[sorted_word] += 1
    count = 0
    for val in anagrams_dict.values():
        count += val * (val - 1) // 2
    return count <= 276