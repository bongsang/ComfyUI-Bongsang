import json
from comfy.comfy_types import IO
from .libs.types import any
from .libs.utils import get_tensor, tensor_to_string
import torch
from datetime import datetime


class AnyInfo:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "optional": {
                "anything": (any, {}),
            },
        }

    CATEGORY = "bongsang/utils"
    INPUT_IS_LIST = True
    OUTPUT_NODE = True
    RETURN_TYPES = ()

    FUNCTION = "display_info"

    def display_info(self, anything=None):
        value_str = f"[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}]\n\n"
        try:

            if type(anything[0]) == torch.Tensor:
                raw_info = get_tensor(anything[0])
                value_str += tensor_to_string(raw_info)
            elif type(anything) == list:
                for c in anything:
                    value_str += str(c)
            else:
                value_str = "Play with me... ʕっ•ᴥ•ʔっ"
        except Exception as e:
            # Json serialization for Other types
            try:
                value_str = json.dumps(anything, indent=4)[1:-1]
            except Exception as e:
                value_str = "Something wrong happended!"
            print(e)

        output = {
            "ui": {
                "text": [
                    value_str,
                ]
            }
        }

        return output
