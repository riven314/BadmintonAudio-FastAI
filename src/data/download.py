import os
import string
from itertools import repeat
from multiprocessing import Pool

from pytube import YouTube
import pandas as pd

import logging
logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler()],
                    format="%(asctime)s — %(name)s — %(levelname)s — %(message)s")


def download_videos(csv_path, save_dir, pool_n = 10):
    assert os.path.isfile(csv_path), f'file not exist: {csv_path}'
    df = pd.read_csv(csv_path)
    titles, urls = df.title.to_list(), df.url.to_list()

    with Pool(pool_n) as pool:
        _ = pool.starmap(
                download_video, 
                zip(urls, titles, repeat(save_dir))
                )
    return None


def download_video(url, raw_title, save_dir):
    logging.info(f'[downloading] \n\nurl: {url} \ntitle: {raw_title} \n')

    title = convert_title(raw_title)
    fname = f'{title}.mp4'
    os.makedirs(save_dir, exist_ok = True)
    
    streams = YouTube(url).streams.filter(
        progressive = True, file_extension = 'mp4', res = '720p'
        )
    streams.first().download(save_dir, filename = fname)

    logging.info(f'[complete] \n\nurl: {url} \ntitle: {raw_title} \n')
    return None
    

def convert_title(raw_title):
    exclude = set(string.punctuation)
    title_tokens = raw_title.split()
    title_tokens = [t for t in title_tokens if t not in exclude]
    return '_'.join(title_tokens)


if __name__ == '__main__':
    csv_path = os.path.join('dataset', 'match_list.csv')
    save_dir = os.path.join('dataset', 'raw_videos')
    download_videos(csv_path, save_dir)



