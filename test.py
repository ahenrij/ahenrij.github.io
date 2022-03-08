def hello(msg):
    """Great with message."""
    print(f'Hello, {msg}')

def pairs():
  for i in range(100):
    if i%2 == 0:
      print(i)
  print("done!")

hello("Henri")
pairs()