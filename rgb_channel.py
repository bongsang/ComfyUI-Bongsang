"""
Author: bongsang
LinkedIn: linkedin.com/in/bongsang
GitHub: github.com/bongsang
"""

from comfy.comfy_types import IO
import torch


class RgbChannel:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": (IO.IMAGE, {}),
            },
        }

    CATEGORY = "bongsang/image"
    RETURN_TYPES = (
        IO.IMAGE,
        IO.IMAGE,
        IO.IMAGE,
    )
    RETURN_NAMES = (
        "red",
        "green",
        "blue",
    )

    FUNCTION = "split_rgb_channel"

    def split_rgb_channel(self, image):
        """
        Splits the RGB channels of the input image and returns normalized RGB images for each channel.

        Args:
            image (torch.Tensor): Input image tensor of shape (1, H, W, 3).

        Returns:
            tuple: Three tensors corresponding to the red, green, and blue channels, each of shape (1, H, W, 3).
        """
        if not isinstance(image, torch.Tensor):
            raise ValueError("Input must be a PyTorch tensor.")

        if image.ndim != 4 or image.size(-1) != 3:
            raise ValueError("Input tensor must have shape (1, H, W, 3).")

        # Compute the sum of all channels for normalization
        sum_channels = image.sum(dim=-1, keepdim=True) + 1e-8  # Avoid division by zero

        # Create red channel image
        red_channel_image = torch.zeros_like(image)
        red_channel_image[:, :, :, 0] = image[:, :, :, 0] / sum_channels.squeeze(
            -1
        )  # Normalize R

        # Create green channel image
        green_channel_image = torch.zeros_like(image)
        green_channel_image[:, :, :, 1] = image[:, :, :, 1] / sum_channels.squeeze(
            -1
        )  # Normalize G

        # Create blue channel image
        blue_channel_image = torch.zeros_like(image)
        blue_channel_image[:, :, :, 2] = image[:, :, :, 2] / sum_channels.squeeze(
            -1
        )  # Normalize B

        return red_channel_image, green_channel_image, blue_channel_image
