'''
Script to show the animation of the dataset

Parameters
----------
    num: int
    TODO add in the action, sensor, and time

Returns
-------
    video of the choosen num
'''


def show_depth_video(depth_info, frame_rate=50):
    '''
    Returns and animated video of the depth data

    Parameters
    ----------
        depth_info: array like
            The matrices of shape WxHxFrames
        frame_rate: int
            frame rate of the animation (in ms)

    Returns
    -------
        None
        Just output a matplotlib figure of the video
    '''

    from matplotlib import animation
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(1, figsize=(6, 6))

    ax = plt.axes()
    ax.set_axis_off()
    im = plt.imshow(depth_info[:, :, 0])

    def init():
        im.set_data(depth_info[:, :, 0])
        return [im]

    def animate(i):
        im.set_array(depth_info[:, :, i])
        return [im]

    ani = animation.FuncAnimation(
        fig, animate, init_func=init, frames=depth_info.shape[-1], interval=frame_rate, blit=True)
    plt.show()


if __name__ == "__main__":
    from utils import get_dataset
    import scipy.io as sio
    import os

    DATA_PATH = os.path.join(os.getcwd(), 'data')
    depth_paths, inertial_paths, skeleton_paths = get_dataset(DATA_PATH)

    while True:
        res = int(input("Choose a number from 0 - {}: ".format(len(depth_paths))))
        depth_info = sio.loadmat(depth_paths[res])['d_depth']
        show_depth_video(depth_info)
