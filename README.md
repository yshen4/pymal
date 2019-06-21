# pymal
MIT machine learning 

# Setup

using Python 3.6+ along with the following packages.
- NumPy
- matplotlib
- SciPy
- tqdm
- PyTorch

## Install python3 and requirements
- Install homebrew: ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
- export PATH=/usr/local/bin:/usr/local/sbin:$PATH
- brew install python3
- brew install libomp
  - for mac, install libomp: fail to load libomp.dylib when importing torch
- install requirements
  - pip3 install -r requirements.txt 

## Verify the installation
```
>>> from __future__ import print_function
>>> import torch
>>> x = torch.rand(5, 3)
>>> print(x)
tensor([[0.1215, 0.6205, 0.9084],
        [0.0900, 0.8290, 0.6976],
        [0.4567, 0.3172, 0.1424],
        [0.9550, 0.0258, 0.3253],
        [0.7004, 0.5671, 0.6638]])
>>> torch.cuda.is_available()
False
```
