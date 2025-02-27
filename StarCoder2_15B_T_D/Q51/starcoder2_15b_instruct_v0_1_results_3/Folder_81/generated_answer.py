def get_anagrams(words):
    anagrams = {}
    for word in words:
        key = ''.join(sorted(word))
        if key in anagrams:
            anagrams[key].append(word)
        else:
            anagrams[key] = [word]
    return anagrams

def get_anagrams_of_length_three_or_more(words):
    anagrams = get_anagrams(words)
    return {key: value for key, value in anagrams.items() if len(key) >= 3}

def get_anagrams_case_insensitive(words):
    anagrams = get_anagrams_of_length_three_or_more(words)
    return {key: value for key, value in anagrams.items() if len(set(key.lower())) == len(key)}

def if_contains_anagrams(words):
    anagrams = get_anagrams_case_insensitive(words)
    return len(anagrams) <= 79