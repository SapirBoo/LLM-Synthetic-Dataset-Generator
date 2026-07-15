
import re
import json
import pandas as pd

def format_data(data):
  content = re.sub(r"<think>.*?</think>", "",data,
    flags=re.DOTALL).strip()

  #Find start of the Json 
  start = content.find("[")
  if start == -1:
    raise ValueError("No JSON found")

  content = content[start:]
  
  decoder = json.JSONDecoder()
  new_data, _ = decoder.raw_decode(content)


  return pd.DataFrame(new_data)
