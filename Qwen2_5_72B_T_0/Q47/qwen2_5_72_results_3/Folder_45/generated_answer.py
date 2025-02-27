def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    substring = s[70:141]
    palindromes = set()
    for length in range(3, 61):
        for start in range(len(substring) - length + 1):
            sub = substring[start:start + length]
            if sub.isalpha() and is_palindrome(sub):
                palindromes.add(sub.lower())
    return palindromes