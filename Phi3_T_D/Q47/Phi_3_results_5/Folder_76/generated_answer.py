def palindromes_of_specific_lengths(s):
    start, end = (101, 292)
    subset = s[start - 1:end].lower()
    palindromes = set()
    for length in range(154, 183):
        for i in range(end - length + 1):
            if subset[i:i + length] == subset[i:i + length][::-1]:
                palindromes.add(subset[i:i + length])
    return {palindrome.upper() for palindrome in palindromes}