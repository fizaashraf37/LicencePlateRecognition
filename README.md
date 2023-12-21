# Overview

This project trains a YOLOv3 model on a pretrained model on number plates 
dataset to detect and recognize the number plates in a real time video or 
image. The trained model can read the characters on number plates with 
above 98% accracy. Please read the [reference research paper](Licence%20Plate%20Detection%20and%20Recognition%20Two%20stage%20YOLO.pdf) to get a better 
understanding of the models.

# Steps to train, validate and test the model
1. Create new project with virtual environment in PyCharm
2. Clone the project repositry from the following link:
https://github.com/TheophileBuy/LicensePlateRecognition/tree/master/Yolo%20Training
3. Copy the contents of the downloaded project into your project folder

## Installing Darkflow
1. In pycharm go to file/setting/project interpreter and click the + sign to install dependencies.
2. Make sure your python version is 3 or greater than 3 
### Dependencies:
- tensorflow 1.14.0 (if u get the error no module named tensorflow.keras or tensorflow.contrib then change the tensorflow version)
- numpy 1.16.0
- opencv 3
- cython
- keras
- imutils
- matplotlib

### OpenCV-Python Installation
#### One way: 
better approach - install opencv-python from pycharm

#### Other way:
Install anaconda
```
wget https://repo.continuum.io/archive/Anaconda3-2018.12-Linux-x86_64.sh
bash Anaconda3-2018.12-Linux-x86_64.sh -b -p $HOME/anaconda
export PATH="$HOME/anaconda/bin:$PATH"
conda update --all
```

Install opencv3
```
conda install --channel https://conda.anaconda.org/menpo opencv3
```

### Clone darkflow repositery
```
git clone https://github.com/thtrieu/darkflow
cd darkflow
python3 setup.py build_ext --inplace
pip install .
```

## Run Demo
You can run the demo by running `python3 finalPrototype.py`

## Training YOLO for LP detection:

1. Move `yolo.cfg`, `yolo-character.cfg`, `yolo-plate.cfg` to `./darkflow/cfg/`
2. Move `yolo.weights` to `./darkflow/bin/`
3. Move `train-character.py` and `train-plate.py` to `./darkflow/`
4. Change labels in `./darkflow/labels.txt`
5. Add your `AnnotationsXM`L and `Images` folder in `./darkflow/data/`
6. Run `train-plate.py` to train your yolo

## Testing for mAP:

1. clone [mAP repositry](https://github.com/Cartucho/mAP) in your prject folder
2. Copy your vaildation xml files in input/ground-truth folder of cloned repositry
3. Run `convert-gt_xml.py` file to convert xml to darkflow text format
4. Copy validation images in `input/detection-results` folder
5. Copy vaildation images in `input/images-optional` folder if you want to see animation
6. Run `validate-model.py`
7. Run `convert-dr-darkflow-json.py`
these scripts will convert yolo predictions into darkflow format 
8. To calculate mAP run `main.py`
-----------------------------------------------------------------------------------------------
