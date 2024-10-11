# Example of fine-tuning
from datasets import load_dataset
from transformers import Seq2SeqTrainer, Seq2SeqTrainingArguments

dataset = load_dataset("path_to_your_dataset")  # Contains your code-text pairs

training_args = Seq2SeqTrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    weight_decay=0.01,
    save_total_limit=3,
    num_train_epochs=3,
)

trainer = Seq2SeqTrainer(
    model=model,
    args=training_args,
    train_dataset=dataset['train'],
    eval_dataset=dataset['eval'],
)

trainer.train()
