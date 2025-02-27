def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s[45:99]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 40, i + 48):
            if j <= len(s):
                sub = s[i:j]
                if sub.isalpha() and is_palindrome(sub.lower()):
                    palindromes.add(sub)
    return palindromes