def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        str1 = str1.lower()
        str2 = str2.lower()
        return sorted(str1) == sorted(str2)

    def is_english_letter(char):
        return char.isalpha()

    def is_long_enough(str):
        return len(str) >= 3

    def are_strings_similar(str1, str2):
        return is_english_letter(str1) and is_english_letter(str2) and is_long_enough(str1) and is_long_enough(str2)

    def are_strings_anagrams(str1, str2):
        return are_strings_similar(str1, str2) and is_anagram(str1, str2)

    def count_anagrams(strings):
        anagrams = 0
        for i in range(len(strings) - 1):
            for j in range(i + 1, len(strings)):
                if are_strings_anagrams(strings[i], strings[j]):
                    anagrams += 1
        return anagrams

    def check_anagram_count(strings):
        return count_anagrams(strings) <= 49
    return check_anagram_count(strings)