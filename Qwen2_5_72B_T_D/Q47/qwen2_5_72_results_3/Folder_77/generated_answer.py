def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    substr = s[103:277]
    palindromes = set()
    for i in range(len(substr)):
        for j in range(i + 100, min(i + 170, len(substr) + 1)):
            if is_palindrome(substr[i:j]) and substr[i:j].isalpha():
                palindromes.add(substr[i:j])
    return palindromes