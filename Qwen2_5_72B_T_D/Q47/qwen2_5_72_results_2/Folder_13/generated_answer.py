def palindromes_of_specific_lengths(s):

    def is_palindrome(candidate):
        return candidate == candidate[::-1]
    specified_substring = s[13:96]
    valid_palindromes = set()
    for length in range(57, 61):
        for start in range(len(specified_substring) - length + 1):
            substring = specified_substring[start:start + length]
            if is_palindrome(substring) and substring.isalpha():
                valid_palindromes.add(substring.lower())
    return valid_palindromes