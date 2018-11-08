# Multi-modal Human Actions
In this repo, we would analyze the open source human action regonition data from UT Dallas
# Setup
1. Get Anaconda [download](https://anaconda.org/anaconda/python)
2. Clone this repo
3. Setup conda environment 
```bash
conda env create -f=environment.yml
```
4. Activate environment
```bash
source activate mmha
```
5. Download data from [here](https://www.utdallas.edu/~kehtar/UTD-MHAD.html) and save them under a folder named `data` at the project root directory
6. change directory to notebooks and launch a jupyter notebook
```bash
cd notebooks
jupyter notebook
```
# About the Dataset
The naming convention of a file is "ai_sj_tk_modality", where ai stands for action number i, sj stands for subject number j, tk stands for trial k, and modality corresponds to four data modalities (color, depth, skeleton, inertial).


## Depth Data
The depth data is a `(240, 320, 55) WidthxHeightxFrames matrix`. <br>
Each frame contains an image <br>
Example of the depth data looks like this <br>
![depth_tennis_swing](pictures/depth_tennis_swing.gif)

## Skeleton Data
Each skeleton data is a `20 x 3 x num_frame matrix`. <br>
Each row of a skeleton frame corresponds to three spatial coordinates of a joint. <br>
The skeleton joint order in UTD-MAD dataset:
1. head 
2. shoulder_center
3. spine
4. hip_center
5. left_shoulder
6. left_elbow
7. left_wrist
8. left_hand
9. right_shoulder
10. right_elbow
11. right_wrist
12. right_hand
13. left_hip
14. left_knee
15. left_ankle
16. left_foot
17. right_hip
18. right_knee
19. right_ankle
20. right_foot

Example of the skeleton data looks like this <br>
![skeleton_tennis_swing](pictures/skeleton_tennis_swing.gif)

## Inertial Data

![inertial_tennis_swing](pictures/inertial_tennis_swing.png)