"""
This script will generate images via Stable Diffusion. It runs on Apple Silicon (M1/M2).

Based on: https://huggingface.co/docs/diffusers/optimization/mps
"""

from diffusers import StableDiffusionPipeline
import time

pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
pipe = pipe.to("mps")

prompt = "crying on deena johnson's shoulder, crescent moon, radiant light, art nouveau, ornate, intricate, elegant, volumetric lighting, scenery, digital painting, highly detailed, artstation, sharp focus, illustration, concept art, ruan jia, steve mccurry"

# Toggle the NSFW filter
#
# The filter is intended to prevent the model from generating images that are
# inappropriate for the general public. However, it is not perfect and can
# sometimes block images that are not NSFW. If you wish to disable the filter,
# set the following variable to False.
pipe.nsfw_filter = False
 
# Enable sliced attention computation.
#
# When this option is enabled, the attention module will split the input tensor in slices, 
# to compute attention in several steps. This is useful to save some memory in exchange for 
# a small speed decrease.
#
# Per Hugging Face, recommended if your computer has < 64 GB of RAM.
pipe.enable_attention_slicing()

# First-time "warmup" pass
#
# This is necessary to get the model to run on Apple Silicon (M1/M2). There is a
# bug in the MPS implementation of the model that causes it to crash on the first
# pass. This is a workaround to get the model to run on Apple Silicon.
#
# It takes about 30 seconds to run.
_ = pipe(prompt, num_inference_steps=1)

# Results match those from the CPU device after the warmup pass.
images = pipe(prompt, num_images_per_prompt=1, height=512, width=512, requires_safety_checker=False).images

# loop through images
for image in images:
    epoch_time = int(time.time())
    prompt = prompt.replace(" ", "_")
    prompt = prompt[:100]

    file_name = str(epoch_time) + "_" + prompt + ".png"
    image.save(file_name)