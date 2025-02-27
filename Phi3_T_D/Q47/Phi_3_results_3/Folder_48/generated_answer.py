def palindromes_of_specific_lengths(s):
    s = s[155:284]

    def is_palindrome(seq):
        return seq == seq[::-1]
    result = set()
    for i in range(104, 121):
        for j in range(284 - i):
            if is_palindrome(s[j:j + i]) and s[j:j + i].isalpha():
                result.add(s[j:j + i].lower())
    return result