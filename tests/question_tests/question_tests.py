#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_1.question_a import test_config
from src.question_2.question_b import get_most_likely_ancestor_consensus

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())

    def test_get_most_likely_ancestor_consensus(self):
        result = get_most_likely_ancestor_consensus('GATATATGCATATACTT', 'ATAT')
        pos1 = 2
        pos2 = 4
        pos3 = 10
        self.assertEqual(result, (pos1, pos2, pos3))