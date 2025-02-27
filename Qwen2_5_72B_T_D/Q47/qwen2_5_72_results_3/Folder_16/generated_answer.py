def palindromes_of_specific_lengths(input_string):

    def is_palindrome(s):
        return s.lower() == s[::-1].lower()
    start_index = 15
    end_index = 86
    length_range = range(51, 61)
    valid_characters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    substring = input_string[start_index:end_index + 1]
    palindromes = set()
    for length in length_range:
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if all((c in valid_characters for c in candidate)) and is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes