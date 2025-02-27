def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    count = 0
    length = len(strings)
    for i in range(length):
        for j in range(i + 1, length):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                if is_anagram(strings[i], strings[j]):
                    count += 1
        if count >= 92:
            return True
    return False