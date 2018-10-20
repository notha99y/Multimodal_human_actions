'''
Script that contains all the helper functions required to analyze the UTD-MHAD dataset

Functions defined
-----------------
    custom_sort(data_paths)
    get_dataset(root_data_path) TODO
'''


def custom_sort(data_paths):
    '''
    Custom sort function that is able to sort a given array of data_paths for the data set of UTD-MHAD

    The sort would sort by:
        1) time
        2) sensors
        3) actions 

    Returning a sorted array of file paths

    Parameters
    ----------
    data_path: array-like
        which contains all the full data_paths of the data files

    Returns
    -------
    sorted array: array-like
        a sorted array which contains all the full data_paths of the data files
    '''
    def get_file_name(path_name):
        return path_name.split('/')[-1].split('.')[0]
    # sort by time
    data_sort_t = sorted(
        data_paths, key=lambda x: get_file_name(x).split('_')[2])
    # sort by sensors
    data_sort_s = sorted(
        data_sort_t, key=lambda x: get_file_name(x).split('_')[1])
    # sort by actions
    data_sort_a = sorted(data_sort_s, key=lambda x: int(
        get_file_name(x).split('_')[0][1:]))

    return data_sort_a


def get_dataset(root_data_path):
    '''
    Returns the sorted full datapath of Depth, Intertial and Skeleton

    Parameters
    ----------
    root_data_path: string
        the path directory containing Depth, Interial and Skeleton .mat files

    Returns
    -------
    full_data_paths: list of string
        a list containing a sorted list of the full data paths of Depth, Inertial and Skeleton .mat files
    '''
    import os
    import glob

    assert type(root_data_path) == str, "root_data_path is not a str. Type is: {}".format(
        type(root_data_path))
    attrs = os.listdir(root_data_path)
    assert len(attrs) != 0, "The root_data_path contains nothing: {}".format(attrs)
    full_data_paths = []
    for attr in attrs:
        temp_path = os.path.join(root_data_path, attr)
        temp_data_full_path = glob.glob(os.path.join(temp_path, '*mat'))
        temp_data_full_path = custom_sort(temp_data_full_path)
        full_data_paths.append(temp_data_full_path)
    return full_data_paths


if __name__ == "__main__":
    print("This script contains all the helper functions required to analyze the UTD-MHAD dataset")
