import fiftyone as fo

CATEGORY_NAMES = [
    "car", 
    "person", 
    "truck", 
    "bus", 
    "motorcycle", 
    "bicycle", 
    "stop sign", 
    "traffic light"
]

train_dataset = fo.zoo.load_zoo_dataset(
    "coco-2017",
    split="train",
    label_types=["detections"],
    classes=CATEGORY_NAMES,
)

val_dataset = fo.zoo.load_zoo_dataset(
    "coco-2017",
    split="validation",
    label_types=["detections"],
    classes=CATEGORY_NAMES,
)

session = fo.launch_app(train_dataset)