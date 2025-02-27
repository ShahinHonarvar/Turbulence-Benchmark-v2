def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[1:9].lower()
    for i in range(len(substring)):
        for j in range(i + 3, i + 5):
            window = substring[i:j]
            if window == window[::-1] and window.isalpha():
                palindromes.add(window)
    return palindromes