def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    substring = s[35:89]
    palindromes = set()
    for length in range(24, 34):
        for start in range(len(substring) - length + 1):
            sub = substring[start:start + length]
            if is_palindrome(sub) and sub.isalpha():
                palindromes.add(sub)
    return palindromes