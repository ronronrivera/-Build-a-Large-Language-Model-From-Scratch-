# Build a Large Language Model From Scratch

<p align="center">
  <img src="path/to/your-image.png" alt="Project banner" width="700">
</p>

This repository is my hands-on journey of building a GPT-style Large Language Model from the ground up, following Sebastian Raschka's book **[Build a Large Language Model (From Scratch)](https://www.manning.com/books/build-a-large-language-model-from-scratch)**.

Instead of relying on high-level libraries, the goal is to understand how an LLM works by implementing each component myself: from turning raw text into tokens all the way to pretraining and fine-tuning a working model.

## What This Repo Does

The project works through the full LLM pipeline, one step at a time:

1. **Working with text data**: tokenizing raw text, building a vocabulary, converting tokens to IDs, and preparing input–target pairs with a sliding window.
2. **Attention mechanisms**: implementing self-attention, causal (masked) attention, and multi-head attention.
3. **GPT architecture**: assembling transformer blocks, layer normalization, feed-forward layers, and shortcut connections into a GPT model.
4. **Pretraining**: training the model on unlabeled text and generating new text.
5. **Fine-tuning**: adapting the model for tasks like text classification and following instructions.


## Acknowledgements

- **Sebastian Raschka**, *Build a Large Language Model (From Scratch)*, Manning Publications, 2024
- Official book repository: [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch)
- Sample text: *The Verdict* by Edith Wharton (public domain)

## License

This project is for educational purposes. Code concepts are based on the book by Sebastian Raschka.
