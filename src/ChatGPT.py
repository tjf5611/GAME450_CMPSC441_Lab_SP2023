from sentence_transformers import SentenceTransformer, util
sentences = ["Sure! Here's an interesting fact: The shortest war in history was between Britain and Zanzibar on August 27, 1896. The war lasted just 38 minutes, with Zanzibar surrendering to Britain after their palace was bombarded.", 
             "Sure, here's a fact: The human nose can detect over 1 trillion different scents, making it one of the most powerful senses in the body. This is due to the olfactory receptor neurons located in the nasal cavity, which are capable of detecting a vast range of smells, from the pleasant to the unpleasant."]

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

embedding_1 = model.encode(sentences[0], convert_to_tensor=True)
embedding_2 = model.encode(sentences[1], convert_to_tensor=True)

util.pytorch_cos_sim(embedding_1,embedding_2)