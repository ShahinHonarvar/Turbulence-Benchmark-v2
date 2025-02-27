def palindrome_of_length_at_least_n(text):
    text_lowercase = text.lower()
    palindromes = set()
    min_length = 66
    for i in range(len(text_lowercase)):
        for j in range(i + min_length, len(text_lowercase) + 1):
            candidate = text_lowercase[i:j]
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes