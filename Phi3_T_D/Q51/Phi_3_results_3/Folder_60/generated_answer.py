from collections import defaultdict

def if_contains_anagrams(string_list):

    def count_letters(word):
        return ''.join(sorted(word.lower()))
    anagram_count = 0
    counter = defaultdict(int)
    for s in string_list:
        if len(s) >= 3:
            key = count_letters(s)
            anagram_count += counter[key]
            counter[key] += 1
            if anagram_count > 77:
                return False
    return True