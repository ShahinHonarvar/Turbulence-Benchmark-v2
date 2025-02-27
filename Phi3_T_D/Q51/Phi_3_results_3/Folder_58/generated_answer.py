def if_contains_anagrams(words):
    anagram_count = 0
    letters_to_compare = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ']
    words = [word.upper() for word in words]

    def is_anagram(s1, s2):
        if sorted(s1) == sorted(s2) and s1 != s2:
            return True
        return False
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if len(words[i]) >= 3 and len(words[j]) >= 3:
                if is_anagram(words[i], words[j]):
                    anagram_count += 1
                    if anagram_count > 60:
                        return False
    return True