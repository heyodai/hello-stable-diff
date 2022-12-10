from rich import print
from dotenv import dotenv_values
import image_gen_class

# Get a prompt from the user
prompt = input("Enter a prompt: ")

# Load in default settings from .env
config = dotenv_values(".env")
num_images_per_prompt = int(config["NUM_IMAGES_PER_PROMPT"])
save_output = bool(config["SAVE_OUTPUT"])
height = int(config["HEIGHT"])
width = int(config["WIDTH"])
num_inference_steps = float(config["NUM_INFERENCE_STEPS"])
is_nsfw_forbidden = True if config["IS_NSFW_FORBIDDEN"] == "True" else False

# Ask user if they wish to change the default settings
# TODO: add a setting to automatically call MagicPrompt
question = (
"""

Default settings:
    - num_images_per_prompt = {}
    - Save output = {}
    - height = {}
    - width = {}
    - num_inference_steps = {}
    - is_nsfw_forbidden = {}

Accept default settings? (\[y]/n)
"""
).format(num_images_per_prompt, save_output, height, width, num_inference_steps, is_nsfw_forbidden)
print(question)
change_settings = input()

# If the user wishes to change the settings, ask them which ones
if change_settings == "n" or change_settings == "N":
    num_images_per_prompt = int(input("Enter the number of images to generate per prompt: "))
    save_output = input("Enter 'y' if you wish to save the images or 'n' if you do not: ")
    height = int(input("Enter the height of the generated images: "))
    width = int(input("Enter the width of the generated images: "))
    num_inference_steps = float(input("Enter the number of inference steps to use in the warmup pass: "))
    is_nsfw_forbidden = input("Enter 'y' if you wish to forbid NSFW images or 'n' if you do not: ")
    if is_nsfw_forbidden == "y":
        is_nsfw_forbidden = True
    else:
        is_nsfw_forbidden = False

# Generate the images
image_gen = image_gen_class.ImageGen(is_nsfw_forbidden)
image_gen.generate_images(prompt, num_images_per_prompt, save_output, height, width, num_inference_steps)