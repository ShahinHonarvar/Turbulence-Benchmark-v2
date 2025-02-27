def palindromes_of_specific_lengths(s):
    substring = s[12:57]
    palindromes = set()
    for i in range(len(substring)):
        for length in range(20, 22):
            if i + length > len(substring):
                break
            if substring[i:i + length].lower() == substring[i:i + length][::-1] and substring[i:i + length].isalpha():
                palindromes.add(substring[i:i + length])
    return palindromes