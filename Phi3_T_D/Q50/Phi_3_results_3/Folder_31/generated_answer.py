def if_contains_anagrams(strings):
    anagrams_count = 0

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]) and len(strings[i]) >= 3 and (len(strings[j]) >= 3):
                anagrams_count += 1
    return anagrams_count >= 68