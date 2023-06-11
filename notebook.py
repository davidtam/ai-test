from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers import LlamaForCausalLM, LlamaTokenizer
LLaMATokenizer = LlamaTokenizer
import torch
from timeit import timeit


model_name = "Neko-Institute-of-Science/LLaMA-7B-HF"
tokenizer = LLaMATokenizer.from_pretrained(model_name)
model = LlamaForCausalLM.from_pretrained(model_name)
# model = T5ForConditionalGeneration.from_pretrained(model_name)



for step in range(5):

    prompt = "Hey, are you consciours? Can you talk to me?"
    inputs = tokenizer(prompt, return_tensors="pt")

    def try_generate():
        generate_ids = model.generate(inputs.input_ids, max_length=300)
        print(tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0])
    # Generate
    timeit(try_generate, number=1)
    # # encode the new user input, add the eos_token and return a tensor in Pytorch
    # new_user_input_ids = tokenizer.encode(input(">> User:") + tokenizer.eos_token, return_tensors='pt')
    #
    # # append the new user input tokens to the chat history
    # bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids
    #
    # # generated a response while limiting the total chat history to 1000 tokens,
    # chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
    #
    # # pretty print last ouput tokens from bot
    # print("DialoGPT: {}".format(tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)))
