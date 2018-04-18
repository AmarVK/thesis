# -*- coding: utf-8 -*-
"""
Created on Wed Mar 07 15:42:48 2018

@author: Suchitra Chandar
"""

from scipy import stats

def learning(avg,max_torque,sample_size,beta,L,Lmin,alpha_sens,Lmax,index):
    #   Compare last sample with the average of the rest and decide improvement and declining
    if avg == 1:
        average_torque = sum(max_torque[:sample_size-1])/(sample_size-1)
        R = (max_torque[sample_size-1]/average_torque)
        if average_torque < max_torque[sample_size-1]:
            print('Improvement')
            deltaL = beta*R
            print(deltaL)
            L = L - deltaL
            if L < Lmin:
                L = Lmin
                alpha_sens = 0.9*alpha_sens
        elif average_torque > max_torque[sample_size-1]:
            print('Decline')
            deltaL = beta*R
            print(deltaL)
            L = L + deltaL
            if L > Lmax:
                L = Lmax
                alpha_sens = 1.1*alpha_sens
        elif average_torque == max_torque[sample_size-1]:
            L = L
        return alpha_sens,L
    #   Regression analysis of sample size to decide improvement or decline
    elif avg == 0:
        slope, intercept, r_value, p_value, std_err = stats.linregress(index,max_torque)
        print(r_value)
        if r_value > 0:
             print('Improvement')
             deltaL = beta*r_value
             print(deltaL)
             L = L - deltaL
             if L < Lmin:
                 L = Lmin
                 alpha_sens = 0.9*alpha_sens
        elif r_value < 0:
             print('Decline')
             deltaL = beta*r_value
             print(deltaL)
             L = L - deltaL
             if L > Lmax:
                 L = Lmax
                 alpha_sens = 1.1*alpha_sens
        return alpha_sens,L
    elif avg == -1:
        return alpha_sens,L