def if_contains_anagrams(words):

    def is_anagram(s1, s2):
        return sorted(s1.lower()).count(s2.lower()) == len(s2) and sorted(s1.lower()) == sorted(s2.lower())
    count = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if is_anagram(words[i], words[j]):
                count += 1
                if count > 4:
                    return False
    return True