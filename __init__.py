"""
Author: bongsang
LinkedIn: linkedin.com/in/bongsang
GitHub: github.com/bongsang
"""
from .any_info import AnyInfo
from .rgb_channel import RgbChannel

NODE_CLASS_MAPPINGS = {
    "AnyInfo": AnyInfo,
    "RgbChannel": RgbChannel,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "AnyInfo": "Any Info",
    "RgbChannel": "Split RGB Channels",
}

WEB_DIRECTORY = "./js"

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
