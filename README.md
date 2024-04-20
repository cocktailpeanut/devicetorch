# devicetorch

![img.png](img.png)

get torch device in one line

# Install

```
pip install devicetorch
```

# Usage

```
import torch
import devicetorch
device = devicetorch.get(torch)    # pass in the existing torch object
```

The value of `device` will be one of the following:

- `mps`: Apple silicon mac
- `cuda`: CUDA
- `cpu`: The rest
