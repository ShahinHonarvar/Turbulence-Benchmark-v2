def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    target = s[106:281]
    palindromes = set()
    for length in range(136, 152):
        for start in range(len(target) - length + 1):
            sub = target[start:start + length]
            if is_palindrome(sub) and sub.isalpha():
                palindromes.add(sub)
    return palindromes