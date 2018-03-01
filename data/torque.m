clc
clear all
close all
robot_data = xlsread('trial2','book','A1:U6389','basic');
i =(1/200):(1/200):(length(robot_data)/200);
figure(1)
grid on
plot(i,10*robot_data(:,3),'r',i,robot_data(:,7),'b',i, robot_data(:,20),'k',i(2:length(robot_data)),smooth(20*diff(robot_data(:,5))),'g',i,robot_data(:,5),'m')
xlabel('time (seconds)')
legend('angle','torque','footswitch','predicted torque')
figure(2)
plot(i(2:length(robot_data)),200*diff(robot_data(:,3)),'b',i,robot_data(:,5),'k')
figure(3)
plot(i(2:length(robot_data)),200*smoothdata(diff(robot_data(:,5)),'gaussian',20),'k',i,robot_data(:,5),'r')
figure(4)
plot(diff(robot_data(:,5)),'b')
figure(5)
plot(i,robot_data(:,20),'b')