def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    valid_palindromes = set()
    s = s[10:101]
    for i in range(len(s)):
        for j in range(i + 10, min(i + 51, len(s) + 1)):
            if is_palindrome(s[i:j]) and s[i:j].isalpha():
                valid_palindromes.add(s[i:j].lower())
    return valid_palindromes