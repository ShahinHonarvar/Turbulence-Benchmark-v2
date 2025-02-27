def palindrome_of_length_n(s):

    def is_palindrome(test_str):
        return test_str == test_str[::-1]
    palindromes = set()
    s_lower = s.lower()
    for i in range(len(s_lower) - 52):
        substring = s_lower[i:i + 53]
        if is_palindrome(substring):
            palindromes.add(substring.upper())
    return palindromes