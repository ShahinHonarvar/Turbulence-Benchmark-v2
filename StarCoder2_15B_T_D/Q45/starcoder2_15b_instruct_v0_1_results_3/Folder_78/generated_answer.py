def palindromes_between_indices(string):
    chars = [c for c in string if c.isalpha()]
    chars_between_indices = [c for c in chars[6:9]]
    palindromes = set()
    for i in range(len(chars_between_indices)):
        for j in range(i + 1, len(chars_between_indices) + 1):
            palindrome = ''.join(chars_between_indices[i:j])
            if len(palindrome) >= 3 and palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes