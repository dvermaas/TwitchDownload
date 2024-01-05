import json
import subprocess

def main():
    command = 'twitch-dl videos moonmoon --json --game "Grand Theft Auto V " --all'
    vod_dict = subprocess.check_output(command, shell=True, encoding="utf-8").splitlines()[1]
    vod_dict = dict(json.loads(vod_dict))

    print(f"Got {vod_dict.get('videos')}")
    for video in vod_dict.get('videos')[::-1]:
        print(video.get("title"), video.get("publishedAt"), video.get("id"))

    # twitch-dl download 2016481831 -q source --output "{date}_{id}_{title}.{format}"
    # ffmpeg -i 2023-12-28_2016481831_future mayor of los santos yung dab.mkv -c:v libaom-av1 -strict 2023-12-28_2016481831_future mayor of los santos yung dab.av1
    # ffmpeg -hwaccel cuda -i "2023-12-28_2016481831_future mayor of los santos yung dab.mkv" -c:v libx264 -aom-params lossless=1  "futuremayorh264.mkv"
    # ffmpeg -i "2023-12-28_2016481831_future mayor of los santos yung dab.mkv" -c:v h264_nvenc -b:v 8000k output.mp4


if __name__ == "__main__":
    main()
