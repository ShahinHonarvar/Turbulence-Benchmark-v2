def palindrome_of_length_n(s: str) -> set:
    result = set()
    s = s.lower()
    for i in range(len(s) - 8):
        palindrome_candidate = s[i:i + 9]
        if palindrome_candidate == palindrome_candidate[::-1]:
            result.add(palindrome_candidate)
    return result