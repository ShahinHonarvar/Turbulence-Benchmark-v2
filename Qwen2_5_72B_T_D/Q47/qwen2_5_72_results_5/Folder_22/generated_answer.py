def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    s = s[100:201]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 4, min(i + 11, len(s) + 1)):
            substr = s[i:j]
            if substr.isalpha() and is_palindrome(substr):
                palindromes.add(substr)
    return palindromes