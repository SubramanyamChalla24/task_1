#  HINDI , GUJARATI OCR USING EASYOCR 


This project is a basic project on hindi , gujarati text ocr using easyocr

## Table of contents
1. [About](#loudspeaker-about)
2. [Tech Stack](#bulb-techstack)
3. [Input images](#camera-input)
4. [Running the Program](#wrench-runningtheprogram)
5. [Output](#file_folder-output)
6. [Time_taken](#clock11-timetaken)

## :loudspeaker: About 
The project is for detecting hindi,gujarati text in various images. It uses easyocr to get the text and bounding boxes coordinates. 


## :bulb: TechStack 

The tech stack used for this project
- EASYOCR
- PYTHON3
- OPENCV

## :camera: INPUT 

The input for the project is taken from https://www.kaggle.com/datasets/dataclusterlabs/hindi-text-image-dataset.

## :wrench: RUNNINGTHEPROGRAM 

- To run the program on a single image , run ```python3 task_1.py -i imagepath ```
- To run the program on a folder, run ```python3 task_1.py -f folderpath ```

## :file_folder: OUTPUT 

- Some output images are shown below 
1. ![alt text](https://github.com/SubramanyamChalla24/task_1/blob/master/output1.jpeg?raw=true)
2. ![alt text](https://github.com/SubramanyamChalla24/task_1/blob/master/91output.jpg?raw=true)

## :clock11: TIMETAKEN 

- For about 100 images using GPU from google colab , the time took was around 10 minutes . 
- For a single image the time was 1 second. 
- Some optimisations are yet to be done.

See the below links for more images and results. 
https://drive.google.com/drive/folders/14t1gW2RJVd9qD91BntOwvpf8diZsDn7Z?usp=sharing
