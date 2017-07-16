# Anagram Unit Tests
# Nayef Copty

import os
import tempfile
import unittest

import anagram


class AnagramTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.fd, cls.path = tempfile.mkstemp()
        content = ('team\n' 'meat\n' 'mate\n' 'tame\n' 'hello\n' 'ellho\n')
        with open(cls.path, 'w') as f:
            f.write(content)
        cls.hashtable = anagram.create_hash_table(cls.path)

    @classmethod
    def tearDownClass(cls):
        os.close(cls.fd)
        os.remove(cls.path)

    def test_create_hash_table(self):
        self.assertEqual(len(self.hashtable), 2)

        keys = self.hashtable.keys()
        self.assertEqual(keys[0], 'aemt')
        self.assertEqual(keys[1], 'ehllo')

        values = self.hashtable.values()
        self.assertEqual(len(values[0]), 4)
        self.assertTrue('team' in values[0])
        self.assertTrue('meat' in values[0])
        self.assertTrue('mate' in values[0])
        self.assertTrue('tame' in values[0])

        self.assertEqual(len(values[1]), 2)
        self.assertTrue('hello' in values[1])
        self.assertTrue('ellho' in values[1])

    def test_count_anagram_sets(self):
        count = anagram.count_anagram_sets(self.hashtable)
        self.assertEqual(count, 2)

    def test_setup_sets_table(self):
        sets = anagram.setup_sets_table(self.hashtable)
        self.assertEqual(len(sets), 2)

        keys = sets.keys()
        self.assertEqual(keys[0], 2)
        self.assertEqual(keys[1], 4)

        values = sets.values()
        self.assertEqual(len(values[0][0]), 2)
        self.assertEqual(len(values[1][0]), 4)

    def test_print_sets(self):
        sets = anagram.setup_sets_table(self.hashtable)
        anagram.print_sets(sets)

        with open('out.txt', 'r') as file:
            lists = list(filter(None, (line.rstrip() for line in file)))

        largest_set = lists[0]
        self.assertTrue('team' in largest_set)
        self.assertTrue('meat' in largest_set)
        self.assertTrue('mate' in largest_set)
        self.assertTrue('tame' in largest_set)

        self.assertTrue('hello' in lists[1])
        self.assertTrue('ellho' in lists[1])

if __name__ == '__main__':
    unittest.main()
