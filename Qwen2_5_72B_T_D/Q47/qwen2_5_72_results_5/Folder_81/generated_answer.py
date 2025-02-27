def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s.lower() == s.lower()[::-1]
    filtered_str = s[12:123]
    palindromes = set()
    for length in range(12, 221):
        for start in range(len(filtered_str) - length + 1):
            substring = filtered_str[start:start + length]
            if substring.isalpha() and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes