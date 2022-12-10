import unittest
from prompt_gen_class import PromptGen

class TestPromptGen(unittest.TestCase):
    def test_generate(self):
        pgc = PromptGen()
        prompt = "test prompt"
        variations = pgc.generate(prompt)
        self.assertEqual(len(variations), 4)

if __name__ == "__main__":
    unittest.main()