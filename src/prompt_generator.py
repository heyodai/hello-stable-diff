"""
Script to generate prompt variations for use in Stable Diffusion.

Credit to Gustavosta: https://huggingface.co/Gustavosta/MagicPrompt-Stable-Diffusion
"""

from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("Gustavosta/MagicPrompt-Stable-Diffusion")
model = AutoModelForCausalLM.from_pretrained("Gustavosta/MagicPrompt-Stable-Diffusion")

# ask the user for their prompt
prompt = input("Enter your prompt: \n\n")

# tokenize the prompt
tokenized_prompt = tokenizer.encode(prompt, return_tensors="pt")

# generate the variations
variations = model.generate(
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
variations = tokenizer.batch_decode(variations, skip_special_tokens=True)

# print the variations
print("Here are your variations:")
print("\n")
for variation in variations:
    print(variation)

# ask user if they wish to save the variations to file
save = input("Save variations to file? (y/n): ")

if save == "y":
    # ask user for file name
    file_name = input("Enter file name: ")

    # save variations to file
    with open(file_name, "w") as f:
        for variation in variations:
            f.write(variation + "\n")

    print("Variations saved to file.")
else:
    print("Variations not saved to file.")
