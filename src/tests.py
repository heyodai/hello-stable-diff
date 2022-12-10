import unittest
from prompt_gen_class import PromptGen
from image_gen_class import ImageGen

class TestPromptGen(unittest.TestCase):
    def test_generate(self):
        pgc = PromptGen()
        prompt = "test prompt"
        variations = pgc.generate(prompt)
        self.assertEqual(len(variations), 4)

class TestImageGen(unittest.TestCase):
    def test_generate(self):
        igc = ImageGen()
        prompt = "test prompt"
        images = igc.generate_images(prompt, save_output = False)
        self.assertEqual(len(images), 1)

if __name__ == "__main__":
    unittest.main()