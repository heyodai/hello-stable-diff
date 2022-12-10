from rich import print
import image_gen_class

# Get a prompt from the user
prompt = input("Enter a prompt: ")

# Ask user if they wish to change the default settings
# TODO: add a setting to automatically call MagicPrompt
print(
"""

Default settings:
    - num_images_per_prompt = 1
    - Save output = True
    - height = 512
    - width = 512
    - num_inference_steps = 1
    - is_nsfw_forbidden = False

Accept default settings? (\[y]/n)
"""
)
change_settings = input()

# If the user wishes to change the settings, ask them which ones
if change_settings == "n" or change_settings == "N":
    num_images_per_prompt = int(input("Enter the number of images to generate per prompt: "))
    save_output = input("Enter 'y' if you wish to save the images or 'n' if you do not: ")
    height = int(input("Enter the height of the generated images: "))
    width = int(input("Enter the width of the generated images: "))
    num_inference_steps = int(input("Enter the number of inference steps to use in the warmup pass: "))
    is_nsfw_forbidden = input("Enter 'y' if you wish to forbid NSFW images or 'n' if you do not: ")
    if is_nsfw_forbidden == "y":
        is_nsfw_forbidden = True
    else:
        is_nsfw_forbidden = False

# If the user does not wish to change the settings, use the defaults
else:
    num_images_per_prompt = 1
    save_output = True
    height = 512
    width = 512
    num_inference_steps = 1
    is_nsfw_forbidden = False

# Generate the images
image_gen = image_gen_class.ImageGen(is_nsfw_forbidden)
image_gen.generate_images(prompt, num_images_per_prompt, save_output, height, width, num_inference_steps)