def palindromes_of_specific_lengths(s):

    def is_palindrome(t):
        return t == t[::-1]
    relevant_substring = s[24:98]
    palindromes_set = set()
    for length in range(10, 37):
        for start in range(len(relevant_substring) - length + 1):
            substring = relevant_substring[start:start + length]
            if substring.isalpha() and is_palindrome(substring.lower()):
                palindromes_set.add(substring)
    return palindromes_set