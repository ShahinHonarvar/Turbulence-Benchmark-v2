def reverse_complement(dna_strand):
    """
    Takes a DNA strand as a string and returns its reverse complementary strand.
    The function is case-sensitive, maintaining the input case in the output.
    """
    complement_map = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C', 'a': 't', 't': 'a', 'c': 'g', 'g': 'c'}
    reversed_strand = dna_strand[::-1]
    reverse_compl = ''.join([complement_map[base] for base in reversed_strand])
    return reverse_compl

def test_reverse_complement():
    """
    Tests the reverse_complement function with various data points to ensure correctness.
    """
    test_cases = {'ATCCG': 'CGGAT', 'TaCgA': 'TcGaT', 'CCcGGA': 'TCcGGC', 'aTcGTA': 'TAcGGT'}
    for input_strand, expected_output in test_cases.items():
        output_strand = reverse_complement(input_strand)
        assert output_strand == expected_output, f'Test Failed: Input ({input_strand}) did not match expected output ({expected_output}). Got ({output_strand})'
    print('All tests passed successfully!')