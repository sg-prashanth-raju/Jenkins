import fire

def hello(name="Prashanth"):
  return "Hello %s!" % name

if __name__ == '__main__':
  fire.Fire(hello)