def palindromes_between_indices(text):
    chars_in_range = [c for c in text.lower() if 'a' <= c <= 'z' and 0 <= text.index(c) <= 6]
    palindromes = set()
    for length in range(3, len(chars_in_range) + 1):
        for i in range(len(chars_in_range) - length + 1):
            palindrome = ''.join(chars_in_range[i:i + length])
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes