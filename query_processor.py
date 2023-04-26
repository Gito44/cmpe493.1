import pickle
import string
punct= string.punctuation
vowels=("a", "e", "i", "u", "o")
stop_words=("the","said","it","has","its","them","a","am","are","but","was","where","who","with","why","of","for","to",
            "on","i","be","by","and","an","will","at","in","reuter","from","that","is","pct","year","news","new",
            "have")


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

with open("dict","rb") as d:
    dictionary=pickle.load(d)

with open("post","rb") as p:
    postings=pickle.load(p)

final_post={}
def reverse_linked_list():
    for key in postings.keys():
        final_post[key]=LinkedList()
        for item in postings[key]:
            final_post[key].add(item[0],item[1])


reverse_linked_list()



def query_input():
    action=str(input('Enter search terms. Use ("") for phrase search'))
    if action[0] == '"':
        return action,0
    else:
        return action,1

def query_tokenizer(string):
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
    return string[1:-1]

def query_punct(string):
    for lett in punct:
        if lett == "-" or lett == "/":
                string = string.replace(lett, " ")
                string = string.lower()
        else:
            string = string.replace(lett, "")
            string = string.lower()
    return string

def find_numpos(first,second):
            firstpositions = first.position.split(", ")
            secondpositions = []
            for item in second.position.split(", "):
                secondpositions.append(int(item))
            for item in firstpositions:
                if int(item) + 1 in secondpositions:
                    numpos = int(item) + 1
                    data = int(first.data)
                    return numpos,data

                else:
                    return None,None
def remaining_words(numpos,data,word):
    while int(word.data) != data:
        word=word.next_node
        if int(word.data)<data:
            return None
    posisus=[]
    for item in word.position.split(", "):
        posisus.append(int(item))
    if numpos+1 in posisus:
        return numpos+1
    else:
        return None

def query(string,input):
    returned_docs=[]
    if input==1:
        qq=string.split()
        w1,w2,k =qq[0], qq[2], int(qq[1])+1
        ws1 = query_punct(w1)
        ws2 = query_punct(w2)
        wsf1=query_tokenizer(ws1)
        wsf2=query_tokenizer(ws2)

        if dictionary.search(wsf1)==True and dictionary.search(wsf2)==True:

            w1p=final_post[wsf1].root
            w2p=final_post[wsf2].root
            while w1p is not None:
                if int(w1p.data) > int(w2p.data):
                    w1p=w1p.next_node
                elif int(w1p.data) < int(w2p.data):
                    if w2p.next_node is not None:
                        w2p= w2p.next_node
                    else:
                        return returned_docs
                elif w1p.data == w2p.data:
                    w1positions=w1p.position.split(", ")
                    w2positions=[]
                    a=0
                    for item in w2p.position.split(", "):
                        w2positions.append(int(item))
                    for item in w1positions:
                        item_range= range(int(item)-k,int(item)+k+1)
                        for num in w2positions:
                            if num in item_range:
                                returned_docs.append(int(w1p.data))
                                w1p=w1p.next_node
                                a=1
                                break
                        break
                    if a ==0:
                        w1p=w1p.next_node

        return returned_docs
    elif input==0:
        string=query_punct(string)
        string=query_tokenizer(string)
        qq=string.split()
        words=[]
        for item in qq:
            words.append(item)
        for word in words:
            if dictionary.search(word) is None:
                return returned_docs
        first,second=final_post[words[0]].root,final_post[words[1]].root
        while first is not None:
            numpos = None
            data = 0
            if int(first.data) > int(second.data):
                first = first.next_node
            elif int(first.data) < int(second.data):
                if second.next_node is not None:
                    second = second.next_node
                else:
                    return None
            elif first.data == second.data:
                numpos,data= find_numpos(first,second)
                if numpos is not None:
                    for i in range(2,len(words)):
                        numpos= remaining_words(numpos,data,final_post[words[i]].root)
                        if numpos== None:
                            first=first.next_node
                            break
                    if numpos!=None:
                        returned_docs.append(int(data))
                        first=first.next_node
                else:
                    first=first.next_node

        return returned_docs


while True:
    a=input("Please enter a command. Enter: '-h' for help.")
    if a=="-h":
        print("Enter: '-h' for help. \n Enter: '-s' to search. \n Enter: '-q' to exit.")
    if a=="-q":
        break
    if a=="-s":
        search, inp = query_input()
        print("Here are the documents that match to your search.")
        result=query(search,inp)
        print(sorted(result))


