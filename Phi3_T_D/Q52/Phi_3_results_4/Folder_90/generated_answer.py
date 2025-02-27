def palindrome_of_length_n(s):
    s = s.lower()
    ans_set = {s[i:i + 318] for i in range(len(s) - 317) if s[i:i + 318:1] == s[i:i + 318:-1]}
    return {e for e in ans_set if e.isalpha()}