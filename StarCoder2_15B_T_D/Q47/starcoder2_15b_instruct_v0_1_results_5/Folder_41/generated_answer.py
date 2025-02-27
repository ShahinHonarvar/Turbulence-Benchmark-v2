def palindromes_of_specific_lengths(string):
    sub_string = string[1:8].lower()
    palindromes = set()
    for i in range(len(sub_string) - 2):
        for j in range(i + 3, min(i + 5, len(sub_string))):
            if sub_string[i:j] == sub_string[i:j][::-1]:
                palindromes.add(sub_string[i:j])
    return palindromes