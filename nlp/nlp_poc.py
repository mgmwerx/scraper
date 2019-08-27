import spacy

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load("en_core_web_sm")

# Process whole documents
#text = ("AGLOW International meets every third Thursday, 9:30 at the Montgomery House of Prayer. All women welcome to join together for praise, prayer and an anointed message. Contact mboudousquie@yahoo.com.")

#text = ("Bridge of Life Assembly of God, 9000 Vaughn Road, Montgomery, holds Sunday morning worship at 10:30 a.m. each week. Sunday school classes meet at 9:30 a.m. We offer classes for all age groups and childcare is provided. Our goal is to build bridges...not walls. We invite you to come join us if you need to learn how to build those bridges. For directions or information call 334-396-0208. Visit www.bridgeoflife.tv.")

text = ("Central Community Christian Church, 981 South Perry Street, Montgomery, holds new members training classes on Sundays at 9 a.m. Sunday School (9:30), morning worship (11:00), Tuesday night Bible study (6:30). Every fourth Sunday of the month is our youth Sunday. For more information please call (334) 269-0457 or by email at centralccchurch1@gmail.com.")

doc = nlp(text)

# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)
