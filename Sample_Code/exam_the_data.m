
%%% This is the example code to show the depth, skeleton, and inertial
%%% data.
%%% If you have any questions about the code and the dataset, please
%%% contact Chen Chen (chenchen870713@gmail.com)

load('a1_s1_t2_depth.mat');
show_depth(d_depth);


load('a1_s1_t2_skeleton.mat');
show_joint_3D(d_skel);


load('a1_s1_t2_inertial.mat');
show_inertial(d_iner);






