def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    seen = set()
    for s in strings:
        if len(s) >= 3:
            n = normalize(s)
            if n in seen:
                anagram_count += 1
                if anagram_count >= 57:
                    return True
            seen.add(n)
    return False