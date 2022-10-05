from multiprocessing.context import assert_spawning
import pytest
from series.series import fibonacci,lucas,other_series,sum_series


# Fibonatchi

'''
fibonacci
0 = 0
1 = 1
2 = 1
3 = 2
4 = 3
5 = 5
6 = 8

'''

def test_f_0():
 
    actual= fibonacci(0)
    expected = 0
    assert actual == expected

def test_f_1():
 
    actual= fibonacci(1)
    expected = 1
    assert actual == expected


def test_f_2():

    actual=fibonacci(2)
    expected=1
    assert actual == expected

def test_f_3():
    actual=fibonacci(3)
    expected=2
    assert actual == expected

def test_f_6():
    actual=fibonacci(6)
    expected=8
    assert actual == expected



# Lucas Numbers

'''
Lucas 
0 = 2
1 = 1
2 = 3
3 = 4
4 = 7
5 = 11
6 = 18

'''

def test_l_0():
 
    actual= lucas(0)
    expected = 2
    assert actual == expected

def test_l_1():
 
    actual= lucas(1)
    expected = 1
    assert actual == expected


def test_l_2():

    actual= lucas(2)
    expected= 3
    assert actual == expected

def test_l_3():
    actual=lucas(3)
    expected= 4
    assert actual == expected

def test_l_6():
    actual= lucas(6)
    expected= 18
    assert actual == expected



# other_series

'''
other series

first base == 4 and second base ==4


0 = 4
1 = 4
2 = 8
3 = 12
4 = 20

first base == 5 and second base ==4

0 = 5
1 = 4
2 = 9
3 = 13
4 = 22

'''

def test_otherseries_0():
 
    actual= other_series(0,4,4)
    expected = 4
    assert actual == expected

def test_otherseries_1():
 
    actual= other_series(1,4,4)
    expected = 4
    assert actual == expected


def test_otherseries_2():

    actual= other_series(2,4,4)
    expected= 8
    assert actual == expected

def test_otherseries_3():
    actual= other_series(3,4,4)
    expected= 12
    assert actual == expected

def test_otherseries_7():
    actual= other_series(4,5,4)
    expected=22
    assert actual == expected



# sum_series



def test_s_0():
 
    actual= sum_series(0)
    expected = 0
    assert actual == expected

def test_s_1():
 
    actual= sum_series(1)
    expected = 1
    assert actual == expected


def test_s_2():

    actual=sum_series(2,2,1)
    expected=3
    assert actual == expected

def test_s_3():
    actual=sum_series(3,2,1)
    expected=4
    assert actual == expected

def test_s_6():
    actual=sum_series(4,2,1)
    expected=7
    assert actual == expected
