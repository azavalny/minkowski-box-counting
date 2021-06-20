import cv2
import preprocess as pps
import numpy as np

image_properties = []

def read_image():
    """Reads an image and obtains properties from it"""
    image = cv2.imread("Australia.png")

    image_p = pps.preprocess_image(image)

    image_height, image_width, image_channels = image.shape

    image_properties.append(image_p)
    image_properties.append(image_height)
    image_properties.append(image_width)
    image_properties.append(image_channels)


def count_and_display():
    """Draws the bounding box around the image"""
    image = image_properties[0]
    image_height = image_properties[1]
    image_width = image_properties[2]
    image_channels = image_properties[3]

    box_size = 50

    threshold = 95
    
    enclose_count = 0
    for h in range(int(image_height+1 / (box_size))):
        for w in range(int(image_width / box_size+1)):
            cv2.rectangle(image, (box_size*w, box_size*h), (box_size + box_size*w, 1+box_size + box_size*h), color=(0,0,255), thickness=2)
            #We use the green channel as it shows the highest contrast from ocean(blue) to islands(green)
            selection = image[box_size*h:1+box_size + box_size*h,box_size*w:box_size + box_size*w, 1]
            blue_mean = np.mean(selection)
            if(blue_mean >= threshold): 
                cv2.rectangle(image, (box_size*w, box_size*h), (box_size + box_size*w, 1+box_size + box_size*h), color=(0,0,125), thickness=-1)
                enclose_count +=1

    print(str(enclose_count) + " enclosed boxes")
    cv2.imshow("Gridded Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("Aus1.png", image)

def main():
    """Main Method"""
    read_image()
    count_and_display()

if __name__ == "__main__":
    main()