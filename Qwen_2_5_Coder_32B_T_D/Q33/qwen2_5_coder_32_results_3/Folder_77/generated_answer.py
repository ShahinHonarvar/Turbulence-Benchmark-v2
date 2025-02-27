def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    result = []
    for i in range(max(837, 0), min(975, len(s))):
        if 'N' < s[i] <= 'W' and s[i] in vowels:
            result.append(s[i])
    return result