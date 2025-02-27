def palindromes_of_specific_lengths(text):
    start, end = (33, 85)
    letters_only = text[start:end + 1].lower()
    palindrome_set = set()
    for length in range(26, 32):
        for i in range(len(letters_only) - length + 1):
            substring = letters_only[i:i + length]
            if substring == substring[::-1]:
                palindrome_set.add(substring)
    return palindrome_set