def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    count = 0
    n = len(strings)
    for i in range(n):
        for j in range(i + 1, n):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3 and is_anagram(strings[i], strings[j]):
                count += 1
                if count >= 69:
                    return True
    return False