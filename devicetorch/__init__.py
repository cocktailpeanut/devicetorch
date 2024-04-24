def get(torch):
  if torch.backends.mps.is_available():
    return "mps"
  elif torch.cuda.is_available():
    return "cuda"
  else:
    return "cpu"
def empty_cache(torch):
  if torch.backends.mps.is_available():
    torch.mps.empty_cache()
  elif torch.cuda.is_available():
    torch.cuda.empty_cache()
def to(torch, input):
  if torch.backends.mps.is_available():
    return input.to("mps")
  elif torch.cuda.is_available():
    return input.to("cuda")
  else:
    return input
def dtype(torch, type=None):
  """
  dtype(torch, "float16") # try to get float16: mps=float16 cuda=float16 cpu=float32
  dtype(torch)            # mps=float32 cuda=float16 cpu=float32
  """
  if torch.backends.mps.is_available():
    if type == "float16":
      return torch.float16
    else:
      return torch.float32
  elif torch.cuda.is_available():
    return torch.float16
  else:
    return torch.float32
