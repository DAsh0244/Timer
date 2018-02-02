#!/usr/bin/env python
# vim:fileencoding=utf-8
# -*- coding: utf-8 -*-
"""
Timer
test_timer.py
Author: Danyal Ahsanullah
Date: 4/20/2017
License: N/A
Description: Timer structure tests
"""
from unittest import TestCase
from timer import Timer


class TestTimerList(TestCase):
    def test_indexing(self):
        sample_rate = 1000
        start = 0
        length = 10
        end = start + length/sample_rate
        time = Timer.get_timer('list', start, sample_rate, length)
        self.assertRaises(IndexError, time.__getitem__, length)
        self.assertRaises(IndexError, time.__getitem__, (-length - 1))
        for i,time_val in enumerate(time):
            self.assertAlmostEqual(start + (i/sample_rate), time_val, places=7, msg='Unexpected Time value mismatch')
        for i, time_val in zip(range(-length, 0, 1),time):
            self.assertAlmostEqual(end + (i / sample_rate), time_val, places=7, msg='Unexpected Time value mismatch')

    def test_positive_slicing(self):
        sample_rate = 1000
        start = 0
        length = 10
        end = start + length/sample_rate
        time = Timer.get_timer('list', start, sample_rate, length)
        stop = 3
        index = slice(start, stop)
        vals = time[index]
        for i,val in zip(range(start, stop), vals):
            self.assertAlmostEqual(start + (i/sample_rate), val, places=7, msg='Unexpected Time value mismatch')
        index = slice(stop)
        vals = time[index]
        for i,val in zip(range(start, stop), vals):
            self.assertAlmostEqual(start + (i / sample_rate), val, places=7, msg='Unexpected Time value mismatch')

    def test_negative_slicing(self):
        sample_rate = 1000
        start = 0
        length = 10
        end = start + length / sample_rate
        time = Timer.get_timer('list', start, sample_rate, length)
        stop = 3
        negative_start = length - stop
        index = slice(negative_start, None)
        vals = time[index]
        for i,val in zip(range(negative_start, length),vals):
            self.assertAlmostEqual(start + (i / sample_rate), val, places=7,
                                   msg='Unexpected Time value mismatch')
        index = slice(-1 - stop, -1)
        vals = time[index]
        for i,val in zip(range(-length, 0, -1),vals):
            self.assertAlmostEqual(end + (i / sample_rate), val, places=7, msg='Unexpected Time value mismatch')
        index = slice(-1, -1 - stop)
        vals = time[index]
        self.assertEqual(vals, [])  # should be empty list

    def test_step_slicing(self):
        sample_rate = 1000
        start = 0
        length = 100
        end = start + length / sample_rate
        time = Timer.get_timer('list', start, sample_rate, length)
        stop = 10
        step = 2
        index = slice(start, stop, step)
        vals = time[index]
        for i,val in zip(range(start, stop, step),vals):
            self.assertAlmostEqual(time[i], val, places=7, msg='Unexpected Time value mismatch')

            
class TestTimerGen(TestCase):
    def test_indexing(self):
        sample_rate = 1000
        start = 0
        length = 10
        end = start + length/sample_rate
        time = Timer.get_timer('gen', start, sample_rate, length)
        self.assertRaises(IndexError, time.__getitem__, length)
        self.assertRaises(IndexError, time.__getitem__, (-length - 1))
        for i,time_val in enumerate(time):
            self.assertAlmostEqual(start + (i/sample_rate), time_val, places=7, msg='Unexpected Time value mismatch')
        for i, time_val in zip(range(-length, 0, 1),time):
            self.assertAlmostEqual(end + (i / sample_rate), time_val, places=7, msg='Unexpected Time value mismatch')

    def test_positive_slicing(self):
        sample_rate = 1000
        start = 0
        length = 10
        end = start + length/sample_rate
        time = Timer.get_timer('gen', start, sample_rate, length)
        stop = 3
        index = slice(start, stop)
        vals = time[index]
        for i,val in zip(range(start, stop), vals):
            self.assertAlmostEqual(start + (i/sample_rate), val, places=7, msg='Unexpected Time value mismatch')
        index = slice(stop)
        vals = time[index]
        for i,val in zip(range(start, stop), vals):
            self.assertAlmostEqual(start + (i / sample_rate), val, places=7, msg='Unexpected Time value mismatch')

    def test_negative_slicing(self):
        sample_rate = 1000
        start = 0
        length = 10
        end = start + length / sample_rate
        time = Timer.get_timer('gen', start, sample_rate, length)
        stop = 3
        negative_start = length - stop
        index = slice(negative_start, None)
        vals = time[index]
        for i,val in zip(range(negative_start, length),vals):
            self.assertAlmostEqual(start + (i / sample_rate), val, places=7,
                                   msg='Unexpected Time value mismatch')
        index = slice(-1 - stop, -1)
        vals = time[index]
        for i,val in zip(range(-length, 0, -1),vals):
            self.assertAlmostEqual(end + (i / sample_rate), val, places=7, msg='Unexpected Time value mismatch')
        index = slice(-1, -1 - stop)
        vals = time[index]
        self.assertRaises(StopIteration,next,vals)  # should be empty list

    def test_step_slicing(self):
        sample_rate = 1000
        start = 0
        length = 100
        end = start + length / sample_rate
        time = Timer.get_timer('gen', start, sample_rate, length)
        stop = 10
        step = 2
        index = slice(start, stop, step)
        vals = time[index]
        for i,val in zip(range(start, stop, step),vals):
            self.assertAlmostEqual(time[i], val, places=7, msg='Unexpected Time value mismatch')
        
        
        
if __name__ == '__main__':
    import unittest
    unittest.main()
