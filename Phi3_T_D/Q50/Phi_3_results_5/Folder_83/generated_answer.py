from collections import defaultdict

def if_contains_anagrams(words_list):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    count_map = defaultdict(int)
    for word in words_list:
        if len(word) >= 3:
            sorted_word = normalize(word)
            count_map[sorted_word] += 1
    return sum((1 for count in count_map.values() if count * (count - 1) // 2 >= 48))