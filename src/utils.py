'''
Script that contains all the helper functions required to analyze the UTD-MHAD dataset

Functions defined
-----------------
    custom_sort(data_paths)
    get_dataset(root_data_path) TODO
'''


def custom_sort(data_paths):
    '''
    Custom sort function that is able to  sort a given array of data_paths for the data set of UTD-MHAD

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


if __name__ == "__main__":
    print("This script contains all the helper functions required to analyze the UTD-MHAD dataset")
