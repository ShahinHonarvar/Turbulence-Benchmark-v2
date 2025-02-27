def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        if sorted(str1.lower().replace(' ', '')) == sorted(str2.lower().replace(' ', '')):
            return True
        return False
    count = 0
    strings = [s.lower() for s in strings]
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3 and is_anagram(strings[i], strings[j]):
                count += 1
                if count > 22:
                    return False
    return True