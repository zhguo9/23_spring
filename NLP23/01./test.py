data = ["12","34"]
with open('/home/zhguo/git/NLP23/01./result.txt','w') as f:
    for d in data:
        f.write(d)
        f.write("\n")