from collections import Counter

def if_contains_anagrams(lst):

    def count_anagrams(arr):
        count = 0
        for word in arr:
            if len(word) >= 3:
                sorted_word = ''.join(sorted(word.lower()))
                count += len(list(Counter(sorted_word).values())) - 1
        return count
    return count_anagrams(lst) >= 123