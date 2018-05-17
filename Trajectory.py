import numpy as np 
from math import *

class Trajectory(object):
	"""docstring for Trajectory"""
	def __init__(self, startPoint, endPoint):
		self.startPoint = startPoint #[0, 0, 0, 0, 0, 0]
		self.endPoint = endPoint #[0, 0, 0, 0, 0, 0]
		
	def Calculate(self):
		sp_time = 0.1
		distance = sqrt((self.startPoint[0] - self.endPoint[0])**2 + (self.startPoint[1] - self.endPoint[1])**2 + (self.startPoint[2] - self.endPoint[2])**2)
		v0 = 0.1
		T = int(distance/v0) #(s) Thoi gian di het quy dao
		numT = int(T/sp_time)
		s0 = 0 #Vi tri diem dau
		
		sn = distance #Vi tri diem cuoi

		h = sn - s0
		# dis_s = h/100.0

		a0 = s0
		a1 = 0
		a2 = 0
		a3 = 1.0/(2 * T**3) * 20*h
		a4 = 1.0/(2 * T**4) * (-30)*h
		a5 = 1.0/(2 * T**5) * 12*h

		t = []
		s = []
		x = []
		y = []
		z = []

		# print(T)
		# print(numT)

		for i in range(numT+1):
			t.append(i*T/numT)
			s.append(a0 + a1*t[i] + a2*t[i]**2 + a3*t[i]**3 + a4*t[i]**4 + a5*t[i]**5)
			# s.append(i*dis_s)
			x.append(self.startPoint[0] + ((self.endPoint[0] - self.startPoint[0])/distance) * s[i])
			y.append(self.startPoint[1] + ((self.endPoint[1] - self.startPoint[1])/distance) * s[i])
			z.append(self.startPoint[2] + ((self.endPoint[2] - self.startPoint[2])/distance) * s[i])
		# print(distance, '\n')
		# for i in range(101):
		# 	print(s[i])
		return x, y, z

if __name__ == '__main__':
	startPoint1 = [1, 2, 3, pi/2, pi/3, pi/4]
	endPoint1 = [5, 6, 7, pi, pi/2, pi/6]
	s = Trajectory(startPoint1, endPoint1)
	print(s.Calculate())
	print('\n', len(s.Calculate()))