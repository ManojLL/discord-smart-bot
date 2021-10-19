from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import spacy

# Load English tokenizer, tagger, parser, NER and word vectors
spacy.load('en')

def train_bot():
    # Create a new chat bot named Discord-ChatBot
    chatbot = ChatBot("Discord-ChatBot")
    
    print("\nTraning Discord-ChatBot\n")

    # Create a new trainer for the chatbo
    trainer = ChatterBotCorpusTrainer(chatbot)

    # Train based on the english corpus
    trainer.train("chatterbot.corpus.english")

    # Train based on english greetings corpus
    trainer.train("chatterbot.corpus.english.greetings")

    # Train based on the english conversations corpus
    trainer.train("chatterbot.corpus.english.conversations")

    print("\nTraining completed")
    
    return chatbot

# message = ""
# while message.lower() not in ("q", "quit", "exit"):
#     message = input("You: ")
#     print(f'bot : {chatbot.get_response(message)}')