# -*- coding: utf-8 -*-


def countdown(i):
    print i
    if i > 0: countdown(i-1)


countdown(3)

print '*'*10


def fact(x):
    print x
    return x * fact(x - 1) if x != 1 else 1


print 'fact: %s' % fact(3)

