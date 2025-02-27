def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        s1, s2 = (s1.lower(), s2.lower())
        return len(s1) == len(s2) and sorted(s1) == sorted(s2)
    count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]) and len(strings[i]) >= 3:
                count += 1
    return count >= 20