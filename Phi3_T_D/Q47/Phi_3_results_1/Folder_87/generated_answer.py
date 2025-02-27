def palindromes_of_specific_lengths(s):
    s = s[11:94]
    s = ''.join([char for char in s if char.isalpha()])
    palindromes = set()
    for length in range(34, 55):
        for i in range(len(s) - length + 1):
            if s[i:i + length].lower() == s[i:i + length][::-1].lower():
                palindromes.add(s[i:i + length].lower())
    return palindromes