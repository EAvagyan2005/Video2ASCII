import os
import cv2


cam_or_vid = input("Enter the name of the video(bad_apple.mp4): ")
cam_or_vid = int(cam_or_vid) if cam_or_vid.isdigit() else cam_or_vid
### GETTING STREAM OF VIDEO
vid = cv2.VideoCapture(cam_or_vid)

dsize1 = tuple(([int(x) for x in input("Enter the width and height(144 40): ").split()]))

### ASSETS FROM GRAYSCALE
grayscale_str = "           <+!rc*/z?sLTv)UAKXHm8RD#$Bg0MNWQ%&@"
grayscale_str1 = " .,:ilwW"
# os.system(f"mode con cols={dsize1[0]} lines={dsize1[1]}")
# file = open('new_file.txt', 'w')

def move(y, x):
    print('\033[%d;%dH' % (y, x))

if not vid.isOpened():
    print("Error opening video stream or file!")
while vid.isOpened():
    ret, frame = vid.read()
    ### CONVERTING TO THE GRAYSCALE
    frame_1 = frame
    frame = cv2.resize(frame, dsize1)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rows, cols = dsize1[::-1]
    move(0, 0)
    for k in range(rows):
        for l in range(cols):
            print(grayscale_str[int((frame[k, l] * (len(grayscale_str)-1)/255))], end='')
        print()

    if ret:
        # cv2.imshow("Frame", frame_1)
        if cv2.waitKey(2) & 0xFF == ord('q'):
            break
    else:
        break
vid.release()
cv2.destroyAllWindows()
