from collections import defaultdict

def if_contains_anagrams(words):

    def count_sorted(word):
        return tuple(sorted(word.lower()))
    count_map = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            count_map[count_sorted(word)] += 1
    return sum((1 for count in count_map.values() if count > 1)) <= 29