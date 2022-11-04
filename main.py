import os
import cv2

# video = 24:18, cmd 6:1 => 48:18, 48*3: 18
dsize1 = (198, 24)
file = open("new_file.txt", "w")
vid = cv2.VideoCapture("bad_apple.mp4")
#vid = cv2.VideoCapture(0)
grayscale_str1 = " `.-':_,^=;><+!rc*/z?sLTv)J7(|Fi{C}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@"
grayscale_str = " .,:ilwW"
#print(len(grayscale_str))
os.system(f"mode con cols={dsize1[0]} lines={dsize1[1]}")
if not vid.isOpened():
    print("Error opening video stream or file!")
while vid.isOpened():
    ret, frame = vid.read()
    #cv2.waitKey(26)
    scale = 0.5
    dsize = tuple([int(frame.shape[1] * scale), int(frame.shape[0] * scale)])
    frame = cv2.resize(frame, dsize1)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #print(dsize1) # 320 240 // 168 36
    rows, cols = dsize1[::-1]
    file.close()
    file = open("new_file.txt", "w")
    os.system("cls")
    for k in range(rows):
        for l in range(cols):
            print(grayscale_str[((frame[k, l] * len(grayscale_str))//256-1)+1], end='')
        print('\n')
    if ret:
        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
vid.release()
cv2.destroyAllWindows()
