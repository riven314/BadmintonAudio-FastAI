import os
from pathlib import Path


def get_files(path, extensions = None, recurse = False, include = None):
    """
    :param:
        path : str, main dir to be searched
        extensions : list, must start with . e.g. '.mp4'
        recurse : bool
        include : list, list of subfolders to be searched

    :return: 
        list of Path object

    from fastai: 
    https://github.com/fastai/course-v3/blob/master/nbs/dl2/08_data_block.ipynb
    """
    path = Path(path)
    extensions = {e.lower() for e in extensions}
    if recurse:
        res = []
        for i,(p,d,f) in enumerate(os.walk(path)): # returns (dirpath, dirnames, filenames)
            if include is not None and i==0: 
                d[:] = [o for o in d if o in include]
            else:
                d[:] = [o for o in d if not o.startswith('.')]
            res += _get_files(p, f, extensions)
        return res
    else:
        f = [o.name for o in os.scandir(path) if o.is_file()]
        return _get_files(path, f, extensions)


def _get_files(p, fs, extensions = None):
    """
    from fastai: 
    https://github.com/fastai/course-v3/blob/master/nbs/dl2/08_data_block.ipynb
    """
    p = Path(p)
    res = [p/f for f in fs if not f.startswith('.')
           and ((not extensions) or f'.{f.split(".")[-1].lower()}' in extensions)]
    return res