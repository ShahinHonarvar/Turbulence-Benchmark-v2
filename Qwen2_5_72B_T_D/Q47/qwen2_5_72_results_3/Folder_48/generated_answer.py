def palindromes_of_specific_lengths(s):

    def is_palindrome(t):
        return t == t[::-1]
    s = s[155:284]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 104, i + 121):
            if j <= len(s):
                candidate = s[i:j]
                if candidate.isalpha() and is_palindrome(candidate.lower()):
                    palindromes.add(candidate)
    return palindromes