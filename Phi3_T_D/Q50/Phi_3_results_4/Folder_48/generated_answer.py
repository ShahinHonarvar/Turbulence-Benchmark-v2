from collections import defaultdict

def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    words_dict = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            normalized = normalize(word)
            words_dict[normalized] += 1
    count_pairs = 0
    for count in words_dict.values():
        count_pairs += count * (count - 1) // 2
    return count_pairs >= 219