def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    s = s[39:95]
    palindromes = set()
    for start in range(len(s)):
        for end in range(start + 14, min(start + 53, len(s) + 1)):
            if is_palindrome(s[start:end]) and s[start:end].isalpha():
                palindromes.add(s[start:end])
    return palindromes