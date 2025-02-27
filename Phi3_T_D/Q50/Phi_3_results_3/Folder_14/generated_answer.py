from collections import defaultdict

def if_contains_anagrams(strings):

    def add_sorted_to_buckets(char_buckets):
        for word in strings:
            if len(word) < 3:
                continue
            word_key = tuple(sorted(word.lower()))
            char_buckets[word_key].append(word)

    def count_anagram_pairs(char_buckets):
        return sum((len(anagrams) * (len(anagrams) - 1) // 2 for anagrams in char_buckets.values()))
    anagram_buckets = defaultdict(list)
    add_sorted_to_buckets(anagram_buckets)
    anagram_count = count_anagram_pairs(anagram_buckets)
    return anagram_count >= 22