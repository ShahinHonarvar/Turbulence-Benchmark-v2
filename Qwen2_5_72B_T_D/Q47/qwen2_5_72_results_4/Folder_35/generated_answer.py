def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    result = set()
    substr = s[34:91]
    for i in range(len(substr)):
        for j in range(i + 14, min(i + 40, len(substr) + 1)):
            if is_palindrome(substr[i:j]) and substr[i:j].isalpha():
                result.add(substr[i:j].lower())
    return result