def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    substring = s[11:97].lower()
    for i in range(len(substring)):
        for j in range(i + 45, i + 53):
            if j <= len(substring):
                candidate = substring[i:j]
                if candidate.isalpha() and is_palindrome(candidate):
                    palindromes.add(candidate)
    return palindromes