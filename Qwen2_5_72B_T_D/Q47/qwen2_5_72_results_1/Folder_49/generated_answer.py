def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    s = s[10:101]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 10, i + 51):
            if j <= len(s):
                sub = s[i:j]
                if sub.isalpha() and is_palindrome(sub):
                    palindromes.add(sub.lower())
    return palindromes