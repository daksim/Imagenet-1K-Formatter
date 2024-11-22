# ImageNet1k Formatter

A script for reorganizing the ImageNet-1k dataset into the standard directory structure for classification tasks, as all images are typically stored in a flat directory.

## Requirements

Python 3.7 or higher

## Usage

### 1. Prepare the Required Files

- **Image Directory**: A folder containing all validation/test images in a flat structure. Each file should be named as `ILSVRC2012_val_00000001.JPEG`, `ILSVRC2012_val_00000002.JPEG`, etc.

- **Label Mapping File**: A JSON file mapping each label ID to its corresponding class name and WordNet ID. Example:

  ```json
  {
      "1": [ "n02119789", "kit_fox"],
      "2": ["n02100735", "English_setter"],
      ...
  }
  ```

  Here we use https://gist.github.com/aaronpolhamus/964a4411c0906315deb9f4a3723aac57 to create one in `imagenet_class_index.json`.

### 2. Run the Formatter Script

```python
python prepare_imagenet.py
```

#### Arguments:

- `image_dir`: Path to the directory containing the flat validation images.
- `label_txt_path`: Path to the TXT file containing image labels. ILSVRC2012_test_ground_truth.txt for test set and ILSVRC2012_validation_ground_truth.txt for val set.
- `label_map_json`: Path to the JSON file mapping label IDs to WordNet IDs and class names.
- `output_dir`: Path to the output directory for the reorganized dataset.
- `num_images`: Max number of images to process (default: None).

### 3. Check the Output

After running the script, the images will be organized into the standard ImageNet directory structure in the specified `output_dir`.

## Example

If your input directory contains:

```
datasets/imagenet/val/
├── ILSVRC2012_val_00000001.JPEG
├── ILSVRC2012_val_00000002.JPEG
└── ...
```

If you set 
```
image_dir = "datasets/imagenet/val"
label_txt_path = "./ILSVRC2012_validation_ground_truth.txt"
label_map_json = "./imagenet_class_index.json"
output_dir = "./val"
```

Running the script will produce:

```
./val/
├── n01440764/
│   ├── ILSVRC2012_val_00000001.JPEG
│   └── ...
└── n01443537/
    ├── ILSVRC2012_val_00000002.JPEG
    └── ...
```