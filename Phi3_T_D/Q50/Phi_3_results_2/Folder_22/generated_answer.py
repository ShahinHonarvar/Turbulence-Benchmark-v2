from itertools import combinations

def if_contains_anagrams(string_list):

    def clean_and_sort(s):
        return ''.join(sorted([c.lower() for c in s if c.isalpha()]))
    count = 0
    for combo in combinations(string_list, 2):
        if clean_and_sort(combo[0]) == clean_and_sort(combo[1]):
            count += 1
            if count >= 72:
                return True
    return False