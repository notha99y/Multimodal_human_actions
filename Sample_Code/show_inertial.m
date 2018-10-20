function show_inertial(iner)

ax = iner(:,1);
ay = iner(:,2);
az = iner(:,3);

gx = iner(:,4);
gy = iner(:,5);
gz = iner(:,6);

figure;plot(ax, '-r'); hold on
plot(ay, '-g'); hold on;
plot(az, '-b'); 
legend('A-X','A-Y','A-Z');
xlabel('Samples');
ylabel('Acceleration (g)');
%title(strcat('Action = ', num2str(action), '  ', 'Trial = ', num2str(trial)));
set(gcf,'Position', [50, 250, 500, 500]);

figure;plot(gx, '-r'); hold on
plot(gy, '-g'); hold on;
plot(gz, '-b'); 
legend('G-X','G-Y','G-Z');
xlabel('Samples');
ylabel('Gyroscope (degree/second)');
%title(strcat('Action = ', num2str(action), '  ', 'Trial = ', num2str(trial)));
set(gcf,'Position', [600, 250, 500, 500]);

