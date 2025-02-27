def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower()) and len(s1) >= 3
    count = 0
    seen = set()
    for word in lst:
        for perm in itertools.permutations(word, len(word)):
            anagram = ''.join(perm).lower()
            if is_anagram(word, anagram):
                pair = tuple(sorted([word.lower(), anagram]))
                if pair in seen:
                    count += 1
                    if count > 3:
                        return False
                    break
                seen.add(pair)
    return True