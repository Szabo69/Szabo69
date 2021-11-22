from turtle import *

speed(8)
colormode(255)
bgcolor('black')
n=0
while n < 200:
    right(n)
    forward(n * 2)
    color(n,255-n,n%30*8)
    n += 1
