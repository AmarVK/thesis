clc
clear all
close all
robot_data = xlsread('trial3','sheet1','A1:U2389','basic');
%9889
% for i = 1: length(robot_data)
%     if robot_data(i,7) > 0
%         torque_data(i) = 0;
%     else
%         torque_data(i) = -robot_data(i,7);
%     end
% end
% for i = 1: length(robot_data)
%     if robot_data(i,20) < 0.3
%         torque_data1(i) = 0;
%     else
%         torque_data1(i) = torque_data(i);
%     end
% end
i = 1:length(robot_data);
figure(1)
plot(i,10*robot_data(:,3),'r',i,robot_data(:,7),'b',i, robot_data(:,20),'k')
figure(2)
plot(robot_data(:,7),'b')
figure(3)
plot(i,robot_data(:,3),'r')
figure(4)
plot(diff(diff(robot_data(:,3))),'b')
figure(5)
plot(i,robot_data(:,20),'b')