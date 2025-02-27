def palindromes_of_specific_lengths(s):

    def is_palindrome(t):
        return t == t[::-1]
    s = s[10:60]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 18, i + 37):
            if j <= len(s):
                candidate = s[i:j].lower()
                if candidate.isalpha() and is_palindrome(candidate):
                    palindromes.add(candidate)
    return palindromes