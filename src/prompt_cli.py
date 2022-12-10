"""
Script to generate prompt variations for use in Stable Diffusion.

Credit to Gustavosta: https://huggingface.co/Gustavosta/MagicPrompt-Stable-Diffusion
"""

from rich import print
import prompt_gen_class

prompt = input("Enter your prompt: \n\n")
pgc = prompt_gen_class.PromptGen()
variations = pgc.generate(prompt)

print("\nHere are your variations:\n")
for variation in variations:
    print(variation)

save = input("Save variations to file? (y/n): ")

if save == "y":
    file_name = input("Enter file name (including file extension): ")
    with open(file_name, "w") as f:
        for variation in variations:
            f.write(variation + "\n")

    print("Variations saved to file.")
else:
    print("Variations not saved to file.")