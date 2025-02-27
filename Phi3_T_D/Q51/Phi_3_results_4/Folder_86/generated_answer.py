def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        if len(s1) != len(s2):
            return False
        return sorted(s1.lower()) == sorted(s2.lower())
    count = 0
    length = len(strings)
    for i in range(length):
        for j in range(i + 1, length):
            if is_anagram(strings[i], strings[j]):
                count += 1
                if count > 48:
                    return False
    return True