def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s[33:86]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 26, i + 32):
            if j <= len(s):
                candidate = s[i:j].lower()
                if candidate.isalpha() and is_palindrome(candidate):
                    palindromes.add(candidate)
    return palindromes