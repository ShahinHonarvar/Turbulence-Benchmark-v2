import itertools

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    count = 0
    for pair in itertools.combinations(strings, 2):
        if len(pair[0]) >= 3 and len(pair[1]) >= 3:
            if is_anagram(pair[0], pair[1]):
                count += 1
                if count > 55:
                    return False
    return True