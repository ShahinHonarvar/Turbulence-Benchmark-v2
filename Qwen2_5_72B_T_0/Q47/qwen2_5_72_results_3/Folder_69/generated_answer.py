def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    s = s[11:97]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 45, i + 53):
            if j <= len(s):
                sub = s[i:j]
                if sub.isalpha() and is_palindrome(sub):
                    palindromes.add(sub.lower())
    return palindromes