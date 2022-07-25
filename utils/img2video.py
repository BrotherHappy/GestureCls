import cv2 as cv,os,glob,os.path as osp
# 将某个文件夹下面的图片转化为一个视频
def img2video(dir_path):
    fps = 8
    size = (960, 540)
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    video:cv.VideoWriter = cv.VideoWriter("film_frame.avi", fourcc, fps,
                            size, True)
    print(video)
    for i in os.listdir(dir_path):
        # if not i.endswith('.png'):
        #     continue
        img_path = os.path.join(dir_path, i)
        # print(img_path)
        img = cv.imread(img_path)
        print(img.shape)
        video.write(img)
    video.release()

if __name__ == "__main__":
    to_video_list = [osp.join('./data','基于深度学习的小样本视频手势识别初赛数据',i) for i in ('stage1_test','stage1_train_val')]
    for i in range
    img2video('./data/基于深度学习的小样本视频手势识别初赛数据/stage1_test/20210223_094534')
    pass

