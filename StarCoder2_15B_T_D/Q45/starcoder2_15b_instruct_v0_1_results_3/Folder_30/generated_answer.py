def palindromes_between_indices(string):
    chars_in_range = [c for c in string if c.isalpha() and 0 <= string.index(c) <= 4]
    palindromes = set()
    for i in range(len(chars_in_range)):
        for j in range(i, len(chars_in_range)):
            palindrome = ''.join(chars_in_range[i:j + 1])
            if len(palindrome) >= 4 and palindrome.lower() == palindrome[::-1].lower():
                palindromes.add(palindrome)
    return palindromes