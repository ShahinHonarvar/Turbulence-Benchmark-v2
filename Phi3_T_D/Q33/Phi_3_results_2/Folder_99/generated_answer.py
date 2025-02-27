def return_vowels(s):
    indices = [i for i in range(323, 527) if '!' <= s[i] <= ':']
    return [s[i] for i in indices if s[i] in 'aeiouAEIOU']