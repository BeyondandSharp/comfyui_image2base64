from PIL import Image
import numpy as np
from torch import Tensor
import base64
from io import BytesIO

class Image2Base64:
    def __init__(self) -> None:
        
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "images": ("IMAGE", {})
            }
        }

    RETURN_TYPES = ("STRING",)

    FUNCTION = "main"

    CATEGORY = "image"

    def main(
            self, 
            images: Tensor):
        
        for image in images:
            i = 255. * image.cpu().numpy()
            img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))

            # Create a BytesIO object to simulate a file-like object
            image_stream = BytesIO()

            # Save the image to the BytesIO stream
            img.save(image_stream, format="PNG")

            # Get raw bytes from the buffer
            image_bytes = image_stream.getvalue()

            # Encode the BytesIO stream content to base64
            base64_string = base64.b64encode(image_bytes).decode("utf-8") # Decode for text representation

        return (str(base64_string),)
       

NODE_CLASS_MAPPINGS = {
    'Image2Base64': Image2Base64
}
