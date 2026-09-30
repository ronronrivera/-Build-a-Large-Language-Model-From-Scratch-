import tiktoken

from utils import create_dataloader

with open('the-verdict.txt', "r", encoding="utf-8") as f:
    raw_text = f.read()



# preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
# preprocessed = [item.strip() for item in preprocessed if item.strip()]
#
# all_words = sorted(set(preprocessed))
# all_words.extend(["<|endoftext|>", "<|unk|>"])
#
# vocab_size = len(all_words)
#
# vocab = {token:integer for integer, token in enumerate(all_words)}

tokenizer = tiktoken.get_encoding('gpt2')

enc_text = tokenizer.encode(raw_text)
# print(len(enc_text))

enc_sample = enc_text[50:]

context_size = 4
x = enc_sample[:context_size]
y = enc_sample[1:context_size+1]

# print(f"x: {x}")
# print(f"y:      {y}")

dataloader = create_dataloader(
        raw_text, batch_size=1, max_length=4, stride=1, shuffle=False
    )
data_iter = iter(dataloader)
first_batch = next(data_iter)

print(first_batch)

# text = (
#     "Hello, do you like tea? <|endoftext|> In the sunlit terraces"
#     "of someunknownPlace. akjfhdfgdbsjfgbdfhgdkjlfhgdkjl"
# )
#
# integers = tokenizer.encode(text, allowed_special={"<|endoftext|>"})
#
# strings = tokenizer.decode(integers)
#
# print(integers)
