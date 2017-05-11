# Overview:
Timer is a set of pure python dynamic timer objects used to provide
a low memory overhead timer at the cost of computational time.

Its main applications are for when you are capturing an incredible amount of data at a consistent sampling rate and
are not concerned with doing much with the data until after you have grabbed the full data set you are interested in.

Timer is designed to be used as a drop in replacement for traditional time arrays, and therefore is fully 
indexable with integer indexes and slice objects. 
## Requirements

[Python3.x][py] - Tested with `> 3.5.1 Win` , `3.4 Linux`

## Example Usage:
Because Timer is designed to be used as a drop in replacement for traditional time arrays, 
creating a timer object is as simple as 
```python
from timer import TimerList

start = 0          # time to start the timer at in seconds
sample_freq = 1000 # sampling frequency in Hz
samples = 10       # number of samples that will be taken

# Create the time instance
time = TimerList(start, sample_freq, samples)
```

Use time as you normally would:

```python
>>> print(time[0]) 
0.0
>>> print(time[-1])
0.009
>>> print(time[0:5])
[0.0, 0.001, 0.002, 0.003, 0.004]
>>> print(time[:5])
[0.0, 0.001, 0.002, 0.003, 0.004]
>>> print(time[5:])
[0.005, 0.006, 0.007, 0.008, 0.009]
>>> print(time[:])
[0.0, 0.001, 0.002, 0.003, 0.004, 0.005, 0.006, 0.007, 0.008, 0.009]
>>> print(time[-10:-1])
[0.0, 0.001, 0.002, 0.003, 0.004, 0.005, 0.006, 0.007, 0.008]
>>> print(time[-10:-1:2])
[0.0, 0.002, 0.004, 0.006, 0.008]
```

Because it may not be desirable to have the timer object return a list 
(say for looping, where it will just be iterated anyway), 
there is a second timer object called `TimerGenerator` that is used the same way,
but will return a generator object instead of a list.

For convenience, there is a generic factory class called `Timer` that is used as follows.
```python
from timer import Timer

start = 0          # time to start the timer at in seconds
sample_freq = 1000 # sampling frequency in Hz
samples = 10       # number of samples that will be taken

# Create the time instance as a list based timer
time_l = Timer.get_timer('list', start,sample_freq,samples)

# Create the time instance as a generator based timer
time_g = Timer.get_timer('gen', start,sample_freq,samples)
```

Timer objects contain a method `savetxt` that writes the full set of timer values to a simple text file. 
Usage is as follows:
```python
from timer import Timer

start = 0          # time to start the timer at in seconds
sample_freq = 1000 # sampling frequency in Hz
samples = 10       # number of samples that will be taken

# Create the time instance as a list based timer
time = Timer.get_timer('list', start,sample_freq,samples)

time.savetxt('test.txt')
```

Contents of `test.txt` <sup>[1]</sup>

```text
0.000
0.001
0.002
0.003
0.004
0.005
0.006
0.007
0.008
0.009

```


## Future Improvements
- add numpy compatibility 
- increase file write options
- support more file types (eg: csv, mat, binary representation, etc)

[py]:https://www.python.org/ "Python main page" 
[1]: # 'note the extra new line'