def get(torch):
  if torch.backends.mps.is_available():
    return "mps"
  elif torch.cuda.is_available():
    return "cuda"
  else:
    return "cpu"
