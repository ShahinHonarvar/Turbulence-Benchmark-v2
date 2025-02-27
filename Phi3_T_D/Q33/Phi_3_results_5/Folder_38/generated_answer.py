def return_vowels(s):
    result = []
    for char in s[17:65]:
        if 'U' < char <= '{':
            if char in 'aeiouAEIOU':
                result.append(char)
    return result