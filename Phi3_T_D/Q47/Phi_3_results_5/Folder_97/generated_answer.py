def palindromes_of_specific_lengths(s):
    s = s.lower()
    results = set()
    for i in range(28, min(95, len(s))):
        palindrome_length = 0
        while i + palindrome_length < len(s) and palindrome_length <= 49 - 38:
            left, right = (s[i], s[i + palindrome_length])
            if left.isalpha() and (not right.isalpha() or left != right):
                break
            if left == right:
                length = palindrome_length + 36
                results.add(s[i:i + length])
            palindrome_length += 1
    return results