import itertools

def if_contains_anagrams(strings):
    pairs = 0
    for pair in itertools.combinations(strings, 2):
        if sorted(pair[0].lower()) == sorted(pair[1].lower()) and len(pair[0]) >= 3:
            pairs += 1
            if pairs >= 11:
                return True
    return False