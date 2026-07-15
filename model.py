# define helper function to load model and tokenizer - include cache
from transformers import AutoTokenizer, AutoModelForCausalLM, TextStreamer, BitsAndBytesConfig, TextIteratorStreamer
import re
import torch
from functools import lru_cache

@lru_cache(maxsize=4)
def load_model(model_name):
  quant_config = BitsAndBytesConfig(
      load_in_4bit=True,
      bnb_4bit_use_double_quant=True,
      bnb_4bit_compute_dtype=torch.bfloat16,
      bnb_4bit_quant_type="nf4"
  )
  tokenizer = AutoTokenizer.from_pretrained(model_name)
  tokenizer.pad_token = tokenizer.eos_token
  model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", quantization_config=quant_config)
  return tokenizer,model
