import itertools

def if_contains_anagrams(strings):

    def count_letters(word):
        return sorted(word.lower())
    anagram_count = 0
    for a, b in itertools.combinations(strings, 2):
        if len(set(a) & set(b)) < len(set(a)) or len(set(a) & set(b)) < len(set(b)):
            continue
        if count_letters(a) == count_letters(b) and len(a) >= 3:
            anagram_count += 1
            if anagram_count > 10:
                return False
    return True