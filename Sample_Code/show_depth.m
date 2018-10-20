function show_depth(depth)

num_frame = size(depth,3);

for i = 1:num_frame
    imagesc(depth(:,:,i));
    pause(1/20);
end