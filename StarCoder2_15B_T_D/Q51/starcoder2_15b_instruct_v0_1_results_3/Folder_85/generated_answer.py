def if_contains_anagrams(words):
    letter_counts = [[word.lower().count(ch) for ch in 'abcdefghijklmnopqrstuvwxyz'] for word in words]
    anagram_pairs = 0
    for i in range(len(words) - 1):
        for j in range(i + 1, len(words)):
            if letter_counts[i] == letter_counts[j] and len(words[i]) >= 3 and (len(words[j]) >= 3):
                anagram_pairs += 1
    return anagram_pairs <= 276