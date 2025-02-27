def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    palindromes = set()
    s = s[100:301]
    for i in range(len(s)):
        for j in range(i + 50, i + 101):
            if j <= len(s):
                sub = s[i:j]
                if sub.isalpha() and is_palindrome(sub):
                    palindromes.add(sub)
    return palindromes