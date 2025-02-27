def palindromes_of_specific_lengths(s):

    def is_palindrome(t):
        return t == t[::-1]
    substring = s[103:277]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 100, i + 170):
            if j <= len(substring):
                candidate = substring[i:j]
                if candidate.isalpha() and is_palindrome(candidate.lower()):
                    palindromes.add(candidate)
    return palindromes