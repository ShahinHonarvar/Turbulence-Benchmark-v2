def palindrome_of_length_n(s):
    s = s.lower()
    return {s[i:i + 45] for i in range(len(s) - 44) if s[i:i + 45] == s[i:i + 45][::-1]}