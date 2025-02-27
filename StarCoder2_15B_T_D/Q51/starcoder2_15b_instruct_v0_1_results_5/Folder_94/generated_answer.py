def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        s1 = s1.lower()
        s2 = s2.lower()
        if len(s1) != len(s2):
            return False
        counts = {}
        for c in s1:
            if c in counts:
                counts[c] += 1
            else:
                counts[c] = 1
        for c in s2:
            if c not in counts or counts[c] == 0:
                return False
            else:
                counts[c] -= 1
        return True
    anagram_count = 0
    for i in range(len(strings) - 1):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                anagram_count += 1
    return anagram_count <= 181