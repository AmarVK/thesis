clc
clear all
close all
robot_data = xlsread('dorsiflexion overground trial 2','book','A1:U8763','basic');
i =(1/200):(1/200):(length(robot_data)/200); %time
A = (diff(robot_data(:,5))); %estimated torque
A = [A(1);A];
figure(1)
plot(i, robot_data(:,20),'k',i,robot_data(:,3),'r',i,robot_data(:,5),'b',i,A,'g')
grid on
title('Comparison of angle, angular velocity and angular acceleration')
legend('Footswitch','angle','angular velocity','angular acceleration')
A1 = [];
for j = 1:1:length(robot_data)
    if robot_data(j,5)>0
%         if abs(A(j))<0.05*max(A)
%             A1(j) = robot_data(j,7);
%         else
            A1(j) = robot_data(j,7)-1.41;
%         end
    end
    if robot_data(j,5)<0
%         if abs(A(j))<0.05*max(A)
%             A1(j) = robot_data(j,7);
%         else
            A1(j) = robot_data(j,7)+1.41;
%         end
    end
    if robot_data(j,5)==0
         A1(j) = robot_data(j,7);
    end
end
% A1 = robot_data(:,7)-stictionvalues(robot_data(:,5));
figure(2)
plot(i,10*A,'b',i,A1,'r',i,robot_data(:,7),'g')
grid on
title('Estimated Torque vs Actual Torque')
legend('10*Estimated Torque','Actual Torque (-Stiction)','Actual Torque')
figure(3)
plot(i,sign(A),'k',i,sign(A1),'r')
grid on
title('Comparison of signs of Actual Torque and Expected Torque')
legend('signum(Expected Torque)','signum(Actual Torque)')
figure(4)
plot(i,robot_data(:,7),'g',i,A1,'r')
grid on
legend('Actual Torque','Torque(-stiction)')
figure(5)
plot(i,A,'g',i,A1,'r')
grid on
legend('Angular Acceleration','Torque(-stiction)')