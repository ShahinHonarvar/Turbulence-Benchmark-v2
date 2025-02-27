def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(100, 301):
        if i + 50 <= 300:
            substring = text[i:i + 50]
            for j in range(len(substring)):
                if substring[j] == substring[j][::-1]:
                    palindromes.add(substring[j])
        if i + 100 <= 300:
            substring = text[i:i + 100]
            for j in range(len(substring)):
                if substring[j] == substring[j][::-1]:
                    palindromes.add(substring[j])
    return palindromes