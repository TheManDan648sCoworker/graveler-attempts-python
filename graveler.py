import time
import sys
import os

from numba import jit, prange, int8
import numpy as np
import psutil

ROLLS = 1_000_000_000
ATTEMPTS = 231

@jit(int8(), nopython=True, parallel=True)
def graveler():
    maxOnes = 0
    for _ in prange(ROLLS):
        numbers = np.random.randint(0, 4, size=ATTEMPTS)
        ones = np.sum(numbers == 0)
        maxOnes = max(maxOnes, ones)
    return maxOnes

# Sets priority mode of this process to high.
p = psutil.Process(os.getpid())
if sys.platform == 'win32':
    p.nice(psutil.HIGH_PRIORITY_CLASS)
elif sys.platform == 'linux':
    p.nice(psutil.IOPRIO_HIGH)
else:
    p.nice(10)

start = time.time()
maxOnes = graveler()
end = time.time()

print('Highest Ones Roll:', maxOnes)
print('Number of Roll Sessions:', ROLLS)
print(f'Took {end - start} seconds.')