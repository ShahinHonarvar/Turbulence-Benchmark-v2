def palindromes_between_indices(string):
    chars = [c for c in string if c.isalpha()]
    chars = [c.lower() for c in chars]
    result = set()
    for i in range(2, len(chars) - 1):
        for j in range(i + 1, len(chars)):
            palindrome = chars[i:j + 1]
            if len(palindrome) >= 3:
                result.add(''.join(palindrome))
    return result