def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s[130:296]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 103, i + 159):
            if j <= len(s):
                substring = s[i:j]
                if substring.isalpha() and is_palindrome(substring.lower()):
                    palindromes.add(substring)
    return palindromes