def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    count = 0
    n = len(strings)
    for i in range(n):
        for j in range(i + 1, n):
            if is_anagram(strings[i], strings[j]) and len(strings[i]) >= 3:
                count += 1
                if count >= 19:
                    return True
    return False