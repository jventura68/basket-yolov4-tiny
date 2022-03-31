import argparse
import cv2
import os

def extractFrames(video, pathOut, totalFrames=50, cada=100):
    try:
      os.mkdir(pathOut)
    except:
      pass

    cap = cv2.VideoCapture(video)
    count = 0
    _each = cada
    saved = 0

    while (cap.isOpened()):

        # Capture frame-by-frame
        ret, frame = cap.read()

        if ret == True:
            _each -= 1
            if _each == 0:
                saved += 1
                print(f'Read {count} - {saved} {ret}')
                cv2.imwrite(os.path.join(pathOut, "frame{:d}.jpg".format(count)), frame)  # save frame as JPEG file
                _each = cada
                if saved == totalFrames:
                    break
            count += 1
        else:
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

def main(video, out, totalFrames, cada):

    extractFrames(video, out, totalFrames, each=250)

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--video', type=str)
    parser.add_argument('--out', type=str)    
    parser.add_argument('--totalFrames', type=int, default=50)    
    parser.add_argument("--cada", type=int, default=100)
    arg = parser.parse_args()
    main(arg.video, arg.out, arg.totalFrames, arg.cada)