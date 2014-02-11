# Find Anagrams in Unix Dictionary
# Nayef Copty

from collections import defaultdict

def create_hash_table(path):
    dictionary = open(path, 'r')
    hash_table = defaultdict(list)

    for word in dictionary:
        word = word.strip('\n')
        word_list = list(word)
        word_list.sort()
        word_key = "".join(word_list)
        hash_table[word_key].append(word)

    dictionary.close()

    return hash_table

def count_anagram_sets(hash_table):
    number_of_sets = 0

    for elem in hash_table:
        if len(hash_table[elem]) > 1:
            number_of_sets += 1

    return number_of_sets

def setup_sets_table(hash_table):
    sets_table = defaultdict(list)

    for elem in hash_table:
        if (len(hash_table[elem]) > 1):
            sets_table[len(hash_table[elem])].append(hash_table[elem])

    return sets_table

def print_sets(sets_table):
    max_key = max(sets_table.keys())

    file = open('out.txt', 'w')

    for key in xrange(max_key, 1, -1):
        for l in sets_table[key]:
            file.write(str(l))
            file.write('\n')
        file.write('\n')

    file.close()

def main():
    hash_table = create_hash_table('/usr/share/dict/words')
    sets = count_anagram_sets(hash_table)
    sets_table = setup_sets_table(hash_table)
    print_sets(sets_table)
    print sets

if __name__ == '__main__':
    main()
