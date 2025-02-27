def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    substring = s[17:96]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 13, min(i + 50, len(substring) + 1)):
            if is_palindrome(substring[i:j]) and substring[i:j].isalpha():
                palindromes.add(substring[i:j])
    return palindromes