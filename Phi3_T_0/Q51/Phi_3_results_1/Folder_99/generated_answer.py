def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    checked = set()
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if normalize(strings[i]) == normalize(strings[j]):
                if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                    anagram_count += 1
                    if anagram_count > 93:
                        return False
                    checked.add(i)
                    checked.add(j)
    return True