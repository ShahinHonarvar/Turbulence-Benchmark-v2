def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        s1 = s1.lower()
        s2 = s2.lower()
        return sorted(s1) == sorted(s2)

    def is_english_letters(s):
        return all((ch.isalpha() for ch in s))

    def is_length_of_at_least_three(s):
        return len(s) >= 3
    anagram_count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            s1 = strings[i]
            s2 = strings[j]
            if is_english_letters(s1) and is_english_letters(s2) and is_length_of_at_least_three(s1) and is_length_of_at_least_three(s2) and is_anagram(s1, s2):
                anagram_count += 1
    return anagram_count <= 73