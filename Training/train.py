import argparse
from pathlib import Path
import shutil

parser = argparse.ArgumentParser(description='Train a model.')
parser.add_argument('-d', '--train-data-zip', type=str, required=True,
                    help='Path to the zipped training dataset.')
parser.add_argument('-w', '--weight-file', type=str, required=False,
                    help='Path to where the last weight file is saved.', default=None)
parser.add_argument('-k', '--keep-extracted-data', action='store_true', default=False,
                    help='Flag to indicate if extracted data should be kept after training.')
parser.add_argument('-e', '--epochs', type=int, default=15, help='number of epochs for training')

args = parser.parse_args()

args.train_data_zip = Path(args.train_data_zip)
args.weight_file = Path(args.weight_file) if args.weight_file is not None else None
dataset_dir = args.train_data_zip.parent
print(dataset_dir)

shutil.unpack_archive(args.train_data_zip, dataset_dir)

from ultralytics import YOLO

model = YOLO('yolov8s.pt') if args.weight_file is None else YOLO(args.weight_file)
# Train the model
print(str(dataset_dir/args.train_data_zip.name/'data.yaml'))
model.train(data=str(dataset_dir/args.train_data_zip.stem/'data.yaml'), epochs=args.epochs)

if not args.keep_extracted_data:
    shutil.rmtree(dataset_dir)