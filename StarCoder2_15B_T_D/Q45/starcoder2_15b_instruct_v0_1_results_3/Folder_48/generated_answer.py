def palindromes_between_indices(text_string):
    text_string = text_string[6:9].lower()
    palindromes = set()
    for i in range(len(text_string)):
        for j in range(i + 4, len(text_string) + 1):
            palindrome = text_string[i:j]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes