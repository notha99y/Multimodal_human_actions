'''
Script to show the animation of the dataset

Parameters
----------
    num: int
    TODO add in the action, subject, and trial

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


def show_skeleton_video(skeleton_info, frame_rate=50):
    import numpy as np
    import matplotlib.pyplot as plt
    import mpl_toolkits.mplot3d.axes3d as p3
    from matplotlib import animation

    J = np.array([[1, 2, 3, 2, 5, 6, 7, 2, 9,  10, 11, 4,  13, 14, 15, 4,  17, 18, 19],
                  [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]])
    J -= 1

    fig = plt.figure()
    ax = p3.Axes3D(fig)

    maxx = skeleton_info[:, 0, :].max()
    minx = skeleton_info[:, 0, :].min()
    maxy = skeleton_info[:, 1, :].max()
    miny = skeleton_info[:, 1, :].min()
    maxz = skeleton_info[:, 2, :].max()
    minz = skeleton_info[:, 2, :].min()

    # ax.set_xlabel('x axis')
    # ax.set_ylabel('z axis')
    # ax.set_zlabel('y axis')
    # ax.set_axis_off()

    ax.view_init(90, 0)
    ax.set_xlim3d(minx, maxx)
    ax.set_zlim3d(miny, maxy)
    ax.set_ylim3d(minz, maxz)

    ax.set_aspect('equal')

    joint = skeleton_info[:, :, 0]
    ln = []
    ln.append(ax.plot(joint[:, 0], joint[:, 2], joint[:, 1], 'o', c='b'))
    for i in range(len(J[0])):
        point1 = joint[J[0, i], :]
        point2 = joint[J[1, i], :]

        ln.append(ax.plot(xs=[point1[0], point2[0]], ys=[
            point1[2], point2[2]], zs=[point1[1], point2[1]], c='r'))

    def animate(i):
        tot_frames = skeleton_info.shape[-1]

        joint = skeleton_info[:, :, i]
        for j in range(len(ln)):

            if j == 0:
                ln[j][0].set_data(joint[:, 0], joint[:, 2])
                ln[j][0].set_3d_properties(joint[:, 1])
            else:
                point1 = joint[J[0, j-1], :]
                point2 = joint[J[1, j-1], :]
                ln[j][0].set_data([point1[0], point2[0]],
                                  [point1[2], point2[2]])
                ln[j][0].set_3d_properties([point1[1], point2[1]])
        ax.view_init(10, -1.2*i)
    ani = animation.FuncAnimation(
        fig, animate, frames=skeleton_info.shape[-1], interval=frame_rate, blit=False)
    ani.save('skeleton.gif', writer='imagemagick', fps=20)
    plt.show()


if __name__ == "__main__":
    from utils import get_dataset
    import scipy.io as sio
    import os

    DATA_PATH = os.path.join(os.getcwd(), 'data')
    print(os.listdir(DATA_PATH))
    depth_paths, RGB_images_paths, inertial_paths, skeleton_paths, RGB_paths, depth_numpy_paths = get_dataset(
        DATA_PATH)

    # while True:
    #     res = int(input("Choose a number from 0 - {}: ".format(len(depth_paths))))
    #     depth_info = sio.loadmat(depth_paths[res])['d_depth']
    #     show_depth_video(depth_info)

    skeleton_info = sio.loadmat(skeleton_paths[450])['d_skel']
    show_skeleton_video(skeleton_info)
