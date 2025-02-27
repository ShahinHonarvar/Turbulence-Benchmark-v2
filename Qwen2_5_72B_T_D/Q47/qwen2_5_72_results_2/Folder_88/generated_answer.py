def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s[11:88]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 3, i + 6):
            if j <= len(s):
                sub = s[i:j].lower()
                if sub.isalpha() and is_palindrome(sub):
                    palindromes.add(sub)
    return palindromes