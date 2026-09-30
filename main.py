import re

from importlib.metadata import version
import tiktoken

from text_tokenizer import SimpleTokenizer


with open('the-verdict.txt', "r", encoding="utf-8") as f:
    raw_text = f.read()


preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]

all_words = sorted(set(preprocessed))
all_words.extend(["<|endoftext|>", "<|unk|>"])

vocab_size = len(all_words)

vocab = {token:integer for integer, token in enumerate(all_words)}

tokenizer = tiktoken.get_encoding('gpt2')

text = (
    "Hello, do you like tea? <|endoftext|> In the sunlit terraces"
    "of someunknownPlace. akjfhdfgdbsjfgbdfhgdkjlfhgdkjl"
)

integers = tokenizer.encode(text, allowed_special={"<|endoftext|>"})

strings = tokenizer.decode(integers)

print(integers)
