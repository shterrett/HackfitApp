def get_weight(data):
  avg = sum(data) / len(data)
  if avg < 2:
    return 10
  else:
    return 40
