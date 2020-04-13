import os

import pandas as pd

from src.data.download import download_videos, download_video, convert_title

import logging
logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler()],
                    format="%(asctime)s — %(name)s — %(levelname)s — %(message)s")

TEST_CSV = os.path.join('test_dataset', 'test.csv')
df = pd.read_csv(TEST_CSV)


def test_convert_title():
    title = df.title[0]
    new_title = convert_title(title)
    print(f'orig title: {title}')
    print(f'new title: {new_title}')
    return title, new_title


def test_download_video():
    url = df.url[0]
    raw_title = df.title[0]
    save_dir = os.path.join('test_dataset', 'raw_videos')
    download_video(url, raw_title, save_dir)
    return None


if __name__ == '__main__':
    test_download_video()