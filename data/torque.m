clc
clear all
robot_data = xlsread('Robot_Data','Trial 1','A1:U2038','basic');
%9889
for i = 1: length(robot_data)
    if robot_data(i,7) > 0
        torque_data(i) = 0;
    else
        torque_data(i) = -robot_data(i,7);
    end
end
for i = 1: length(robot_data)
    if robot_data(i,20) < 0.3
        torque_data1(i) = 0;
    else
        torque_data1(i) = torque_data(i);
    end
end
i = 1:length(robot_data);
figure(1)
plot(i,torque_data1,'r',i,robot_data(:,7),'b',i, robot_data(:,20),'k')
figure(2)
plot(i,torque_data1,'r')