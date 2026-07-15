from config import HF_MODELS, system_message
from prompts import build_user_prompt
from model import load_model
from formatter import format_data

def generate_data(model,prompt_style,studio_style,studio_type,rows,description,topic):

  if prompt_style == "Creative":
    instruction = """
    Generate unusual class names.
    Create diverse instructors."""

  elif prompt_style == "Realistic":
    instruction = """
    Generate highly realistic data."""

  else:
    instruction = """
    Generate diverse data.
    Avoid duplicated instructors."""


  user_data=build_user_prompt(topic,studio_style,studio_type,rows,description+instruction)
  messages=[
      {"role": "system", "content": system_message},
      {"role": "user", "content": user_data}
  ]
  tokenizer,model=load_model(HF_MODELS[model])
  inputs = tokenizer.apply_chat_template( messages,tokenize=True,add_generation_prompt=True,return_tensors="pt").to("cuda")

  outputs = model.generate(
    **inputs,
    max_new_tokens=4000,
)

  generated_tokens = outputs[0][inputs["input_ids"].shape[-1]:]
  generated = tokenizer.decode(
    generated_tokens,
    skip_special_tokens=True
)

  if isinstance(generated, list):
    generated = generated[0]

  data=format_data(generated)
  data.to_csv("synthetic_dataset.csv", index=False)
  return data,"synthetic_dataset.csv"
