def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return len(set(s1.lower()).difference(s2.lower())) == 0
    pairs = 0
    seen = []
    for i, str1 in enumerate(lst):
        for str2 in lst[i + 1:]:
            if str1.lower() != str2.lower() and len(str1) >= 3 and (len(str2) >= 3) and is_anagram(str1, str2):
                pair_key = ''.join(sorted(str1.lower()))
                if pair_key not in seen:
                    seen.append(pair_key)
                    pairs += 1
                    if pairs > 6:
                        return False
    return True