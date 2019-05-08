# coding: utf-8

import spacy

### Load spaCy's English NLP model
nlp = spacy.load('en_core_web_lg')

### The text we want to examine
text = "Amazon.com, Inc., doing business as Amazon, is an American electronic commerce and cloud computing company based in Seattle, Washington, that was founded by Jeff Bezos on July 5, 1994. The tech giant is the largest Internet retailer in the world as measured by revenue and market capitalization, and second largest after Alibaba Group in terms of total sales. The amazon.com website started as an online bookstore and later diversified to sell video downloads/streaming, MP3 downloads/streaming, audiobook downloads/streaming, software, video games, electronics, apparel, furniture, food, toys, and jewelry. The company also produces consumer electronics - Kindle e-readers, Fire tablets, Fire TV, and Echo - and is the world's largest provider of cloud infrastructure services (IaaS and PaaS). Amazon also sells certain low-end products under its in-house brand AmazonBasics."

### Parse the text with spaCy
### Our 'document' variable now contains a parsed version of text.
document = nlp(text)

### print out all the named entities that were detected
for entity in document.ents:
    print(entity.text, entity.label_)

    
