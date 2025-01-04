"""
Date: 2025-01-04
Ver: 1.0.0
Author: bongsang
LinkedIn: linkedin.com/in/bongsang
GitHub: github.com/bongsang
"""
from .any_info import AnyInfo

NODE_CLASS_MAPPINGS = {
    "AnyInfo": AnyInfo,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "AnyInfo": "Any Info",
}

WEB_DIRECTORY = "./js"

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
