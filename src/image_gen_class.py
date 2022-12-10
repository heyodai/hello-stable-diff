"""
This script will generate images via Stable Diffusion. It runs on Apple Silicon (M1/M2).

Based on: https://huggingface.co/docs/diffusers/optimization/mps
"""

from diffusers import StableDiffusionPipeline
import time

class ImageGen:
    def __init__(self, is_nsfw_forbidden = False) -> None:
        """
        Initialize the image generator.
        
        Args:
            is_nsfw_forbidden : bool
                If True, the model will not generate NSFW images.
        
        Returns:
            None
        """

        self.pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
        self.pipe = self.pipe.to("mps")

        # Toggle the NSFW filter
        #
        # The filter is intended to prevent the model from generating images that are
        # inappropriate for the general public. However, it is not perfect and can
        # sometimes block images that are not NSFW.
        #
        # @see https://github.com/CompVis/stable-diffusion/issues/239
        if is_nsfw_forbidden:
            self.pipe.nsfw_filter = lambda images, **kwargs: (images, False)

        # Enable sliced attention computation.
        #
        # When this option is enabled, the attention module will split the input tensor in slices, 
        # to compute attention in several steps. This is useful to save some memory in exchange for 
        # a small speed decrease.
        #
        # Per Hugging Face, recommended if your computer has < 64 GB of RAM.
        self.pipe.enable_attention_slicing()

    def generate_images(self, prompt, num_images_per_prompt = 1, save_output = True, height = 512, width = 512, num_inference_steps = 1) -> list:
        """
        Generate images based on the provided prompt.
        
        Args:
            prompt : str
                The prompt to use to generate the images.
            num_images_per_prompt : int
                (Optional | Default: 1)
                The number of images to generate per prompt.
            save_output : bool
                (Optional | Default: True)
                If True, the images will be saved to disk. Otherwise, they will be returned.
            height : int
                (Optional | Default: 512)
                The height of the generated images.
            width : int
                (Optional | Default: 512)
                The width of the generated images.
            num_inference_steps : int
                (Optional | Default: 1)
                The number of inference steps to use in the warmup pass.
        
        Returns:
            A list of PIL images
        """

        # First-time "warmup" pass
        #
        # This is necessary to get the model to run on Apple Silicon (M1/M2). There is a
        # bug in the MPS implementation of the model that causes it to crash on the first
        # pass. This is a workaround to get the model to run on Apple Silicon.
        #
        # It takes about 30 seconds to run.
        _ = self.pipe(prompt, num_inference_steps = num_inference_steps)

        # Results match those from the CPU device after the warmup pass.
        # TODO: does requires_safety_checker actually do anything?
        images = self.pipe(
            prompt, 
            num_images_per_prompt = num_images_per_prompt, 
            height = height, 
            width = width).images
            # requires_safety_checker = False).images

        # Save the images to disk if requested
        if save_output:
            for image in images:
                epoch_time = int(time.time())
                prompt = prompt.replace(" ", "_")
                prompt = prompt[:100]

                file_name = str(epoch_time) + "_" + prompt + ".png"
                image.save(file_name)
       
        return images