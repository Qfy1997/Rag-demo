from sentence_transformers import SentenceTransformer,util
import faiss
import torch
from transformers import AutoModel, AutoTokenizer
import time
import warnings
warnings.filterwarnings("ignore")

if __name__=='__main__':
    query="我在广场跑步的时候把棉袄挂在栏杆上了，结果棉袄被别人拿走了，请问拿走我棉袄的那个人犯法吗？"
    model = SentenceTransformer('simcse_law_bert_base_chinese')
    sentences = []
    prompt = []
    prompt_content="法律知识提示:"
    with open("./law.txt",'r') as f:
        lines = f.readlines()
        for line in lines:
            sentences.append(line)
    # print(len(sentences))
    embeddings = model.encode(sentences)
    sim = util.cos_sim(embeddings[0],embeddings[1])
    # print(sim)
    # print(embeddings[2])
    # print(embeddings[2].shape)
    # print(embeddings.shape)
    # print(type(embeddings))
    dimension=embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    # print(index.ntotal)
    topK = 1
    search = model.encode([query])
    D,I = index.search(search,topK)
    # df['sentence'].iloc[I[0]]
    # print(D)
    # print(I)
    # print(sentences[I[0][0]].strip())
    # print(sentences[I[0][1]].strip())
    # print(sentences[I[0][2]].strip())
    for i in range(topK):
        # prompt.append(sentences[I[0][i]].strip())
        prompt_content+=sentences[I[0][i]].strip()+"、"
    # print(prompt)
    prompt_content=prompt_content[:-1]+"。"
    # print(prompt_content)
    query_prompt=query+prompt_content
    print(query_prompt)
    model_path = './LLMs/chatglm-6b-int4'
    start=time.time()
    tokenizer = AutoTokenizer.from_pretrained(model_path,trust_remote_code=True)
    model = AutoModel.from_pretrained(model_path, trust_remote_code=True).float()
    response, history = model.chat(tokenizer,query_prompt,history=[])
    end = time.time()-start
    print("调用chatGlm耗时",end,"s。")
    print(response)
    # print(history)
    
    