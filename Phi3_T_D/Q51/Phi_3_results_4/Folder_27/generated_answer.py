def if_contains_anagrams(strings):

    def count_chars(s):
        return ''.join(sorted(s.lower()))
    pairs = 0
    checked = set()
    for i in range(len(strings)):
        current_anagram = count_chars(strings[i])
        for j in range(i + 1, len(strings)):
            if (i, j) not in checked and current_anagram == count_chars(strings[j]):
                pairs += 1
                if pairs > 113:
                    return False
                checked.add((i, j))
    return True