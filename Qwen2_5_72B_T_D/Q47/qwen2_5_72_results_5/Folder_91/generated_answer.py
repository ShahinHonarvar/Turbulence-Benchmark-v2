def palindromes_of_specific_lengths(s):

    def is_palindrome(x):
        return x.lower() == x[::-1].lower()
    s = s[:11]
    palindromes = set()
    for length in range(3, 6):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if is_palindrome(substring) and substring.isalpha():
                palindromes.add(substring.lower())
    return palindromes