def palindromes_of_specific_lengths(s):
    s_slice = s[26:88]
    results = {s_slice[i:j] for i in range(len(s_slice)) for j in range(i + 52, i + 57) if s_slice[i:j].isalpha() and s_slice[i:j].lower() == s_slice[i:j][::-1]}
    return results