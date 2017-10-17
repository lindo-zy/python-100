#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，
低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，
高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，
高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？

程序分析：请利用数轴来分界，定位。注意定义时需把奖金定义成长整型
'''


def get_reward(I):
    rewards = 0
    if I <= 10:
        rewards = I * 0.1

    elif (I > 10) and (I <= 20):
        rewards = (I - 10) * 0.075 + get_reward(10)

    elif (I > 20) and (I <= 40):
        rewards = (I - 20) * 0.05 + get_reward(20)

    elif (I > 40) and (I <= 60):
        rewards = (I - 40) * 0.03 + get_reward(40)

    elif (I > 60) and (I <= 100):
        rewards = (I - 60) * 0.015 + get_reward(60)

    else:
        rewards = get_reward(100) + (I - 100) * 0.01

    return rewards

if __name__ == '__main__':
    i = int(input('输入净利润(万为单位):')) * 10000
    print("净利润:", i)
    print("发放的奖金为：", get_reward(i / 10000) * 10000)
