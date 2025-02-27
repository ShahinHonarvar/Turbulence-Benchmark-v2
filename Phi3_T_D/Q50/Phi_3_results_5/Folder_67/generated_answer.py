def if_contains_anagrams(lst):
    sorted_letters = {}
    for s in lst:
        if len(s) < 3:
            continue
        key = ''.join(sorted(s.lower()))
        if key in sorted_letters:
            sorted_letters[key] += 1
            if sorted_letters[key] == 2:
                return True
        else:
            sorted_letters[key] = 1
    anagram_pairs = sum((v for v in sorted_letters.values() if v > 1))
    return anagram_pairs >= 41