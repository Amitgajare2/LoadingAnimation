
import time

def typewriter(text, delay=0.1):
  for letter in text:
    print(letter, end='', flush=True)
    time.sleep(delay)
  print()
    
typewriter("▁ ▂ ▃ ▄ ▅ ▆ ▇ █ ▇ ▆ ▅ ▄ ▃ ▁", 0.09)



