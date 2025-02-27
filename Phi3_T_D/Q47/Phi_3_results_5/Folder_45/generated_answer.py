def palindromes_of_specific_lengths(s):
    sub_string = s[70:141]
    return {sub_string[i:j] for i in range(len(sub_string)) for j in range(i + 3, min(i + 61, len(sub_string) + 1) + 1) if sub_string[i:j].lower() == sub_string[i:j][::-1] and sub_string[i:j].isalpha()}