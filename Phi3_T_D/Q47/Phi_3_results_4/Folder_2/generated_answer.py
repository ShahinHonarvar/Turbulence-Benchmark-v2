def palindromes_of_specific_lengths(s):

    def is_valid_character(char):
        return char.isalpha()

    def is_palindrome(word):
        return word == word[::-1]
    result_set = set()
    for length in range(18, 37):
        for i in range(10, 60 - length + 1):
            substr = s[i:i + length]
            if all((is_valid_character(c.lower()) for c in substr)) and is_palindrome(substr):
                result_set.add(substr.lower())
    return result_set