import os
import shutil
import re
from tqdm import tqdm

base_dir = "TRAIN/"

# Create training folder
files = os.listdir(base_dir)

# Moves all training cat images to cats folder, training dog images to dogs folder
def train_maker(name):
  train_dir = "{}/train/{}".format(base_dir, name)
  for f in files:
        search_object = re.search(name, f)
        if search_object:
          shutil.move('{}/{}'.format(base_dir, name), train_dir)

train_maker("EOSINOPHIL")
train_maker("LYMPHOCYTE")
train_maker("MONOCYTE")
train_maker("NEUTROPHIL")

# Make the validation directories
try:
    os.makedirs("val/EOSINOPHIL")
    os.makedirs("val/LYMPHOCYTE")
    os.makedirs("val/MONOCYTE")
    os.makedirs("val/NEUTROPHIL")
except OSError:
    print ("Creation of the directory %s failed")
else:
    print ("Successfully created the directory %s ")

# Create validation folder

EOSINOPHIL_train = base_dir + "train/EOSINOPHIL/"
EOSINOPHIL_val = "val/EOSINOPHIL/"
LYMPHOCYTE_train = base_dir + "train/LYMPHOCYTE/"
LYMPHOCYTE_val = "val/LYMPHOCYTE/"
MONOCYTE_train = base_dir + "train/MONOCYTE/"
MONOCYTE_val = "val/MONOCYTE/"
NEUTROPHIL_train = base_dir + "train/NEUTROPHIL/"
NEUTROPHIL_val = "val/NEUTROPHIL/"

EOSINOPHIL_files = os.listdir(EOSINOPHIL_train)
LYMPHOCYTE_files = os.listdir(LYMPHOCYTE_train)
MONOCYTE_files = os.listdir(MONOCYTE_train)
NEUTROPHIL_files = os.listdir(NEUTROPHIL_train)

# This will put 1000 images from the two training folders
# into their respective validation folders

for f in tqdm(EOSINOPHIL_files[:244]):
    shutil.move('{}/{}'.format(EOSINOPHIL_train, f), EOSINOPHIL_val)

for f in tqdm(LYMPHOCYTE_files[:244]):
    shutil.move('{}/{}'.format(LYMPHOCYTE_train, f), LYMPHOCYTE_val)

for f in tqdm(MONOCYTE_files[:244]):
    shutil.move('{}/{}'.format(MONOCYTE_train, f), MONOCYTE_val)

for f in tqdm(NEUTROPHIL_files[:244]):
    shutil.move('{}/{}'.format(NEUTROPHIL_train, f), NEUTROPHIL_val)                