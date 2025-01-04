import torch
from torchvision import transforms
from PIL import Image


def get_tensor(image_tensor):
    """
    Extracts detailed information about a PyTorch tensor representing an image.
    Returns the details as a dictionary.
    """
    if not isinstance(image_tensor, torch.Tensor):
        raise ValueError("The input is not a torch.Tensor.")

    info = {}

    # Gather details about the tensor
    info["shape"] = tuple(image_tensor.shape)
    info["data_type"] = str(image_tensor.dtype)

    # Statistics for each channel
    if len(image_tensor.shape) == 4:  # [B, H, W, C]
        stats = {}
        for i, channel in enumerate(["R", "G", "B"]):
            channel_data = image_tensor[0, :, :, i]  # Extract the ith channel
            stats[channel] = {
                "min": torch.min(channel_data).item(),
                "max": torch.max(channel_data).item(),
                "mean": torch.mean(channel_data).item(),
                "std_dev": torch.std(channel_data).item(),
                "variance": torch.var(channel_data).item(),
            }

        info["channel_statistics"] = stats

    # Additional information
    info["additional_info"] = {
        "num_elements": image_tensor.numel(),
        "is_contiguous": image_tensor.is_contiguous(),
    }

    return info


def tensor_to_string(info):
    """
    Converts the image tensor info dictionary to a human-readable string format.
    """
    if "error" in info:
        return f"Error: {info['error']}"

    result = []
    result.append("-" * 30)
    result.append("Tensor Information:")
    result.append("-" * 30)

    result.append(f"Shape: {info['shape']}")
    result.append(f"Data Type: {info['data_type']}")
    result.append(f"Total Elements: {info['additional_info']['num_elements']:,}")
    result.append(f"Is Contiguous: {info['additional_info']['is_contiguous']}")
    result.append("\n")
    result.append("-" * 30)
    result.append("Statistics Per Channel:")
    result.append("-" * 30)

    channel_stats = info.get("channel_statistics", {})
    for channel, stats in channel_stats.items():
        result.append(f"[Channel-{channel}]")
        result.append(f"  Minimum Value: {stats['min']}")
        result.append(f"  Maximum Value: {stats['max']}")
        result.append(f"  Mean: {stats['mean']:.6f}")
        result.append(f"  Standard Deviation: {stats['std_dev']:.6f}")
        result.append(f"  Variance: {stats['variance']:.6f}")
        result.append("\n")

    return "\n".join(result)


# Example usage
if __name__ == "__main__":
    image_path = "example.png"  # Replace with your image file path
    image = Image.open(image_path).convert("RGB")  # Ensure the image is RGB
    transform = transforms.ToTensor()  # Convert to a PyTorch tensor
    image_tensor = (
        transform(image).permute(1, 2, 0).unsqueeze(0)
    )  # [H, W, C] -> [1, H, W, C]

    info = get_tensor(image_tensor)
    print(tensor_to_string(info))
