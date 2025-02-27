from collections import Counter, defaultdict

def if_contains_anagrams(words):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    length_counter = defaultdict(lambda: Counter())
    for word in words:
        if len(word) >= 3:
            sorted_word = tuple(sorted(word.lower()))
            length_counter[len(sorted_word)][sorted_word] += 1
    pairs_count = 0
    for count in length_counter.values():
        for _, value in count.items():
            pairs_count += value * (value - 1) // 2
    return pairs_count >= 46