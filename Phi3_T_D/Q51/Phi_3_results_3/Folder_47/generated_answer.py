def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return sorted(str1.lower().replace(' ', '')) == sorted(str2.lower().replace(' ', '')) and len(str1) >= 3
    count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                count += 1
                if count > 366:
                    return False
    return True