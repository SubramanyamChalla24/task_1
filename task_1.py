# importing the needed libraries,packages
import PIL, os, datetime, easyocr, cv2, argparse
import matplotlib.pyplot as plt
from PIL import ImageDraw
from datetime import datetime

# show_image function shows a given image with given title in a proper format
def show_image(title, image):
    plt.figure(figsize=(10, 10))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.xticks([])
    plt.yticks([])
    plt.show()


# run function takes image,reader object of easy_ocr , file location of image and test_variable to check if it is a folder or a single image to process accordingly.
def run(image, reader, file_loc, test=0):
    image = cv2.imread(file_loc)  # read image from location
    bounds = reader.readtext(file_loc)  # use easy_ocr to detect text,bounding boxes
    for bound in bounds:  # loop through every box
        x, y = int(bound[0][0][0]), int(bound[0][0][1])  # get coords of top-left point
        # get coords of bottom-right point
        x1, y1 = int(bound[0][2][0]), int(bound[0][2][1])
        cv2.rectangle(image, (x, y), (x1, y1), (0, 255, 0), 3)  # draw rectangle
    if test == 1:  # if it is a single image then show the image
        show_image("", image)  # show the image
        # result will give the text in the image.
        result = " ".join([line[1] for line in bounds])
    return image  # return the image


# main function
def main():
    reader = easyocr.Reader(["hi", "en"])  # create object for hindi and english
    ap = argparse.ArgumentParser()  # argument parser to get arguments
    ap.add_argument("-i", "--imagepath", help="path to input image")
    ap.add_argument(
        "-f",
        "--folderpath",
        help="path to folder where input images are in a folder with name images",
    )
    args = ap.parse_args()
    start = datetime.now()  # start the time.
    if args.imagepath is not None:  # if single image then test=1
        image = cv2.imread(args.imagepath)  # read image
        final_image = run(image, reader, args.imagepath, 1)
    else:  # if not then a folder containing images
        folder = args.folderpath  # get folder path
        input_path = os.path.join(folder)  # input_path is same as folder_path
        output_path = os.path.join("output_images")  # put output_path
        # if output_path doesn't exists then create the folder.
        if not os.path.exists(output_path):
            os.mkdir(output_path)
        for filename in os.listdir(input_path):  # loop through the images
            if filename.endswith(".jpg"):  # if the file ends with jpg
                imagepath = os.path.join(input_path, filename)  # imagepath
                image = cv2.imread(imagepath)  # read image
                final_image = run(image, reader, imagepath, 0)  # run the program
                # get output image path
                output_image_path = os.path.join(
                    output_path, os.path.splitext(filename)[0] + "output.jpg"
                )
                # write the image (save the image in the location)
                cv2.imwrite(
                    output_image_path,
                    final_image,
                )
        end = datetime.now()  # end time
        print(f"time taken={end-start}")  # print time taken


# if name ==main run
if __name__ == "__main__":
    main()
