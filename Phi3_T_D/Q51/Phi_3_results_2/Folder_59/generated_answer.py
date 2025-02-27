def if_contains_anagrams(strings):

    def count_chars(s):
        count = {}
        for char in s.lower():
            if char.isalpha():
                count[char] = count.get(char, 0) + 1
        return count

    def is_anagram(str1, str2):
        return count_chars(str1) == count_chars(str2)
    anagram_count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]) and len(strings[i]) >= 3:
                anagram_count += 1
                if anagram_count > 15:
                    return False
    return True