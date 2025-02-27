from itertools import combinations

def if_contains_anagrams(strings_list):

    def normalize(s):
        return ''.join(sorted(s.lower()))

    def has_anagram_more_than_count(string, strings_list, count):
        anagrams = [s for s in strings_list if normalize(s) == normalize(string) and s.lower() != string.lower()]
        return len(anagrams) > count
    for string in strings_list:
        if len(string) < 3:
            continue
        for s1, s2 in combinations(strings_list, 2):
            if normalize(s1) == normalize(s2) and len(set(s1.lower()) & set(string.lower())) == len(set(s1.lower())):
                return False
    return True