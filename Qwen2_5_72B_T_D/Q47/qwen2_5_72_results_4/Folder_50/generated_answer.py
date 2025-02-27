def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    substring = s[36:93]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 10, min(i + 36, len(substring)) + 1):
            current = substring[i:j]
            if current.isalpha() and is_palindrome(current):
                palindromes.add(current)
    return palindromes