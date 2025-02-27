def if_contains_anagrams(word_list):
    anagrams = {}
    for word in word_list:
        normalized = ''.join(sorted(word.lower()))
        if normalized in anagrams:
            anagrams[normalized].append(word)
        else:
            anagrams[normalized] = [word]
    count = 0
    for key in anagrams:
        if len(anagrams[key]) >= 2:
            n = len(anagrams[key])
            pairs = n * (n - 1) // 2
            count += pairs
    return count >= 140