function show_joint_3D(skeleton)

total_joint = 20;


J = [1, 2, 3, 2, 5, 6, 7, 2, 9,  10, 11, 4,  13, 14, 15, 4,  17, 18, 19;
     2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20];
     
ss = [];

num_frame = size(skeleton,3);

for i = 1:num_frame
    ss = [ss; skeleton(:,:,i)];
end

maxx = max(ss(:,1));
minx = min(ss(:,1));
maxy = max(ss(:,2));
miny = min(ss(:,2));
maxz = max(ss(:,3));
minz = min(ss(:,3));

clear ss

for i = 1:num_frame
    %%%% skeleton joints
    

    joint = skeleton(:,:,i);
    
    h = plot3(joint(:,1), joint(:,3), joint(:,2), 'r.', 'MarkerSize', 15);
    xlabel('X');
    ylabel('Z');
    zlabel('Y');
    %rotate(h,[0 45], -180);
    
    
%     for j = 1:total_joint
%         tmp = joint(j,:);
%         plot3(tmp(1),tmp(2),tmp(3),'r.','MarkerSize',15); 
%         %text(tmp(1),tmp(2),num2str(j));
%         xlabel('X');
%         ylabel('Y');
%         zlabel('Z');
%         hold on;
%     end

    set(gca,'DataAspectRatio',[1 1 1])
    
    
    
    for j = 1:size(J,2)
        point1 = joint(J(1,j),:);
        point2 = joint(J(2,j),:);
        line([point1(1),point2(1)], [point1(3),point2(3)], [point1(2),point2(2)], 'LineWidth',2);
    end
    
    axis([minx maxx minz maxz miny maxy]);
    grid;
    %axis tight;
    %axis off;
    set(gcf,'nextplot','replacechildren','Position', [10, 10, 400, 1000]); % original [100 100 200 500]
    
    pause(1/20);
end
