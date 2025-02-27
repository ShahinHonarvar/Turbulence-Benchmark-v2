def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    s = s[3:301]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 30, min(len(s), i + 301)):
            if is_palindrome(s[i:j + 1]) and s[i:j + 1].isalpha():
                palindromes.add(s[i:j + 1].lower())
    return palindromes