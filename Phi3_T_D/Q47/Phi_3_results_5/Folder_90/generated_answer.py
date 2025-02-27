def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = set()
    s_subset = s[106:281]
    for i in range(136, 152):
        for j in range(281 - i):
            substring = s_subset[j:j + i]
            if substring.isalpha() and is_palindrome(substring.lower()):
                palindromes.add(substring)
    return palindromes