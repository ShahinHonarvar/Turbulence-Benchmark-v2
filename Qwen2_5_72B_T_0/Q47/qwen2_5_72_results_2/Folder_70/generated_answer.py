def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    valid_palindromes = set()
    s = s[10:71]
    for i in range(len(s)):
        for j in range(i + 24, min(i + 53, len(s) + 1)):
            substring = s[i:j]
            if substring.isalpha() and is_palindrome(substring):
                valid_palindromes.add(substring)
    return valid_palindromes