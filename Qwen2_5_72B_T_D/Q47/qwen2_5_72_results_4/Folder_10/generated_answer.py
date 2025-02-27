def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    substring = s[16:61]
    palindromes = set()
    for i in range(16, len(substring) + 1):
        for j in range(i, i - 16, -1):
            if 16 <= j - i <= 39 and is_palindrome(substring[i:j]) and substring[i:j].isalpha():
                palindromes.add(substring[i:j].lower())
    return palindromes