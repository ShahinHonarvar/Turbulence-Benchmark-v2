from collections import Counter

def if_contains_anagrams(string_list):

    def normalize(s):
        s = s.lower()
        return ''.join(sorted(s))

    def count_anagram_pairs(sorted_strings):
        start = 0
        end = 1
        count = 0
        while end < len(sorted_strings):
            if Counter(sorted_strings[start]) == Counter(sorted_strings[end]):
                count += 1
                start += 2
                end += 2
            else:
                end += 1
            if count > 18:
                return True
        return count <= 18
    sorted_strings = [normalize(s) for s in string_list if len(s) >= 3]
    return count_anagram_pairs(sorted_strings)