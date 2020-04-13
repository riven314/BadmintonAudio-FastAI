"""
sample cmd: scenedetect --input xyz.mp4 detect-content list-scenes split-video --output save_dir
"""
import os
from subprocess import call

from src.common.os_utils import get_files

import logging
logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler()],
                    format="%(asctime)s — %(name)s — %(levelname)s — %(message)s")


def slice_videos(mp4_dir, out_dir):
    """
    subfolder are generated under out_dir, clips from same videos are in same subfolder
    """
    os.makedirs(out_dir, exist_ok = True)
    mp4_paths = get_files(mp4_dir, extensions = ['.mp4'], recurse = False)

    for mp4_path in mp4_paths:
        fname = os.path.basename(mp4_path)
        title, _ = os.path.splitext(fname)
        write_dir = os.path.join(out_dir, title)
        os.makedirs(write_dir, exist_ok = True)

        _slice_video(str(mp4_path), write_dir)

    logging.info('videos slicing complete')
    return None


def _slice_video(mp4_path, out_dir):
    assert os.path.isfile(mp4_path), f'file not exist: {mp4_path}'
    logging.info(f'slicing video: {mp4_path}')
    cmd = ['scenedetect', '--input', mp4_path, 'detect-content', 'list-scenes', 'split-video', '--output', out_dir]
    call(cmd)
    return None


if __name__ == '__main__':
    import glob
    mp4_path = os.path.join('dataset', 'raw_videos')
    out_dir = os.path.join('dataset', 'sliced_clips')
    slice_videos(mp4_path, out_dir)


