def palindromes_of_specific_lengths(input_string):

    def is_palindrome(s):
        return s == s[::-1]
    relevant_substring = input_string[16:78]
    palindromes_set = set()
    for length in range(43, 48):
        for start in range(len(relevant_substring) - length + 1):
            part = relevant_substring[start:start + length]
            if part.isalpha() and is_palindrome(part.lower()):
                palindromes_set.add(part)
    return palindromes_set