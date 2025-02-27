def if_contains_anagrams(strings_list):

    def count_letters(word):
        letter_counts = {}
        for letter in word.lower():
            if letter.isalpha():
                if letter not in letter_counts:
                    letter_counts[letter] = 0
                letter_counts[letter] += 1
        return letter_counts

    def are_anagrams(word1, word2):
        return count_letters(word1) == count_letters(word2)
    anagram_count = 0
    list_length = len(strings_list)
    for i in range(list_length):
        for j in range(i + 1, list_length):
            if len(strings_list[i]) >= 3 and len(strings_list[j]) >= 3:
                if are_anagrams(strings_list[i], strings_list[j]):
                    anagram_count += 1
                    if anagram_count >= 79:
                        return True
    return False