from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# 1. Load once
model_name = "gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token
model = AutoModelForCausalLM.from_pretrained(model_name)

def tokenize(text):
    return tokenizer(
        text,
        truncation=True,
        padding="max_length",
        max_length=128,
        return_tensors="pt"
    )

def get_data():
    data = [
        "### Instruction:\nWhat is self-attention?\n\n### Response:\nSelf-attention allows each token to attend to others.",
        "### Instruction:\nWhat is a transformer?\n\n### Response:\nA transformer is a neural network based on attention."
    ]
    return data

def train():
    optimizer = torch.optim.AdamW(model.parameters(), lr=5e-5)
    model.train()

    data = get_data()

    for step in range(3):
        text = data[step % len(data)]
        inputs = tokenize(text)

        input_ids = inputs["input_ids"]
        labels = input_ids.clone()

        optimizer.zero_grad()
        outputs = model(input_ids=input_ids, labels=labels)
        loss = outputs.loss
        loss.backward()
        optimizer.step()

        print(f"Step {step+1} | Loss: {loss.item():.4f}")

if __name__ == "__main__":
    train()
