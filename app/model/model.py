import pickle
import re
from pathlib import Path

__version__ = '0.1.0'

BASE_DIR = Path(__file__).resolve(strict=True).parent

with open(f'{BASE_DIR}/classify_news_pipeline-{__version__}.pkl', 'rb') as f:
    model = pickle.load(f)

classes = [
    'Politics',
    'Sport',
    'Technology',
    'Entertainment',
    'Business'
]

def predict_pipeline(text):
    text = re.sub(r'[!@#$(),\n"%^*?\:;~`0-9]', ' ', text)
    text = re.sub(r'[[]]', ' ', text)
    text = text.lower()

    probabilities = model.predict_proba([text]).tolist()
    probs_percentage = [[round(prob * 100, 4) for prob in probs] for probs in probabilities]

    class_probs = dict(zip(classes, probs_percentage[0]))

    return class_probs