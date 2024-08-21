# graveler-attempts-python

An optimization of [ShoddyCast's code](https://github.com/arhourigan/graveler/blob/main/graveler.py) that simulates attempts of escaping [Pikasprey's Graveler Soft-Lock](https://www.youtube.com/watch?v=GgMl4PrdQeo&t=0s).

On my Windows Computer with an AMD Ryzen 7 5800X 8-Core Processor, this takes me roughly 57 seconds. On my MacBook Pro 2020 with an Apple M1, this takes me roughly 82 seconds.

Note: Timing does not include setting process priority or numba compilation.

This could be faster by using a different language such as C, but the goal was to get a fast time using the original language used by ShoddyCast (Python).

## Installation
Navigate to the project folder and install the dependencies.
```
pip install -r requirements.txt
```
Then run using:
```
python3 graveler.py
```
