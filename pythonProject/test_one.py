#！/usr/bin/env python
#-*-coding:utf-8-*-
def func(x):
    return x+1
def test_answer():
    assert func(3)==4

def test_set_comparson():
    set1 = set('1308')
    set2 = set('8035')
    assert set1 == set2

