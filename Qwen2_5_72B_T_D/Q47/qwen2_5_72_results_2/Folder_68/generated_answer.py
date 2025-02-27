def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    s = s[:51]
    palindromes = set()
    for start in range(len(s)):
        for end in range(start + 50, min(len(s), start + 101)):
            substring = s[start:end]
            if is_palindrome(substring) and substring.isalpha():
                palindromes.add(substring)
    return palindromes