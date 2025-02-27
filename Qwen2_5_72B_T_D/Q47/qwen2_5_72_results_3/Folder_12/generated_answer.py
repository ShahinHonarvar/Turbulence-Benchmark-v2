def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s[62:89]
    palindromes = set()
    for i in range(len(s)):
        for j in range(18, 22):
            if i + j <= len(s):
                sub = s[i:i + j].lower()
                if sub.isalpha() and is_palindrome(sub):
                    palindromes.add(sub)
    return palindromes