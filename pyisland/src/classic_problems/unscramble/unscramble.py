"""
You have to find the original (unscrambled) words, which were randomly
taken from a wordlist.

Scrambled words from challenge should replace the text in the
scrambledwordlist.txt!
"""

def word_list(file_name: str) -> list:
    words = []
    with open(file_name, "r") as f:
        for line in f:
            words.append(line.replace('\n', ''))

    return words

def main():
    bad_words = word_list("scrambledwordlist.txt")
    good_words = word_list("wordlist.txt")

    # Alphabetically sorts all scrambled and unscrabled words
    sbad = [''.join(sorted(word)) for word in bad_words]
    # Creates a list of tuples [(sorted-word, correct-word),...]
    sgood = [(''.join(sorted(word)), word) for word in good_words]

    # Compares scrambled to unscrambled and returns correct-word if there
    # is a match
    final = [z for x in sbad for y, z in sgood if x==y]

    print(', '.join(final))


if __name__ == '__main__':
    main()
