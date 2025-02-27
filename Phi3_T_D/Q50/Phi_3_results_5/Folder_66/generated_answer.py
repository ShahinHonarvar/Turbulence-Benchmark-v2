def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    for i, s1 in enumerate(strings):
        for s2 in strings[i + 1:]:
            if len(s1) >= 3 and len(s2) >= 3 and (normalize(s1) == normalize(s2)):
                anagram_count += 1
                if anagram_count >= 92:
                    return True
    return False