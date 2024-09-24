from transformers import AutoModelForCausalLM, AutoTokenizer


checkpoint = "bigcode/starcoder"
device = "mac" # for GPU usage or "cpu" for CPU usage

tokenizer = AutoTokenizer.from_pretrained(checkpoint)
# to save memory consider using fp16 or bf16 by specifying torch_dtype=torch.float16 for example
model = AutoModelForCausalLM.from_pretrained(checkpoint).to(device)
