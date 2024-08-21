# graveler-attempts-python

An optimization of [ShoddyCast's code](https://github.com/arhourigan/graveler/blob/main/graveler.py) that simulates attempts of escaping [Pikasprey's Graveler Soft-Lock](https://www.youtube.com/watch?v=GgMl4PrdQeo&t=0s).

On my AMD Ryzen 7 5800X 8-Core Processor this takes me roughly 57 seconds (not including numba compiling).

This could be faster by using a different language such as C, but the goal was to get a fast time using the original language used by ShoddyCast (Python).

## Installation
Navigate to the project folder and install the dependencies.
```
pip install requirements.txt
```
Then run using:
```
python3 graveler.py
```