def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)
    anagram_pairs = 0
    strings = [s.lower() for s in strings if len(s) >= 3]
    checked = set()
    for i in range(len(strings)):
        if strings[i] in checked:
            continue
        checked.add(strings[i])
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                anagram_pairs += 1
                checked.add(strings[j])
    return anagram_pairs <= 41