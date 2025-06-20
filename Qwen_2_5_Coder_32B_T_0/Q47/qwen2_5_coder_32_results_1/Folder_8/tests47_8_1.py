from Q47.qwen2_5_coder_32_results_1.Folder_8.generated_answer import palindromes_of_specific_lengths


def test_string_of_similar_chars():
    n = max(72, 51)
    m = min(72 - 17 + 1, 51)
    s = ''.join('a' for _ in range(n * 2))
    assert palindromes_of_specific_lengths(s) == {'a' * i for i in range(50, m + 1)}


def test_string_of_similar_nums():
    n = max(72, 51)
    m = min(72 - 17 - 1, 51)
    s = ''.join('0' for _ in range(n * 2))
    assert not palindromes_of_specific_lengths(s)


def test_string_of_distinct_chars():
    s = 'abc' * (72 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_string_of_spaces():
    s = ' ' * (72 * 3)
    assert palindromes_of_specific_lengths(s) == set()


def test_string_of_spaces_and_letters():
    s = ' a ' * (72 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_length_of_palindrome():
    s = ''.join('a' for _ in range(72 * 2))
    returned_result = palindromes_of_specific_lengths(s)
    for i in returned_result:
        assert 50 <= len(i) <= 51


def test_location_of_palindrome():
    s = ''.join('a' for _ in range(72 * 3))
    returned_result = palindromes_of_specific_lengths(s)
    sliced_s = s[17: 72 + 1]
    for i in returned_result:
        assert i in sliced_s


def test_string_of_punctuations_and_space():
    s = '@ %' * (72 * 3)
    assert not palindromes_of_specific_lengths(s)
    