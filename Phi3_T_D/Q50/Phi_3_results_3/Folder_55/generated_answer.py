from collections import defaultdict

def if_contains_anagrams(string_list):
    anagrams = defaultdict(list)
    for word in string_list:
        if len(word) >= 3:
            cleaned_word = word.lower()
            key = ''.join(sorted(cleaned_word))
            anagrams[key].append(word)
    count = 0
    for key in anagrams:
        if len(anagrams[key]) >= 2:
            count += len(anagrams[key]) * (len(anagrams[key]) - 1) // 2
    return count >= 15