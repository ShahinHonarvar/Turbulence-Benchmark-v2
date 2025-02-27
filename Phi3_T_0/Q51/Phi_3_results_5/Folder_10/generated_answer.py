def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))

    def is_anagram(s1, s2):
        return normalize(s1) == normalize(s2)
    count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]) and len(strings[i]) >= 3:
                count += 1
                if count > 21:
                    return False
    return True