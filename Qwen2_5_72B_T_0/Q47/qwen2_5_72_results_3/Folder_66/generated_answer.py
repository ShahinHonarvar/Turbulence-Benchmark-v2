def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    substring = s[32:80]
    palindromes = set()
    for length in range(35, 42):
        for start in range(len(substring) - length + 1):
            sub = substring[start:start + length]
            if sub.isalpha() and is_palindrome(sub):
                palindromes.add(sub)
    return palindromes