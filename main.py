import os
import json
import subprocess

broadcasters = ["moonmoon"]
base_path = os.path.join(os.path.expanduser("~"), "Downloads")


def download_vods(online_vods: set, base_dir: str, folder="Vods"):
    path = os.path.join(base_dir, folder)
    saved_vods = {filename.split("_")[0] for filename in os.listdir(path)}
    todo_vods = online_vods - saved_vods
    for vod_id in todo_vods:
        dowload_vod_cmd = f'twitch-dl download {vod_id} -q source --output "{{id}}_{{date}}.{{format}}" --max-workers {os.cpu_count()}'
        subprocess.call(dowload_vod_cmd, cwd=path)


def download_chats(online_vods: set, base_dir: str, folder="Chats"):
    path = os.path.join(base_dir, folder)
    saved_chats = {filename.split(".")[0] for filename in os.listdir(path)}
    todo_chats = online_vods - saved_chats
    for chat_id in todo_chats:
        download_chat_cmd = f"chat_downloader https://www.twitch.tv/videos/{chat_id} --output {chat_id}.log"
        subprocess.call(download_chat_cmd, cwd=path)


def main():
    for broadcaster in broadcasters:
        working_dir = os.path.join(base_path, broadcaster)
        if not os.path.exists(working_dir):
            os.makedirs(working_dir)
            os.makedirs(os.path.join(working_dir, "Vods"))
            os.makedirs(os.path.join(working_dir, "Chats"))

        list_vods_cmd = f'twitch-dl videos {broadcaster} --json --all'
        vod_dict = subprocess.check_output(list_vods_cmd, cwd=working_dir, shell=True, encoding="utf-8").splitlines()[0]
        vod_dict = dict(json.loads(vod_dict))
        online_vods = set([video.get("id") for video in vod_dict.get('videos')[::-1]])
        download_vods(online_vods, working_dir)
        download_chats(online_vods, working_dir)
    print("Done")


if __name__ == "__main__":
    main()
