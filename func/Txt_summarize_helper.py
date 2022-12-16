from transformers import PegasusForConditionalGeneration
from transformers import PegasusTokenizer
from transformers import pipeline

class Summarize(object):
    
    def __init__(self):
        self.tokenizer = PegasusTokenizer.from_pretrained("google/pegasus-xsum")
        self.model = PegasusForConditionalGeneration.from_pretrained("google/pegasus-xsum")

    def summarize(self, target_text):
        tokens = self.tokenizer(target_text, truncation=True, padding="longest", return_tensors="pt")
        summary = self.model.generate(**tokens, min_length = 80, max_length = 120)
        return self.tokenizer.decode(summary[0])