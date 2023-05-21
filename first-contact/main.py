#Code highly based on https://github.com/Me163/youtube/blob/main/Transformers/repl.py exemple's
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM,GenerationConfig
import sys
line = 'What color is the undoubtely beutiful sky?'

#xl feels laggy on a PC with:
#R5 3600@4.15GHz - 2060 16GB 3200MHz
model_name = 'google/flan-t5-base'
tokenizer = AutoTokenizer.from_pretrained(model_name)
tokens = tokenizer.tokenize(line)

#print(tokens)
ids = tokenizer.convert_tokens_to_ids(tokens)
#print(ids)

#Do both function
##token = tokenizer(line, return_tensors="pt")
##print(token)

#Pick right class base on name of the model
config = GenerationConfig(max_new_tokens=200)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

#Just a observation for how vector look like
##input_embeddings = model.get_input_embeddings()
##token_ids = token['input_ids'][0]
##our_embeddings = input_embeddings(token_ids)
##print(our_embeddings)

for line in sys.stdin:
	#Pratical
	token = tokenizer(line, return_tensors="pt")
	outputs = model.generate(**token, GenerationConfig=config)
	#decode vectors
	#"skip_special_tokens" Skip special artifacts that model generate
	print(tokenizer.batch_decode(outputs, skip_special_tokens=True))