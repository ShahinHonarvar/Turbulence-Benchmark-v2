from collections import Counter

def if_contains_anagrams(lst):

    def count_anagrams(strings):
        anagram_count = 0
        for string in strings:
            string = string.lower()
            if len(string) >= 3:
                sorted_string = ''.join(sorted(string))
                counter = Counter(sorted_string)
                anagram_count += len(list(counter.values())) - 1
        return anagram_count // 2 >= 115
    return count_anagrams(lst)