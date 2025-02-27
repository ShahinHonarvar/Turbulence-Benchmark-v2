def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    s = s[15:87]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 51, min(i + 61, len(s) + 1)):
            if is_palindrome(s[i:j]) and s[i:j].isalpha():
                palindromes.add(s[i:j].lower())
    return palindromes