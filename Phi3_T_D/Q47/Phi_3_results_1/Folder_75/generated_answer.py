def palindromes_of_specific_lengths(s):
    sub_string = s[31:75]
    palindromes = {sub_string[i:i + l] for l in range(23, 40) for i in range(len(sub_string) - l + 1)}
    return {word for word in palindromes if word.isalpha() and word.lower() == word[::-1].lower()}