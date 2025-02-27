def if_contains_anagrams(string_list):
    anagrams = {}
    for word in string_list:
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word not in anagrams:
            anagrams[sorted_word] = []
        anagrams[sorted_word].append(word)
    count = 0
    for key, words in anagrams.items():
        if len(words) >= 2:
            for i in range(len(words)):
                for j in range(i + 1, len(words)):
                    if len(words[i]) >= 3 and len(words[j]) >= 3:
                        count += 1
                        if count >= 3:
                            return True
    return False