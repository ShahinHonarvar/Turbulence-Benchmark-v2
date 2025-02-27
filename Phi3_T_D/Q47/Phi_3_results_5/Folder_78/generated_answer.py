def palindromes_of_specific_lengths(input_string):
    substr = input_string[15:73]

    def is_valid_palindrome(s):
        return s == s[::-1] and 19 <= len(s) <= 55

    def contains_only_english_letters(s):
        return all(('A' <= char.upper() <= 'Z' for char in s))
    palindromes = {substr[i:j + 1] for i in range(len(substr)) for j in range(i, len(substr)) if is_valid_palindrome(substr[i:j + 1]) and contains_only_english_letters(substr[i:j + 1])}
    return palindromes