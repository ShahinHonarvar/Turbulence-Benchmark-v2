def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    valid_palindromes = set()
    s = s[27:78]
    for i in range(len(s)):
        for j in range(i + 18, i + 20):
            if j <= len(s) and s[i:j].isalpha() and is_palindrome(s[i:j]):
                valid_palindromes.add(s[i:j].lower())
    return valid_palindromes