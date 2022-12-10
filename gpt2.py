from transformers import GPT2Tokenizer, GPT2Model
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2Model.from_pretrained('gpt2')
text = "write an email to dr. chen proposing we move to the new VR lab"
encoded_input = tokenizer(text, return_tensors='pt')
output = model(**encoded_input)
