"""
Find Anagrams in Unix Dictionary
Nayef Copty
"""
from collections import defaultdict

def create_hash_table(path):
    """
    Maps a sorted word to all its anagrams in a given dictionary text file.
    """
    hash_table = defaultdict(list)
    with open(path, 'r') as dictionary:
        for word in dictionary:
            word = word.strip('\n')
            hash_table[''.join(sorted(word))].append(word)
    return hash_table

def count_anagram_sets(hash_table):
    return sum(len(v) > 1 for _, v in hash_table.iteritems())

def setup_sets_table(hash_table):
    sets_table = defaultdict(list)
    for _, v in hash_table.iteritems():
        if len(v) > 1:
            sets_table[len(v)].append(v)
    return sets_table

def print_sets(sets_table):
    max_key = max(sets_table.keys())
    with open('out.txt', 'w') as f:
        for key in xrange(max_key, 1, -1):
            for l in sets_table[key]:
                f.write(str(l) + '\n')
            f.write('\n')

def main():
    hash_table = create_hash_table('/usr/share/dict/words')
    sets = count_anagram_sets(hash_table)
    sets_table = setup_sets_table(hash_table)
    print_sets(sets_table)
    print sets

if __name__ == '__main__':
    main()
