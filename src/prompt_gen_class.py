"""
Script to generate prompt variations for use in Stable Diffusion.

Credit to Gustavosta: https://huggingface.co/Gustavosta/MagicPrompt-Stable-Diffusion
"""

from transformers import AutoTokenizer, AutoModelForCausalLM

class PromptGen:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("Gustavosta/MagicPrompt-Stable-Diffusion")
        self.model = AutoModelForCausalLM.from_pretrained("Gustavosta/MagicPrompt-Stable-Diffusion")

    def generate(self, prompt):
        """
        Function to generate prompt variations.

        Args:
            prompt (str): The prompt to generate variations for.

        Returns:
            variations (list): A list of variations for the prompt.
        """

        # tokenize the prompt
        tokenized_prompt = self.tokenizer.encode(prompt, return_tensors="pt")

        # generate the variations
        variations = self.model.generate(
            tokenized_prompt,
            do_sample=True,
            max_length=500,
            top_k=100,
            top_p=0.95,
            temperature=0.9,
            num_return_sequences=4,
            attention_mask=None,
        )

        # decode the variations
        variations = self.tokenizer.batch_decode(variations, skip_special_tokens=True)

        return variations