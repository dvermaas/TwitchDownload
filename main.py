import json
import subprocess

def main():
    command = 'twitch-dl videos moonmoon --json --game "Grand Theft Auto V " --all'
    vod_dict = subprocess.check_output(command, shell=True, encoding="utf-8").splitlines()[1]
    vod_dict = dict(json.loads(vod_dict))

    print(f"Got {vod_dict.get('videos')}")
    for video in vod_dict.get('videos')[::-1]:
        print(video.get("title"), video.get("publishedAt"), video.get("id"))

    # twitch-dl download 1643027074 -q source --output "{id}_{title}.{format}"


if __name__ == "__main__":
    main()
