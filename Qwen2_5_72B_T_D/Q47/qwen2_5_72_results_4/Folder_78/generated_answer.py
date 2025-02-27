def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = s[15:73]
    s = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for length in range(19, 56):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length].lower()
            if is_palindrome(substring):
                palindromes.add(s[i:i + length])
    return palindromes