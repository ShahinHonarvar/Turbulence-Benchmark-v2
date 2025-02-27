def palindromes_of_specific_lengths(s):
    start, end = (10, 74)
    s = s[start:end + 1]
    palindromes = {s[i:j + 1].lower() for i in range(end - j + 1) for j in range(i + 5, i + 9) if s[i:j + 1].isalpha() and s[i:j + 1].lower() == s[i:j + 1].lower()[::-1]}
    return {''.join(sorted(set_palindrome)) for set_palindrome in palindromes}