import cv2
import os
import argparse

parser = argparse.ArgumentParser(description="Video to Frames")
parser.add_argument("--input_file", type=str, default="./example.mp4", help="video to extract")
parser.add_argument("--output_dir", type=str, default='./data/', help="Folder to output")
args = parser.parse_args()

# Playing video from file:
cap = cv2.VideoCapture(args.input_file)
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

try:
    if not os.path.exists(args.output_dir):
        print("Making directory")
        os.makedirs(args.output_dir)
except OSError:
    print('Error: Creating directory' + args.output_dir)

currentFrame = 0
while frame_count > currentFrame:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Saves image of the current frame in jpg file
    name = args.output_dir + str(currentFrame) + '.jpg'
    print('Creating...' + name)
    cv2.imwrite(name, frame)

    # To stop duplicate images
    currentFrame += 1

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
