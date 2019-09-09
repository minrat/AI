# -*- coding: utf-8 -*-
'''
Author: Gemini.Chen
e-mail: gemini_chen@163.com
Here We will Do The face detect and save the snapshot or video silently.

'''
import os, sys, shutil
import cv2
import argparse


class VideoFaceDetect:
    def __init__(self):
        # Here Need Enhance Later
        self.work_space = "./workspace"
        self.tmp_directory = "./tmp"
        self.out_directory = "./out"

        # enable directory
        self.directory_state_enable(self.work_space)
        self.directory_state_enable(self.tmp_directory)
        self.directory_state_enable(self.out_directory)

        # snapshot switch
        self.need_snapshot = False
        #
        self.fps = ""
        self.size = ""
        self.fourcc = ""

    # Enable Directory
    def directory_state_enable(self, dir_path):
        if os.path.exists(dir_path):
            # print(dir_path+" Already Avaliable.")
            pass
        else:
            try:
                os.mkdir(dir_path)
            except IOError:
                print("Create "+dir_path + "Meet Error, Please Double Check")

    # Get The Video File
    def video_state_verify(self, source_file):
        # Verify Video State
        if source_file.strip() == "":
            print("Video No Exist, Please Double Confirm")
            sys.exit(0)
        # Verify Related Workspace

    # face detect and save the snapshot
    def face_detect(self, source_video):
        print("Detect Section Start..\n")
        # Copy the source file
        shutil.copy(source_video, self.work_space)

        # get the source video name
        video_name = os.path.basename(source_video)

        # Load The Video resource
        cap = cv2.VideoCapture(self.work_space+'/'+video_name)

        # Get The Codec
        pre = cap.get(cv2.CAP_PROP_FOURCC)

        # Get The Property(width, height)
        self.size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

        # Set The Codec
        self.fourcc = cv2.VideoWriter_fourcc(*'DIVX')

        # Get The Source fps
        self.fps = cap.get(cv2.CAP_PROP_FPS)

        # Load OpenCV classifier
        classfier = cv2.CascadeClassifier('./haarcascade_frontalface_alt2.xml')

        # set the mark flag color (B,R,G)
        color = (0, 255, 0)

        # set the cursor var
        i = 0
        while cap.isOpened():
            # read the video frame
            state, frame = cap.read()
            if not state:
                break

            # convert the current frame into a gray image
            grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # use detectMultiScale face detect
            face_detect_result = classfier.detectMultiScale(
                grey,
                scaleFactor=1.25,
                minNeighbors=3,
                # set the minimum scope
                minSize=(1, 1),
                # set the maximum scope
                # maxSize=(20, 20)
            )

            if len(face_detect_result) > 0:
                for face_rect in face_detect_result:
                    x, y, w, h = face_rect
                    cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)

                    # save snapshot (only keep face detected situation)
                    cv2.imwrite(os.path.join(self.tmp_directory, str(i) + '.png'), frame)
                    i += 1

            # save snapshot (keep all situation)
            # cv2.imwrite(os.path.join(self.tmp_directory, str(i) + '.png'), frame)
            # i += 1

            # display the process
            # cv2.imshow("Face Detection Progressing", frame)

        # release the resource
        cap.release()

        print("Detect Section End..\n")

    # composite the pic to video
    def composite_video(self, video_out):
        # count the total pics
        pic_counts = len(os.listdir(self.tmp_directory))

        # set the codec
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        #
        video_writer = cv2.VideoWriter(self.out_directory+'/'+video_out, fourcc, self.fps, self.size)

        for i in range(0, pic_counts+1):
            im_name = os.path.join(self.tmp_directory, str(i)+'.png')
            frame = cv2.imread(im_name)
            video_writer.write(frame)

        # close the writer
        video_writer.release()

        # destroy the cv2
        cv2.destroyAllWindows()

        # clean tmp directory
        if self.need_snapshot is False:
            self.job_clean(self.tmp_directory)

    # clean the tmp file
    def job_clean(self, file_path):
        if file_path.strip()is not "":
            # remove snapshot
            try:
                # verify file state
                if os.path.isfile(file_path):
                    # remove file
                    os.remove(file_path)
                # verify directory state
                elif os.path.isdir(file_path):
                    #  remove directory
                    shutil.rmtree(file_path, True)
            except FileNotFoundError:
                print("Remove Action Meet Unexpected Error, Please Double Confirm.")


if __name__ == '__main__':
    # define a flag
    flag = True

    parser = argparse.ArgumentParser(description='testing')
    parser.add_argument("--input_file", type=str, help='Input csv dataset')
    parser.add_argument("--output_file", type=str, help='Output csv dataset')
    params, _ = parser.parse_known_args()

    # verify the standard command format
    if params.input_file is None:
        flag = False
        raise BaseException("variable [source file] is missing")
    if params.output_file is None:
        flag = False
        raise BaseException("variable [output_file]  is missing")

    # decide to do or not
    if flag is False:
        sys.exit(1)

    print("Face Detect Testing Start....\n")

    face_detect = VideoFaceDetect()
    # detect the video
    face_detect.face_detect(params.input_file)

    # generate new video
    face_detect.composite_video(params.output_file)
