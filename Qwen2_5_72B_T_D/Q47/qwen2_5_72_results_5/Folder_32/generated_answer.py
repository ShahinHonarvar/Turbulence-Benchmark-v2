def palindromes_of_specific_lengths(s):

    def is_palindromesub(s):
        return s == s[::-1]
    palindromes = set()
    s = s[16:78].lower()
    for i in range(len(s)):
        for j in range(43, 48):
            if i + j <= len(s):
                sub = s[i:i + j]
                if sub.isalpha() and is_palindrome_sub(sub):
                    palindromes.add(sub)
    return palindromes