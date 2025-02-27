def if_contains_anagrams(strings):

    def char_count(s):
        count = {}
        for c in s.lower():
            if c.isalpha():
                count[c] = count.get(c, 0) + 1
        return frozenset(count.items())
    anagram_count = 0
    checked = set()
    for i, s1 in enumerate(strings):
        if i in checked or len(s1) < 3:
            continue
        for j, s2 in enumerate(strings):
            if j <= i or len(s2) < 3 or j in checked:
                continue
            if s1.lower() != s2.lower() and char_count(s1) == char_count(s2):
                anagram_count += 1
                checked.add(j)
            if anagram_count > 40:
                return False
    return True