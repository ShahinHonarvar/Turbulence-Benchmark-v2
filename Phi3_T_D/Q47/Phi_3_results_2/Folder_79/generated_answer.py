def palindromes_of_specific_lengths(s):
    sub_str = s[1:9]
    palindromes = {sub_str[i:j + 1].lower() for i in range(len(sub_str) - 2) for j in range(i + 2, len(sub_str)) if sub_str[i:j + 1].isalpha() and sub_str[i:j + 1] == sub_str[i:j + 1][::-1]}
    return set(filter(lambda palindrome: 3 <= len(palindrome) <= 4, palindromes))