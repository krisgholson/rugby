import os
import subprocess
import json
from datetime import datetime

TODAY = datetime.now()
TODAY_STRING = TODAY.strftime('%Y%m%d')
import shutil

from dotenv import load_dotenv
from youtube import upload as youtube_upload

load_dotenv()

CAMERA_DIR = f'{os.environ.get("CAMERA_DIR")}'
RUGBY_VIDEOS_DIR = f'{os.environ.get("RUGBY_VIDEOS_DIR")}'
PROCESS_DIR = f'{os.environ.get("PROCESS_DIR")}'


def copy_video_files(todir):
    for file in os.listdir(CAMERA_DIR):
        if file.endswith('.MP4'):
            shutil.copy2(os.path.join(CAMERA_DIR, file), os.path.join(todir, file))
            print(os.path.join(CAMERA_DIR, file))


def process_video_files(process_dir):
    list_of_video_files = filter(lambda x: x.endswith('.MP4'), os.listdir(process_dir))
    list_of_video_files = sorted(list_of_video_files,
                                 key=lambda x: os.path.getmtime(os.path.join(process_dir, x)))
    txt_file = os.path.join(process_dir, 'videos.txt')
    # write all video file names to txt file so that they can be joined with ffmpeg
    with open(txt_file, 'w') as txt:
        for file in list_of_video_files:
            print(os.path.join(process_dir, file))
            txt.write(f"file '{file}'\n")

    video_file = os.path.join(process_dir, 'video.mp4')
    # ffmpeg -f concat -i videos.txt -c copy video.mp4
    # -an removes sound
    concat_video = subprocess.run(
        ['ffmpeg', '-f', 'concat', '-i', txt_file, '-c', 'copy', '-an', video_file])
    print("The concat_video exit code was: %d" % concat_video.returncode)


def upload(process_dir):
    video_file = os.path.join(process_dir, 'video.mp4')
    meta_file = os.path.join(process_dir, 'video-meta.json')
    with open(meta_file, 'r') as f:
        meta = json.load(f)

    youtube_upload(video_file, meta)


def make_video_folder():
    todays_video_dir = RUGBY_VIDEOS_DIR + '/' + TODAY_STRING
    os.mkdir(todays_video_dir)
    return todays_video_dir


def main():
    # todays_video_dir = make_video_folder()
    # print(todays_video_dir)
    # copy_video_files(todays_video_dir)
    process_dir = os.path.join(RUGBY_VIDEOS_DIR, PROCESS_DIR)
    # process_video_files(process_dir)
    upload(process_dir)


if __name__ == "__main__":
    main()
