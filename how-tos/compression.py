class CompressedGene:
    def __init__( self, gene: str ) -> None:
        self._compress( gene )

    def _compress( self, gene: str ) -> None:
        self.bit_string: int = 1  # start with sentinel
        nucleotides = {
            'A': 0b00,
            'C': 0b01,
            'G': 0b10,
            'T': 0b11
        }
        for nucleotide in gene.upper():
            self.bit_string <<= 2  # shift left 2 bits
            try:
                self.bit_string |= nucleotides[nucleotide]
            except KeyError:
                raise KeyError(f'Invalid nucleotide: "{nucleotide}"')

    def decompress( self ) -> str:
        gene: str = ""
        nucleotides = {
            0b00: 'A',
            0b01: 'C',
            0b10: 'G',
            0b11: 'T'
        }
        for i in range( 0, self.bit_string.bit_length() - 1, 2 ):  # to exclude sentinel
            bits: int = self.bit_string >> i & 0b11  # get just two relevant bits
            try:
                gene += nucleotides[bits]
            except KeyError:
                raise KeyError(f'Invalid bits: {bits}')

        return gene[::-1]

    def __str__( self ):
        return self.decompress()


if __name__ == '__main__':
    from sys import getsizeof

    original: str = "TAGGGATTAACCGTTACATACATATATAGCCATGGATCGATTATATATAGGGATTAACCGTTATATATATATAGCATGGATCGATTATA" * 100
    print( f'original is {getsizeof( original )} bytes' )
    compressed: CompressedGene = CompressedGene( original )
    print( f'compressed is {getsizeof( compressed )} bytes' )
    print( compressed )
    print( f'original and decompressed are the same: {original == compressed.decompress()}' )

    test_bits = CompressedGene('ACGT')
    print(test_bits.decompress())
