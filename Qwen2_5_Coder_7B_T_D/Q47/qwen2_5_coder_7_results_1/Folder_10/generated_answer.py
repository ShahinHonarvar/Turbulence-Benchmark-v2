def palindromes_of_specific_lengths(s):

    def is_palindrome(subs):
        return subs.lower() == subs[::-1].lower()
    result = set()
    for length in range(16, 40):
        for start in range(16, 61 - length):
            subs = s[start:start + length]
            if is_palindrome(subs) and subs.isalpha():
                result.add(subs)
    return result