"""
Based on: https://huggingface.co/docs/diffusers/optimization/mps
"""

from diffusers import StableDiffusionPipeline
import time

pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
pipe = pipe.to("mps")

# disable nsfw safety filter
pipe.config.nsfw = True
pipe.safety_checker = None

# Enable sliced attention computation.
#
# When this option is enabled, the attention module will split the input tensor in slices, 
# to compute attention in several steps. This is useful to save some memory in exchange for 
# a small speed decrease.
#
# Per Hugging Face, recommended if your computer has < 64 GB of RAM.
pipe.enable_attention_slicing()

prompt = "a photo of an astronaut riding a horse on mars"

# First-time "warmup" pass (see explanation above)
_ = pipe(prompt, num_inference_steps=1)

# Results match those from the CPU device after the warmup pass.
images = pipe(prompt, num_images_per_prompt=2).images

# loop through images
for image in images:
    epoch_time = int(time.time())
    prompt = prompt.replace(" ", "_")

    file_name = prompt + "_" + str(epoch_time) + ".png"
    image.save(file_name)