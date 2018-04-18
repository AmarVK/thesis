clc
clear all
close all

robot_data = xlsread('trial1','ankle_pb.121033','A1:U6889','basic');
i =(1/200):(1/200):(length(robot_data)/200); %time
% stiction either as %FTR or absolute value
% max_tor = max(robot_data(:,7));
% min_tor = min(robot_data(:,7));
% FTR = max_tor - min_tor;
% percent_FTR = input('% FTR: ');
% stiction = percent_FTR*FTR/100;
stiction = input('stiction torque (N-m): ');

vel_thresh = input('velocity theshold (%): ');
vel_thresh = vel_thresh/100;

A = (diff(robot_data(:,5))); %angular acceleration (estimated torque)
A = [A(1);A];
figure(1)
graph1 = plot(i, robot_data(:,20),'c',i,robot_data(:,3),'k',i,robot_data(:,5),'--k',i,A,':k');
set(graph1,'LineWidth',1.5);
grid on
title('Comparison of angle, angular velocity and angular acceleration')
legend('Footswitch (V)','Angle (rad)','Angular velocity (rad s^{-1})','Scaled angular acceleration (rad s^{-2})')
xlabel('Time (seconds)')
A1 = [];
for j = 1:1:length(robot_data)
    if robot_data(j,5)>=0
        if abs(robot_data(j,5))<vel_thresh*max(robot_data(:,5))
            A1(j) = robot_data(j,7);
        else
            A1(j) = robot_data(j,7)-stiction;
        end
    end
    if robot_data(j,5)<0
        if abs(robot_data(j,5))<vel_thresh*max(robot_data(:,5))
            A1(j) = robot_data(j,7);
        else
            A1(j) = robot_data(j,7)+stiction;
        end
    end
end

A1 = smooth(A1, 'lowess');


figure(2)
graph2 = plot(i,10*A,':k',i,A1,'k',i,robot_data(:,7),'c');
set(graph2,'LineWidth',1.5);
grid on
title('Estimated Torque vs Actual Torque')
legend('Scaled Angular Acceleration (s^{-2})','Stiction compensated Torque (N-m)','Actual Torque(N-m)')
xlabel('Time (seconds)')
scaled_torque = 34.8587*A1;
ball = [0];
for count = 1:length(robot_data)
    if robot_data(count,20)<0.2
        if scaled_torque(count)>ball(count-1)
        ball(count) = scaled_torque(count);
        else
        ball(count) = ball(count-1);
        end
    else
        ball(count) = 0;
    end
end
figure(3)
area(i,ball)
hold on
plot(i,scaled_torque,'c')
hold on
plot(i,ball,'-ro')
title('Prediction of ball position')
legend('Predicted Ball Position (Pixel)','Scaled Stiction Compensated Torque (N-m)','Actual ball position from Game (Pixel)')
xlabel('Time (seconds)')
flag = 0;
gait = 1;
ystart = [];
max_torque = [0 0 0 0 0];
ball = ball/34.8587;
for count = 1:length(robot_data)
    if flag == 0
        if robot_data(count,20) < 0.2
            flag = 1;
        end
        if count == 1
            ystart(count) = 250;
        else
            ystart(count) = ystart(count-1);
        end
    else
        if robot_data(count,20) > 1
            flag = 0;
            gait = gait + 1
        end
        if gait < 6
            if max_torque(gait)<ball(count)
                max_torque(gait) = ball(count)
            else
                max_torque(gait) = max_torque(gait);
            end
            ystart(count) = ystart(count-1);
        else
            max_torque
            gait = 1;
            r = corr2([1 2 3 4 5],max_torque)
            if r~=0
                ystart(count) = ystart(count-1) + 50*r;
            else
                ystart(count) = ystart(count-1);
            end
            max_torque = [0 0 0 0 0];
        end
    end
end
[pks,locs] = findpeaks(A1,'MinPeakDistance',300);
locs = locs/200;
[yupper,ylower] = envelope(50*A1,2200,'peaks');
figure(4)
plot(i,50*A1,i,ystart,i,yupper,i,100*robot_data(:,20),i,ball/34.8587,'r')
title('Machine Learning Validation')
legend('Scaled Torque (N-m)','Position of Start-line in the game (Pixel)','Trend of Max Torque')
xlabel('Time (seconds)')
rvalues = [];