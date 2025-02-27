def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    substring = s[119:257]
    palindromes = set()
    for length in range(104, 124):
        for start in range(len(substring) - length + 1):
            sub = substring[start:start + length]
            if sub.isalpha() and is_palindrome(sub):
                palindromes.add(sub)
    return palindromes