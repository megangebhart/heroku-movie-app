from spacy.lang.en import English
import pandas as pd
from spacy.lang.en.stop_words import STOP_WORDS
import texthero as hero
from scipy import sparse
import pickle
def classification_func(review):
    # Load English tokenizer, tagger, parser, NER and word vectors
    nlp = English()
    #  "nlp" Object is used to create documents with linguistic annotations.
    my_doc = nlp(review)
    # Create list of word tokens
    token_list = []
    for token in my_doc:
        token_list.append(token.text)
    # Create list of word tokens after removing stopwords
    filtered_sentence =[] 
    for word in token_list:
        lexeme = nlp.vocab[word]
        if lexeme.is_stop == False:
            filtered_sentence.append(word) 
   
    complete_text = ' '.join(word for word in filtered_sentence)
    review_df = pd.DataFrame()
    review_df["text"] = [complete_text] 
    review_df["tfidf"] = (hero.tfidf(review_df["text"], max_features=3000))
    sA = sparse.csr_matrix(review_df["tfidf"][0]) 

    loaded_model = pickle.load(open("final_model.sav", 'rb'))
    result = loaded_model.predict(sA)
    # print("results: ", result)
    return(result[0])
