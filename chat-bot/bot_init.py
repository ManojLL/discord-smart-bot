from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import spacy

# Load English tokenizer, tagger, parser, NER and word vectors
spacy.load("en_core_web_sm")

 # Create a new chat bot named Discord-ChatBot
chatbot = ChatBot("Discord-ChatBot", storage_adapter="chatterbot.storage.SQLStorageAdapter")

def train_bot(): 
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