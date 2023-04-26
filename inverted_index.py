import sys
import string
import pickle
sys.setrecursionlimit(30000)
punct= string.punctuation
vowels=("a", "e", "i", "u", "o")
stop_words=("the","said","it","has","its","them","a","am","are","but","was","where","who","with","why","of","for","to",
            "on","i","be","by","and","an","will","at","in","reuter","from","that","is","have")

class News:
    def __init__(self, title, text, i):
        self.title=title
        self.text=text
        self.id=i


class TrieNode:
    def __init__(self, data):
        self.data=data
        self.is_End=False
        self.children={}

class Trie:
    def __init__(self):
        self.root= TrieNode("")

    def insert(self, word):
        current_node=self.root
        for letter in word:
            if letter in current_node.children:
                current_node=current_node.children[letter]
            else:
                current_node.children[letter]=TrieNode(letter)
                current_node=current_node.children[letter]
        if current_node.is_End == False:
            current_node.is_End=True

    def search(self, search_word):
        current_node=self.root
        word=str()
        for letter in search_word:
            if letter in current_node.children:
                current_node=current_node.children[letter]
                word+=current_node.data
            else:
                break
        if current_node.is_End:
            return True
        else:
            return None

class LinkedListNode:
    def __init__(self, d, p, n=None):
        self.data=d
        self.next_node=n
        self.position=str(p)


class LinkedList:
    def __init__(self, r=None ):
        self.root=r
        self.size=0

    def add(self, d,p):
        if self.root is not None:
            if self.root.data==d:
                self.root.position+= ", " + str(p)
                self.size+=1
            else:
                new_node=LinkedListNode(d,p,self.root)
                self.root=new_node
                self.size+=1
        else:
            new_node = LinkedListNode(d, p, self.root)
            self.root = new_node
            self.size += 1
    def print_list(self):
        this_node=self.root
        while this_node is not None:
            print(this_node.data + ":", this_node.position, end="->")
            this_node=this_node.next_node
        print("None")


def text_extractor(text, str1, str2, liste):
    if str1 and str2 in text:
        text_extractor(text[text.index(str2)+len(str2):],str1,str2,liste1)
        liste.append(text[text.index(str1)+len(str1):text.index(str2)])
    else:
        return


def dissector(text):
    if '<TEXT TYPE="UNPROC">' in text:
        id = text[text.index('NEWID="') + len('NEWID="'):text.index('">')]
        body = text[text.index('<TEXT TYPE="UNPROC">&#2;') + len('<TEXT TYPE="UNPROC">&#2;'):text.index('</TEXT>')]
        return News(None,body,id)
    else:
        title=text[text.index("<TITLE>")+len("<TITLE>"):text.index("</TITLE>")]
        id=text[text.index('NEWID="')+len('NEWID="'):text.index('">')]
        if "<BODY>" in text:
            body=text[text.index("<BODY>")+len("<BODY>"):text.index("</BODY>")]
            return News(title,body,id)
        else:
            return News(title, None, id)

def news_tokenizer(string):
    string= " " + string + " "
    string= string.replace("\n", " ")
    for word in string.split():
        replace= " " + word + " "
        if word in stop_words:
            string=string.replace(replace," ")
        if word.isalpha()==False:
            string=string.replace(replace," ")
        elif word[0:2] == "lt":
            string=string.replace(replace, " ")
        else:
            if word[-4:] == "sses":
                string=string.replace(replace, " "+ word[:-2] +" ")
            elif word[-3:] == "ies":
                string=string.replace(replace," "+ word[:-2] +" ")
            elif word[-3:] == "ing":
                for vowel in vowels:
                    if vowel in word[:-3]:
                        string=string.replace(replace," "+ word[:-3] +" ")
            if word[-1:] == "s" and word[-2:] != "ss":
                string=string.replace(replace," "+ word[:-1] +" ")
    return string



file0=open("reut2-000.sgm" , encoding='iso-8859-1')
a0=file0.read()
file1=open("reut2-001.sgm",encoding='iso-8859-1')
a1=file1.read()
file2=open("reut2-002.sgm",encoding='iso-8859-1')
a2=file2.read()
file3=open("reut2-003.sgm",encoding='iso-8859-1')
a3=file3.read()
file4=open("reut2-004.sgm",encoding='iso-8859-1')
a4=file4.read()
file5=open("reut2-005.sgm",encoding='iso-8859-1')
a5=file5.read()
file6=open("reut2-006.sgm",encoding='iso-8859-1')
a6=file6.read()
file7=open("reut2-007.sgm",encoding='iso-8859-1')
a7=file7.read()
file8=open("reut2-008.sgm",encoding='iso-8859-1')
a8=file8.read()
file9=open("reut2-009.sgm",encoding='iso-8859-1')
a9=file9.read()
file10=open("reut2-010.sgm",encoding='iso-8859-1')
a10=file10.read()
file11=open("reut2-011.sgm",encoding='iso-8859-1')
a11=file11.read()
file12=open("reut2-012.sgm",encoding='iso-8859-1')
a12=file12.read()
file13=open("reut2-013.sgm",encoding='iso-8859-1')
a13=file13.read()
file14=open("reut2-014.sgm",encoding='iso-8859-1')
a14=file14.read()
file15=open("reut2-015.sgm",encoding='iso-8859-1')
a15=file15.read()
file16=open("reut2-016.sgm",encoding='iso-8859-1')
a16=file16.read()
file17=open("reut2-017.sgm",encoding='iso-8859-1')
a17=file17.read()
file18=open("reut2-018.sgm",encoding='iso-8859-1')
a18=file18.read()
file19=open("reut2-019.sgm",encoding='iso-8859-1')
a19=file19.read()
file20=open("reut2-020.sgm",encoding='iso-8859-1')
a20=file20.read()
file21=open("reut2-021.sgm",encoding='iso-8859-1')
a21=file21.read()

b="<REUTERS"
c="</REUTERS>"
liste1=[]
news=[]

text_extractor(a21,b,c,liste1)
text_extractor(a20,b,c,liste1)
text_extractor(a19,b,c,liste1)
text_extractor(a18,b,c,liste1)
text_extractor(a17,b,c,liste1)
text_extractor(a16,b,c,liste1)
text_extractor(a15,b,c,liste1)
text_extractor(a14,b,c,liste1)
text_extractor(a13,b,c,liste1)
text_extractor(a12,b,c,liste1)
text_extractor(a11,b,c,liste1)
text_extractor(a10,b,c,liste1)
text_extractor(a9,b,c,liste1)
text_extractor(a8,b,c,liste1)
text_extractor(a7,b,c,liste1)
text_extractor(a6,b,c,liste1)
text_extractor(a5,b,c,liste1)
text_extractor(a4,b,c,liste1)
text_extractor(a3,b,c,liste1)
text_extractor(a2,b,c,liste1)
text_extractor(a1,b,c,liste1)
text_extractor(a0,b,c,liste1)

file0.close()
file1.close()
file2.close()
file3.close()
file4.close()
file5.close()
file6.close()
file7.close()
file8.close()
file9.close()
file10.close()
file11.close()
file12.close()
file13.close()
file14.close()
file15.close()
file16.close()
file17.close()
file18.close()
file19.close()
file20.close()
file21.close()


for item in liste1:
    news.append(dissector(item))

for item in news:
    for lett in punct:
        if lett == "-" or lett =="/":
            if item.title is not None:
                item.title= item.title.replace(lett," ")
                item.title= item.title.lower()
            if item.text is not None:
                item.text= item.text.replace(lett," ")
                item.text=item.text.lower()
        else:
            if item.title is not None:
                item.title= item.title.replace(lett,"")
                item.title= item.title.lower()
            if item.text is not None:
                item.text= item.text.replace(lett,"")
                item.text=item.text.lower()

for new in news:
    if new.title is not None:
        new.title=news_tokenizer(new.title)
    if new.text is not None:
        new.text = news_tokenizer(new.text)

dictionary=Trie()
postings={}
for new in news:
    counter=0
    if new.title is not None:
        for word in new.title.split():
            counter+=1
            try:
                postings[word]
            except:
                postings[word]=LinkedList()
            dictionary.insert(word)
            postings[word].add(new.id,counter)

    if new.text is not None:
        for word in new.text.split():
            counter+=1
            try:
                postings[word]
            except:
                postings[word]=LinkedList()
            dictionary.insert(word)
            postings[word].add(new.id, counter)




def linked_list_to_list(head):
    lst = []
    current = head
    while current is not None:
        lst.append((current.data,current.position))
        current = current.next_node
    return lst


second_post={}
for key in postings.keys():
    second_post[key]=linked_list_to_list(postings[key].root)


with open("dict","wb") as d:
    pickle.dump(dictionary,d)
    d.close()

with open("post","wb") as p:
    pickle.dump(second_post,p)
    p.close()