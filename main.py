import os
import cv2

# video = 24:18, cmd 6:1 => 48*3:18
vid = cv2.VideoCapture(input("Enter the name of the video(bad_apple.mp4): "))
dsize1 = tuple(([int(x) for x in input("Enter the width and height(144 22): ").split()]))
grayscale_str1 = " `.-':_,^=;><+!rc*/z?sLTv)J7(|Fi{C}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@"
grayscale_str = " .,:ilwW"
# os.system(f"mode con cols={dsize1[0]} lines={dsize1[1]}")
# file = open('new_file.txt', 'w')
if not vid.isOpened():
    print("Error opening video stream or file!")
while vid.isOpened():
    ret, frame = vid.read()
    frame_1 = frame
    frame = cv2.resize(frame, dsize1)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rows, cols = dsize1[::-1]
    os.system("cls")
    """file.close()
    file = open("new_file.txt", "w")
    os.system("tasklist > file.txt")
    ls = open("file.txt", 'r')
    if "notepad.exe" in ls:
        os.system("taskkill/im notepad.exe")"""
    for k in range(rows):
        for l in range(cols):
            print(grayscale_str[int((frame[k, l] * (len(grayscale_str)-1)/255))], end='')
            # file.write(grayscale_str[int((frame[k, l] * (len(grayscale_str)-1)/255))])
        print('\n')
        #file.write('\n')
    ##os.system("notepad.exe new_file.txt")
    if ret:
        cv2.imshow("Frame", frame_1)
        if cv2.waitKey(2) & 0xFF == ord('q'):
            break
    else:
        break
vid.release()
cv2.destroyAllWindows()
