import os
import shutil
import json

def reorganize_imagenet_data(image_dir, label_txt_path, label_map_json, output_dir, subset="val", num_images=None):
    """
    Reorganize ImageNet-1K data from  into ImageNet-like directory structure.

    Args:
        image_dir (str): Path to the directory containing all ImageNet train/validation/test images.
        label_txt_path (str): Path to the txt file containing labels for each image.
        label_map_json (str): Path to the JSON file mapping label IDs to class names.
        output_dir (str): Path to the output directory for reorganized data.
        num_images (int, optional): Max number of images to reorganize.

    Returns:
        None
    """
    # Load label map
    with open(label_map_json, "r") as f:
        label_map = json.load(f)

    # Load image-label pairs
    with open(label_txt_path, "r") as f:
        labels = [line.strip() for line in f.readlines()]
    
    # Create output directory structure
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Process images
    if num_images == None:
        num_images = len(labels)
    for i, label in enumerate(labels[:num_images]):
        # Map label to class name
        class_id = label_map[label][0]  # e.g., n01440764
        class_name_dir = os.path.join(output_dir, class_id)

        # Create class directory if not exists
        os.makedirs(class_name_dir, exist_ok=True)

        # Get source image path
        image_filename = f"ILSVRC2012_{subset}_{i + 1:08d}.JPEG"
        src_path = os.path.join(image_dir, image_filename)

        # Get destination path
        dest_path = os.path.join(class_name_dir, image_filename)

        # Move image
        if os.path.exists(src_path):
            shutil.copy(src_path, dest_path)
        else:
            print(f"Image {src_path} not found. Skipping.")

    print(f"Reorganized {num_images} images into {output_dir}.")


if __name__ == "__main__":

    # Example usage: reorganize ImageNet validation data
    # Note: You need to download the ImageNet validation data and the label files first.
    image_dir = "/mnt/data/datasets/ILSVRC2012/val"  # Path to your flat directory of images (val or train or test)
    label_txt_path = "./ILSVRC2012_validation_ground_truth.txt"  # Path to the txt file containing labels
    label_map_json = "./imagenet_class_index.json"  # Path to the JSON mapping label IDs to class names
    output_dir = "./val"  # Output directory
    num_images = None  # Max number of images to reorganize

    reorganize_imagenet_data(image_dir, label_txt_path, label_map_json, output_dir, subset="val", num_images=num_images)
