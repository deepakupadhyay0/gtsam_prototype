import datetime
import glob
import os
from pathlib import Path
from rosbags.typesys import get_types_from_msg, register_types


def filter_bagfile_folders(base):
    folders = filter(os.path.isdir, [os.path.join(base, f) for f in os.listdir(base)])
    for folder in folders:
        if 'ignore' in folder:
            continue
        if 'T' in folder:
            # yield folder + '/bag'
            yield folder

def get_bagfile_folders(dataset_folders):
    bagfile_folders = []
    for folder in dataset_folders:
        bagfile_folders += filter_bagfile_folders(folder)
    bagfile_folders.sort()
    return bagfile_folders

def load_msg_types(msg_folder, msg_prefix=''):
    # Get SafeAI custom message definitions
    types = {}
    # folders = filter(os.path.isdir, [os.path.join(msg_folder, f) for f in os.listdir(msg_folder)])
    if os.path.exists(msg_folder):
        for msg_file in glob.glob(msg_folder+'/*.msg'):
            msg_text = Path(msg_file).read_text()
            msg_name = Path(msg_file).stem
            types.update(get_types_from_msg(msg_text, msg_prefix+msg_name))

    return types