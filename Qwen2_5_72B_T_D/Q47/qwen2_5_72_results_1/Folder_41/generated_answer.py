def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    substring = s[1:8]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 3, min(len(substring) + 1, i + 5)):
            sub = substring[i:j]
            if sub.isalpha() and is_palindrome(sub):
                palindromes.add(sub.lower())
    return palindromes