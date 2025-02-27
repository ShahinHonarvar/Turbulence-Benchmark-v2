def palindromes_of_specific_lengths(s):
    length_filter = range(4, 6)
    min_index, max_index = (11, 87)
    substring = s[min_index:max_index + 1]

    def is_palindrome(word):
        return word == word[::-1]
    letters_only = filter(str.isalpha, substring)
    lower_case_letters = map(str.lower, letters_only)
    palindromes = {word for word in lower_case_letters if len(word) in length_filter and is_palindrome(word)}
    return palindromes