import math

class WeatherAnalysis(object):
    def __init__(self,day0,day1,day2):
        #今天明天后天
        self.day0 = day0
        self.day1 = day1
        self.day2 = day2
    def average_tmp(self):
        #三天平均温度计算
        self.average_tmp =  ( (float(self.day0['tmp_max'])+float(self.day0['tmp_min']))/2+
                              (float(self.day1['tmp_max'])+float(self.day1['tmp_min']))/2+
                              (float(self.day2['tmp_max'])+float(self.day2['tmp_min']))/2) /3
        return self.average_tmp
    def tmp_difference(self):
        #三天温差计算
        self.tmp_difference = max(float(self.day0['tmp_max']),
                                  float(self.day1['tmp_max']),
                                  float(self.day2['tmp_max']))-\
                              min(float(self.day0['tmp_min']),
                                  float(self.day1['tmp_min']),
                                  float(self.day2['tmp_min']))
        return self.tmp_difference


