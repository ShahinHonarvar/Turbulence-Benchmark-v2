def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()

    def is_alpha(sub):
        return all((c.isalpha() for c in sub))
    substring = s[11:97]
    palindromes = set()
    for length in range(45, 53):
        for start in range(len(substring) - length + 1):
            sub = substring[start:start + length]
            if is_palindrome(sub) and is_alpha(sub):
                palindromes.add(sub.lower())
    return palindromes