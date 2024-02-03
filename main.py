import os
import json
import subprocess

working_dir = "G:\\"


def download_vods(online_vods: set, folder="Vods"):
    saved_vods = {filename.split("_")[0] for filename in os.listdir(working_dir+folder)}
    todo_vods = online_vods - saved_vods
    for vod_id in todo_vods:
        dowload_vod_cmd = f'twitch-dl download {vod_id}' + ' -q source --output "{id}_{date}.{format}" --max-workers 8'
        subprocess.call(dowload_vod_cmd, cwd=working_dir+folder)


def download_chats(online_vods: set, folder="Chats"):
    saved_chats = {filename.split(".")[0] for filename in os.listdir(working_dir+folder)}
    todo_chats = online_vods - saved_chats
    for chat_id in todo_chats:
        download_chat_cmd = f"chat_downloader https://www.twitch.tv/videos/{chat_id} --output {chat_id}.log"
        subprocess.call(download_chat_cmd, cwd=working_dir+folder)


def main():
    list_vods_cmd = 'twitch-dl videos moonmoon --json --game "Grand Theft Auto V " --all'
    vod_dict = subprocess.check_output(list_vods_cmd, cwd=working_dir, shell=True, encoding="utf-8").splitlines()[1]
    vod_dict = dict(json.loads(vod_dict))

    online_vods = set([video.get("id") for video in vod_dict.get('videos')[::-1]])
    download_vods(online_vods)
    download_chats(online_vods)
    print("Done")


if __name__ == "__main__":
    main()
