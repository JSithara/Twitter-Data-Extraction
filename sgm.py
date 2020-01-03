f = open("files/reut2-020.sgm")
content = f.read()
process_content = content.split("</REUTERS>")
index = 0
for input in process_content:
    article = input.split('<REUTERS')
    index=index+1
    if(len(article) >= 2):
        article_start = article[1].find(">")
        f = open("files/result20/"+str(index)+".txt","w")
        f.write(article[1][article_start+1:])
        f.close()
        
