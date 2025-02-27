def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(filter(str.isalpha, s1.lower())) == sorted(filter(str.isalpha, s2.lower()))
    count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]) and len(filter(str.isalpha, strings[i])) >= 3:
                count += 1
                if count >= 18:
                    return True
    return False