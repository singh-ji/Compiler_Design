
#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Lexical analyser Experiment 1
import re
import string
f = open('Desktop/input.c', 'r')
operators = ['=', '+', '-', '/', '*', '++', '--', '==', '>', '<', '>=', '<=']
keywords = ['<math.h>', '<stdio.h>', '<string.h>', '<conio.h>','void','int', 'float', 'char', 'long', 'return', 'if', 'else', 'include', 'special_symbol_countanf','printf', 'main']
identifiers = ['n1', 'n2', 'n3','a','b','c']
symbols = ['{', '}', '[', ']', '(', ')', '#', ';', ',', '"']
operator_count = 0
keyword_count = 0
identifier_count = 0
special_symbol_count = 0
op = []
ke = []
ide = []
sy = []
i = f.read()
count = 0
program = i.split('\n')
for line in program:
    tokens = line.split()
    for token in tokens:
        if token in operators:
            operator_count += 1
            if token not in op:
                op.append(token)
        elif token in keywords:
            keyword_count += 1
            if token not in ke:
                ke.append(token)
        elif token in identifiers:
            identifier_count += 1
            if token not in ide:
                ide.append(token)
        elif token in symbols:
            special_symbol_count += 1
            if token not in sy:
                sy.append(token)
print("\n************************************************************\n")
print("Operator Count: {}".format(operator_count))
print("Operators",op)
print("\n************************************************************\n")
print("Keyword Count: {}".format(keyword_count))
print("Keywords",ke)
print("\n************************************************************\n")
print("Identifier Count: {}".format(identifier_count))
print("Identifiers",ide)
print("\n************************************************************\n")
print("Others: {}".format(special_symbol_count))
print("Others",sy)
f.close()


# In[3]:


#EXPERIMENT 2 RE TO NFA
transition_table = [ [0]*3 for _ in range(20) ]
re = input("Enter the regular expression : ")
re += " "
i = 0
j = 1
N = len(re)
while(i<N):
    if re[i] == 'a':
        try:
            if re[i+1] != '|' and re[i+1] !='*':
                transition_table[j][0] = j+1
                j += 1
            elif re[i+1] == '|' and re[i+2] =='b':
                transition_table[j][2]=((j+1)*10)+(j+3)
                j+=1
                transition_table[j][0]=j+1
                j+=1
                transition_table[j][2]=j+3
                j+=1
                transition_table[j][1]=j+1
                j+=1
                transition_table[j][2]=j+1
                j+=1
                i=i+2
            elif re[i+1]=='*':
                transition_table[j][2]=((j+1)*10)+(j+3)
                j+=1
                transition_table[j][0]=j+1
                j+=1
                transition_table[j][2]=((j+1)*10)+(j-1)
                j+=1
        except:
            transition_table[j][0] = j+1
    elif re[i] == 'b':
        try:
            if re[i+1] != '|' and re[i+1] !='*':
                transition_table[j][1] = j+1
                j += 1
            elif re[i+1]=='|' and re[i+2]=='a':
                transition_table[j][2]=((j+1)*10)+(j+3)
                j+=1
                transition_table[j][1]=j+1
                j+=1
                transition_table[j][2]=j+3
                j+=1
                transition_table[j][0]=j+1
                j+=1
                transition_table[j][2]=j+1
                j+=1
                i=i+2
            elif re[i+1]=='*':
                transition_table[j][2]=((j+1)*10)+(j+3)
                j+=1
                transition_table[j][1]=j+1
                j+=1
                transition_table[j][2]=((j+1)*10)+(j-1)
                j+=1
        except:
            transition_table[j][1] = j+1
    elif re[i]=='e' and re[i+1]!='|'and re[i+1]!='*':
        transition_table[j][2]=j+1
        j+=1
    elif re[i]==')' and re[i+1]=='*':
        transition_table[0][2]=((j+1)*10)+1
        transition_table[j][2]=((j+1)*10)+1
        j+=1
    i +=1
print ("Transition function:")
for i in range(j):
    if(transition_table[i][0]!=0):
        print("q[{0},a]-->{1}".format(i,transition_table[i][0]))
    if(transition_table[i][1]!=0):
        print("q[{0},b]-->{1}".format(i,transition_table[i][1]))
    if(transition_table[i][2]!=0):
        if(transition_table[i][2]<10):
            print("q[{0},e]-->{1}".format(i,transition_table[i][2]))
        else:
            print("q[{0},e]-->{1} & {2}".format(i,int(transition_table[i][2]/10),transition_table[i][2]%10))


# In[ ]:





# In[1]:


#Experiment 3 NFA TO DFA
import pandas as pd

nfa = {}
n = int(input("No. of states : "))
t = int(input("No. of transitions : "))
for i in range(n):
    state = input("state name : ")
    nfa[state] = {}
    for j in range(t):
        path = input("path : ")
        print("Enter end state from state {} travelling through path {} : ".format(state, path))
        reaching_state = [x for x in input().split()]
        nfa[state][path] = reaching_state

print("\nNFA :- \n")
print(nfa)
print("\nPrinting NFA table :- ")
nfa_table = pd.DataFrame(nfa)
print(nfa_table.transpose())

print("Enter final state of NFA : ")
nfa_final_state = [x for x in input().split()]

new_states_list = []


dfa = {}
keys_list = list(
    list(nfa.keys())[0])
path_list = list(nfa[keys_list[0]].keys())

dfa[keys_list[0]] = {}
for y in range(t):
    var = "".join(nfa[keys_list[0]][
                      path_list[y]])
    dfa[keys_list[0]][path_list[y]] = var
    if var not in keys_list:
        new_states_list.append(var)
        keys_list.append(var)

while len(new_states_list) != 0:
    dfa[new_states_list[0]] = {}
    for _ in range(len(new_states_list[0])):
        for i in range(len(path_list)):
            temp = []
            for j in range(len(new_states_list[0])):
                temp += nfa[new_states_list[0][j]][path_list[i]]
            s = ""
            s = s.join(temp)
            if s not in keys_list:
                new_states_list.append(s)
                keys_list.append(s)
            dfa[new_states_list[0]][path_list[i]] = s

    new_states_list.remove(new_states_list[0])

print("\nDFA :- \n")
print(dfa)
print("\nPrinting DFA table :- ")
dfa_table = pd.DataFrame(dfa)
print(dfa_table.transpose())

dfa_states_list = list(dfa.keys())
dfa_final_states = []
for x in dfa_states_list:
    for i in x:
        if i in nfa_final_state:
            dfa_final_states.append(x)
            break

print("\nFinal states of the DFA are : ", dfa_final_states)


# In[13]:


#EXPERIMENT 4.1 Removing left recursion 
#Pragya Bharti RA1911030010063 
gram = {}

def add(str):                              
    x = str.split("->") #splitting the input string with -> as a separator
    y = x[1] #storing the first character of the list x in y
    x.pop() #returns the last value of the list  
    z = y.split("|") #splits the rhs with | as a separator
    x.append(z) #makes a list of all the characters ex: ['A','Ab','B']
    gram[x[0]]=x[1] #gram[A]='Ab' A is key and Ab is value

def removeDirectLR(gramA, A):        # This function is used to remove the direct left recursion
    """gramA is dictonary"""         
    temp = gramA[A]
    tempCr = []
    tempInCr = []
    for i in temp:
        if i[0] == A:    #if the first character is A in the production
            tempInCr.append(i[1:]+[A+"'"])  # A'-> αA|ep we are appending various αAs to the list (alpha could be anything)
        else:
            tempCr.append(i+[A+"'"])
    tempInCr.append(["e"]) # adding epsilon to the list coz A'-> αA|ep
    gramA[A] = tempCr 
    gramA[A+"'"] = tempInCr
    return gramA   #returning the production


def checkForIndirect(gramA, a, ai): # This function is used to check for indirect left recursions:
    if ai not in gramA:
        return False 
    if a == ai:
        return True
    for i in gramA[ai]:
        if i[0] == ai:
            return False
        if i[0] in gramA:
            return checkForIndirect(gramA, a, i[0])
        return False

def rep(gramA, A):
    temp = gramA[A]
    newTemp = []
    for i in temp:
        if checkForIndirect(gramA, A, i[0]):
            t = []
            for k in gramA[i[0]]:
                t=[]
                t+=k
                t+=i[1:]
                newTemp.append(t)

        else:
            newTemp.append(i)
            gramA[A] = newTemp
            return gramA

def rem(gram):
    c = 1
    conv = {}
    gramA = {}
    revconv = {}
    for j in gram:
        conv[j] = "A"+str(c) #j is the key and value 'A1'
        gramA["A"+str(c)] = []#'A1' is a key and [](an empty arr) is value
        c+=1 

    for i in gram:
        for j in gram[i]: #{('A','Ab')}
            temp = []
            for k in j:
                if k in conv:
                    temp.append(conv[k])
                else:
                    temp.append(k)
            gramA[conv[i]].append(temp)


    #print(gramA)
    for i in range(c-1,0,-1):
        ai = "A"+str(i)
        for j in range(0,i):
            aj = gramA[ai][0][0]
            if ai!=aj :
                if aj in gramA and checkForIndirect(gramA,ai,aj):
                    gramA = rep(gramA, ai)

    for i in range(1,c):
        ai = "A"+str(i)
        for j in gramA[ai]:
            if ai==j[0]:
                gramA = removeDirectLR(gramA, ai)
                break

    op = {}
    for i in gramA:
        a = str(i)
        for j in conv:
            a = a.replace(conv[j],j)
            revconv[i] = a

    for i in gramA:
        l = []
        for j in gramA[i]:
            k = []
            for m in j:
                if m in revconv:
                    k.append(m.replace(m,revconv[m]))
                else:
                    k.append(m)
            l.append(k)
        op[revconv[i]] = l

    return op

n = int(input("Enter No of Production: "))
for i in range(n):
    txt=input()
    add(txt)
   
result = rem(gram) #gram from add function

for x,y in result.items():
    print(f'{x} -> {y}')


# In[4]:


#LEFT RECURSION

def func(n):
    s= input("Enter the grammar:")
    if s[0]!=s[3]:
        print("No left recursion")
    if s[0]==s[3]:
        
        l=len(s)
        alpha=''
        beta=''
        b=s[0]+"'"
    
        for i in range(l):
            if s[i]=="|":
                alpha=alpha+s[i+1:]
        for i in range(l):
            if s[i]=="|":
                beta=beta+s[4:i]
        alpha=alpha+b
        beta=beta+b
        print("_________")
        print(s[0],"->",alpha)
        print(b,"->",beta,"| epsilon\n")

n=int(input("Enter number of transitions: \n"))
for i in range(n):
    func(i)


# In[1]:


#LEFT FACTORING
#Pragya Bharti RA1911030010063
def leftFactoring(s): 
    k=[]
    l=[]
    n=""
    k=s.split('->')
    l=k[1].split('|') 
    for i in range(0,len(l)-1):
        for j in range(0,min(len(l[i]),len(l[i+1]))): 
            if(l[i][j]==l[i+1][j]):
                if l[i][j] not in n:
                    n=n+l[i][j]
    print(k[0]+'->'+n+"R")
    m=k[1].split(n)
    print("R->",end="")
    for i in range(1,len(m)):
       print(m[i],end="")
    
s=input("Enter the production: ") #main function
while(True):
    leftFactoring(s)
    print("\ndo you have another production?")
    T=input("y/n:")
    if T=='y':
        s=input("Enter the production: ")
    elif T=='n':
        break


# In[ ]:


#EXPERIMENT 4.1 Removing left recursion
#Pragya Bharti RA1911030010063
gram = {}

def add(str):                              
    x = str.split("->") #splitting the input string with -> as a separator
    y = x[1] #storing the first character of the list x in y
    x.pop() #returns the last value of the list 
    z = y.split("|") #splits the rhs with | as a separator
    x.append(z) #makes a list of all the characters ex: ['A','Ab',B]
    gram[x[0]]=x[1]#gram[A]='Ab'

def removeDirectLR(gramA, A):        # This function is used to remove the direct left recursion
    """gramA is dictonary"""         
    temp = gramA[A]
    tempCr = []
    tempInCr = []
    for i in temp:
        if i[0] == A:
            #tempInCr.append(i[1:])
            tempInCr.append(i[1:]+[A+"'"])  #
        else:
            #tempCr.append(i)
            tempCr.append(i+[A+"'"])
    tempInCr.append(["e"])
    gramA[A] = tempCr
    gramA[A+"'"] = tempInCr
    return gramA


def checkForIndirect(gramA, a, ai):
    if ai not in gramA:
        return False 
    if a == ai:
        return True
    for i in gramA[ai]:
        if i[0] == ai:
            return False
        if i[0] in gramA:
            return checkForIndirect(gramA, a, i[0])
        return False

def rep(gramA, A):
    temp = gramA[A]
    newTemp = []
    for i in temp:
        if checkForIndirect(gramA, A, i[0]):
            t = []
            for k in gramA[i[0]]:
                t=[]
                t+=k
                t+=i[1:]
                newTemp.append(t)

        else:
            newTemp.append(i)
            gramA[A] = newTemp
            return gramA

def rem(gram):
    c = 1
    conv = {}
    gramA = {}
    revconv = {}
    for j in gram:
        conv[j] = "A"+str(c)
        gramA["A"+str(c)] = []
        c+=1

    for i in gram:
        for j in gram[i]:
            temp = []
            for k in j:
                if k in conv:
                    temp.append(conv[k])
                else:
                    temp.append(k)
            gramA[conv[i]].append(temp)


    #print(gramA)
    for i in range(c-1,0,-1):
        ai = "A"+str(i)
        for j in range(0,i):
            aj = gramA[ai][0][0]
            if ai!=aj :
                if aj in gramA and checkForIndirect(gramA,ai,aj):
                    gramA = rep(gramA, ai)

    for i in range(1,c):
        ai = "A"+str(i)
        for j in gramA[ai]:
            if ai==j[0]:
                gramA = removeDirectLR(gramA, ai)
                break

    op = {}
    for i in gramA:
        a = str(i)
        for j in conv:
            a = a.replace(conv[j],j)
            revconv[i] = a

    for i in gramA:
        l = []
        for j in gramA[i]:
            k = []
            for m in j:
                if m in revconv:
                    k.append(m.replace(m,revconv[m]))
                else:
                    k.append(m)
            l.append(k)
        op[revconv[i]] = l

    return op

n = int(input("Enter No of Production: "))
for i in range(n):
    txt=input()
    add(txt)
   
result = rem(gram)

for x,y in result.items():
    print(f'{x} -> {y}')


# In[1]:


#EXPT 5
#Computation of first and follow
import sys
sys.setrecursionlimit(60)

def first(string):
    #print("first({})".format(string))
    first_ = set() #convert any of the iterable to sequence of iterable elements with distinct elements
    if string in non_terminals:
        alternatives = productions_dict[string]

        for alternative in alternatives:
            first_2 = first(alternative)
            first_ = first_ |first_2

    elif string in terminals:
        first_ = {string}

    elif string=='' or string=='@':
        first_ = {'@'}

    else:
        first_2 = first(string[0])
        if '@' in first_2:
            i = 1
            while '@' in first_2:
                #print("inside while")

                first_ = first_ | (first_2 - {'@'})
                #print('string[i:]=', string[i:])
                if string[i:] in terminals:
                    first_ = first_ | {string[i:]}
                    break
                elif string[i:] == '':
                    first_ = first_ | {'@'}
                    break
                first_2 = first(string[i:])
                first_ = first_ | first_2 - {'@'}
                i += 1
        else:
            first_ = first_ | first_2


    #print("returning for first({})".format(string),first_)
    return  first_


def follow(nT):
    #print("inside follow({})".format(nT))
    follow_ = set()
    #print("FOLLOW", FOLLOW)
    prods = productions_dict.items()
    if nT==starting_symbol:
        follow_ = follow_ | {'$'}
    for nt,rhs in prods:
        #print("nt to rhs", nt,rhs)
        for alt in rhs:
            for char in alt:
                if char==nT:
                    following_str = alt[alt.index(char) + 1:]
                    if following_str=='':
                        if nt==nT:
                            continue
                        else:
                            follow_ = follow_ | follow(nt)
                    else:
                        follow_2 = first(following_str)
                        if '@' in follow_2:
                            follow_ = follow_ | follow_2-{'@'}
                            follow_ = follow_ | follow(nt)
                        else:
                            follow_ = follow_ | follow_2
    #print("returning for follow({})".format(nT),follow_)
    return follow_





no_of_terminals=int(input("Enter no. of terminals: "))

terminals = []

print("Enter the terminals :")
for _ in range(no_of_terminals):
    terminals.append(input())

no_of_non_terminals=int(input("Enter no. of non terminals: "))

non_terminals = []

print("Enter the non terminals :")
for _ in range(no_of_non_terminals):
    non_terminals.append(input())

starting_symbol = input("Enter the starting symbol: ")

no_of_productions = int(input("Enter no of productions: "))

productions = []

print("Enter the productions:")
for _ in range(no_of_productions):
    productions.append(input())


#print("terminals", terminals)

#print("non terminals", non_terminals)

#print("productions",productions)


productions_dict = {}

for nT in non_terminals:
    productions_dict[nT] = []


#print("productions_dict",productions_dict)

for production in productions:
    nonterm_to_prod = production.split("->")
    alternatives = nonterm_to_prod[1].split("/")
    for alternative in alternatives:
        productions_dict[nonterm_to_prod[0]].append(alternative)

#print("productions_dict",productions_dict)

#print("nonterm_to_prod",nonterm_to_prod)
#print("alternatives",alternatives)


FIRST = {}
FOLLOW = {}

for non_terminal in non_terminals:
    FIRST[non_terminal] = set()

for non_terminal in non_terminals:
    FOLLOW[non_terminal] = set()

#print("FIRST",FIRST)

for non_terminal in non_terminals:
    FIRST[non_terminal] = FIRST[non_terminal] | first(non_terminal)

#print("FIRST",FIRST)


FOLLOW[starting_symbol] = FOLLOW[starting_symbol] | {'$'}
for non_terminal in non_terminals:
    FOLLOW[non_terminal] = FOLLOW[non_terminal] | follow(non_terminal)

#print("FOLLOW", FOLLOW)

print("{: ^20}{: ^20}{: ^20}".format('Non Terminals','First','Follow'))
for non_terminal in non_terminals:
    print("{: ^20}{: ^20}{: ^20}".format(non_terminal,str(FIRST[non_terminal]),str(FOLLOW[non_terminal])))


# In[1]:


# Ex 6
# Generating predictive parse table

def removeLeftRecursion(rulesDiction):
    store = {}
    # traverse over rules
    for lhs in rulesDiction:
        alphaRules = []
        betaRules = []
        allrhs = rulesDiction[lhs]
        for subrhs in allrhs:
            if subrhs[0] == lhs:
                alphaRules.append(subrhs[1:])
            else:
                betaRules.append(subrhs)
        if len(alphaRules) != 0:
            lhs_ = lhs + "'"
            while (lhs_ in rulesDiction.keys())                     or (lhs_ in store.keys()):
                lhs_ += "'"
            # make beata rule
            for b in range(0, len(betaRules)):
                betaRules[b].append(lhs_)
            rulesDiction[lhs] = betaRules
            # make alpha rule
            for a in range(0, len(alphaRules)):
                alphaRules[a].append(lhs_)
            alphaRules.append(['#'])

            store[lhs_] = alphaRules

    for left in store:
        rulesDiction[left] = store[left]
    return rulesDiction


def LeftFactoring(rulesDiction):
    newDict = {}
    # iterate over all rules of dictionary
    for lhs in rulesDiction:
        # get rhs for given lhs
        allrhs = rulesDiction[lhs]
        # temp dictionary hslps detect left factoring
        temp = dict()
        for subrhs in allrhs:
            if subrhs[0] not in list(temp.keys()):
                temp[subrhs[0]] = [subrhs]
            else:
                temp[subrhs[0]].append(subrhs)
        new_rule = []
        # temp_dict stores new subrules for left factoring
        tempo_dict = {}
        for term_key in temp:
            # get value from temp for term_key
            allStartingWithTermKey = temp[term_key]
            if len(allStartingWithTermKey) > 1:
                lhs_ = lhs + "'"
                while (lhs_ in rulesDiction.keys())                         or (lhs_ in tempo_dict.keys()):
                    lhs_ += "'"
                # append the left factored result
                new_rule.append([term_key, lhs_])
                # add expanded rules to tempo_dict
                ex_rules = []
                for g in temp[term_key]:
                    ex_rules.append(g[1:])
                tempo_dict[lhs_] = ex_rules
            else:
                # no left factoring required
                new_rule.append(allStartingWithTermKey[0])
        # add original rule
        newDict[lhs] = new_rule
        # add newly generated rules after left factoring
        for key in tempo_dict:
            newDict[key] = tempo_dict[key]
    return newDict


# calculation of first

def first(rule):
    global rules, nonterm_userdef,         term_userdef, diction, firsts
    if len(rule) != 0 and (rule is not None):
        if rule[0] in term_userdef:
            return rule[0]
        elif rule[0] == '#':
            return '#'

    # condition for Non-Terminals
    if len(rule) != 0:
        if rule[0] in list(diction.keys()):
            # fres temporary list of result
            fres = []
            rhs_rules = diction[rule[0]]
            # call first on each rule of RHS
            for itr in rhs_rules:
                indivRes = first(itr)
                if type(indivRes) is list:
                    for i in indivRes:
                        fres.append(i)
                else:
                    fres.append(indivRes)

            if '#' not in fres:
                return fres
            else:
                # apply epsilon
                newList = []
                fres.remove('#')
                if len(rule) > 1:
                    ansNew = first(rule[1:])
                    if ansNew != None:
                        if type(ansNew) is list:
                            newList = fres + ansNew
                        else:
                            newList = fres + [ansNew]
                    else:
                        newList = fres
                    return newList

                fres.append('#')
                return fres


# calcuation of follow
def follow(nt):
    global start_symbol, rules, nonterm_userdef,         term_userdef, diction, firsts, follows
    # for start symbol return $ (recursion base case)

    solset = set()
    if nt == start_symbol:
        # return '$'
        solset.add('$')
    for curNT in diction:
        rhs = diction[curNT]
        # go for all productions of NT
        for subrule in rhs:
            if nt in subrule:
                while nt in subrule:
                    index_nt = subrule.index(nt)
                    subrule = subrule[index_nt + 1:]
                    # empty condition - call follow on LHS
                    if len(subrule) != 0:
                        res = first(subrule)

                        if '#' in res:
                            newList = []
                            res.remove('#')
                            ansNew = follow(curNT)
                            if ansNew != None:
                                if type(ansNew) is list:
                                    newList = res + ansNew
                                else:
                                    newList = res + [ansNew]
                            else:
                                newList = res
                            res = newList
                    else:

                        if nt != curNT:
                            res = follow(curNT)

                    # add follow result in set form
                    if res is not None:
                        if type(res) is list:
                            for g in res:
                                solset.add(g)
                        else:
                            solset.add(res)
    return list(solset)


def computeAllFirsts():
    global rules, nonterm_userdef,         term_userdef, diction, firsts
    for rule in rules:
        k = rule.split("->")
        # remove un-necessary spaces
        k[0] = k[0].strip()
        k[1] = k[1].strip()
        rhs = k[1]
        multirhs = rhs.split('|')
        # remove un-necessary spaces
        for i in range(len(multirhs)):
            multirhs[i] = multirhs[i].strip()
            multirhs[i] = multirhs[i].split()
        diction[k[0]] = multirhs

    print(f"\nRules: \n")
    for y in diction:
        print(f"{y}->{diction[y]}")
    print(f"\nAfter elimination of left recursion:\n")

    diction = removeLeftRecursion(diction)
    for y in diction:
        print(f"{y}->{diction[y]}")
    print("\nAfter left factoring:\n")

    diction = LeftFactoring(diction)
    for y in diction:
        print(f"{y}->{diction[y]}")

    # calculate first for each rule
    for y in list(diction.keys()):
        t = set()
        for sub in diction.get(y):
            res = first(sub)
            if res != None:
                if type(res) is list:
                    for u in res:
                        t.add(u)
                else:
                    t.add(res)

        # save result in 'firsts' list
        firsts[y] = t

    print("\nCalculated firsts: ")
    key_list = list(firsts.keys())
    index = 0
    for gg in firsts:
        print(f"first({key_list[index]}) "
            f"=> {firsts.get(gg)}")
        index += 1


def computeAllFollows():
    global start_symbol, rules, nonterm_userdef,        term_userdef, diction, firsts, follows
    for NT in diction:
        solset = set()
        sol = follow(NT)
        if sol is not None:
            for g in sol:
                solset.add(g)
        follows[NT] = solset

    print("\nCalculated follows: ")
    key_list = list(follows.keys())
    index = 0
    for gg in follows:
        print(f"follow({key_list[index]})"
            f" => {follows[gg]}")
        index += 1


# create parse table
def createParseTable():
    import copy
    global diction, firsts, follows, term_userdef
    print("\nFirsts and Follow Result table\n")

    # find space size
    mx_len_first = 0
    mx_len_fol = 0
    for u in diction:
        k1 = len(str(firsts[u]))
        k2 = len(str(follows[u]))
        if k1 > mx_len_first:
            mx_len_first = k1
        if k2 > mx_len_fol:
            mx_len_fol = k2

    print(f"{{:<{10}}} "
        f"{{:<{mx_len_first + 5}}} "
        f"{{:<{mx_len_fol + 5}}}"
        .format("Non-T", "FIRST", "FOLLOW"))
    for u in diction:
        print(f"{{:<{10}}} "
            f"{{:<{mx_len_first + 5}}} "
            f"{{:<{mx_len_fol + 5}}}"
            .format(u, str(firsts[u]), str(follows[u])))

    # create matrix of row(NT) x [col(T) + 1($)]
    # create list of non-terminals
    ntlist = list(diction.keys())
    terminals = copy.deepcopy(term_userdef)
    terminals.append('$')

    # create the initial empty state of ,matrix
    mat = []
    for x in diction:
        row = []
        for y in terminals:
            row.append('')
        # of $ append one more col
        mat.append(row)

    # Classifying grammar as LL(1) or not LL(1)
    grammar_is_LL = True

    # rules implementation
    for lhs in diction:
        rhs = diction[lhs]
        for y in rhs:
            res = first(y)
            # epsion is present,
            # - take union with follow
            if '#' in res:
                if type(res) == str:
                    firstFollow = []
                    fol_op = follows[lhs]
                    if fol_op is str:
                        firstFollow.append(fol_op)
                    else:
                        for u in fol_op:
                            firstFollow.append(u)
                    res = firstFollow
                else:
                    res.remove('#')
                    res = list(res) +                        list(follows[lhs])
            # add rules to table
            ttemp = []
            if type(res) is str:
                ttemp.append(res)
                res = copy.deepcopy(ttemp)
            for c in res:
                xnt = ntlist.index(lhs)
                yt = terminals.index(c)
                if mat[xnt][yt] == '':
                    mat[xnt][yt] = mat[xnt][yt]                                 + f"{lhs}->{' '.join(y)}"
                else:
                    # if rule already present
                    if f"{lhs}->{y}" in mat[xnt][yt]:
                        continue
                    else:
                        grammar_is_LL = False
                        mat[xnt][yt] = mat[xnt][yt]                                     + f",{lhs}->{' '.join(y)}"

    # final state of parse table
    print("\nGenerated parsing table:\n")
    frmt = "{:>12}" * len(terminals)
    print(frmt.format(*terminals))

    j = 0
    for y in mat:
        frmt1 = "{:>12}" * len(y)
        print(f"{ntlist[j]} {frmt1.format(*y)}")
        j += 1

    return (mat, grammar_is_LL, terminals)


def validateStringUsingStackBuffer(parsing_table, grammarll1,
                                table_term_list, input_string,
                                term_userdef,start_symbol):

    print(f"\nValidate String => {input_string}\n")


    if grammarll1 == False:
        return f"\nInput String = "             f"\"{input_string}\"\n"             f"Grammar is not LL(1)"

    # implementing stack buffer

    stack = [start_symbol, '$']
    buffer = []

    # reverse input string store in buffer
    input_string = input_string.split()
    input_string.reverse()
    buffer = ['$'] + input_string

    print("{:>20} {:>20} {:>20}".
        format("Buffer", "Stack","Action"))

    while True:
        # end loop if all symbols matched
        if stack == ['$'] and buffer == ['$']:
            print("{:>20} {:>20} {:>20}"
                .format(' '.join(buffer),
                        ' '.join(stack),
                        "Valid"))
            return "\nValid String!"
        elif stack[0] not in term_userdef:
            # take font of buffer (y) and tos (x)
            x = list(diction.keys()).index(stack[0])
            y = table_term_list.index(buffer[-1])
            if parsing_table[x][y] != '':
                # format table entry received
                entry = parsing_table[x][y]
                print("{:>20} {:>20} {:>25}".
                    format(' '.join(buffer),
                            ' '.join(stack),
                            f"T[{stack[0]}][{buffer[-1]}] = {entry}"))
                lhs_rhs = entry.split("->")
                lhs_rhs[1] = lhs_rhs[1].replace('#', '').strip()
                entryrhs = lhs_rhs[1].split()
                stack = entryrhs + stack[1:]
            else:
                return f"\nInvalid String! No rule at "                     f"Table[{stack[0]}][{buffer[-1]}]."
        else:
            # stack top is Terminal
            if stack[0] == buffer[-1]:
                print("{:>20} {:>20} {:>20}"
                    .format(' '.join(buffer),
                            ' '.join(stack),
                            f"Matched:{stack[0]}"))
                buffer = buffer[:-1]
                stack = stack[1:]
            else:
                return "\nInvalid String! "                     "Unmatched terminal symbols"


# DRIVER CODE - MAIN

sample_input_string = None

rules=[]
n = int(input("Enter number of rules : "))

# iterating till the range
for i in range(0, n):
    ele = str(input())

    rules.append(ele) # adding the element


# nonterm_userdef=['A','B','C']
nonterm_userdef=[]
nu = int(input("Enter number of non terminals : "))

# iterating till the range
for i in range(0, nu):
    ele = str(input())

    nonterm_userdef.append(ele) # adding the element
# term_userdef=['k','O','d','a','c','b','r']
term_userdef=[]
tu = int(input("Enter number of terminals : "))

# iterating till the range
for i in range(0, tu):
    ele = str(input())

    term_userdef.append(ele) # adding the element
# sample_input_string="a r k O"
sample_input_string = str(input("Enter the sample string"))

# diction - store rules inputed
# firsts - store computed firsts
diction = {}
firsts = {}
follows = {}

# computes all FIRSTs for all non terminals
computeAllFirsts()
start_symbol = list(diction.keys())[0]
# computes all FOLLOWs for all occurences
computeAllFollows()
# generate formatted first and follow table then generate parse table

(parsing_table, result, tabTerm) = createParseTable()

# validate string input using stack-buffer concept
if sample_input_string != None:
    validity = validateStringUsingStackBuffer(parsing_table, result,
                                            tabTerm, sample_input_string,
                                            term_userdef,start_symbol)
    print(validity)
else:
    print("\nNo input String detected")


# In[1]:


#Expt 7 Shift reduce parsing
#PRAGYA BHARTI RA1911030010063
grammer={}
var= [k for k in input("Enter The Variable in Grammer:").split(" ")]
ter =[k for k in input("Enter The Terminal in Grammer:").split(" ")]
for v in var:
    grammer[v]=[k for k in input("Enter the production of "+v+"  Separated by space:").split(" ")]

inpbuff=input("Enter The String to pass:")
inpbuff=inpbuff
inp2=inpbuff
stack=''
print("=====================================================")
print("STACK\t\tINPUT\t\tACTION")
print("=====================================================")
reduced=0
for i in inpbuff:
    reduced=1
    while(reduced==1):
        for v in var:
            for prod in grammer[v]:
                if prod in stack:
                    if prod[-1]==stack[-1]:
                        stack=stack.replace(prod,v)
                        print(stack,"\t\t",inp2,"\t\tReduced!!")
                        reduced=1
                else:
                    reduced=0
    stack+=i
    inp2=inp2[1:len(inp2)]
    print(stack,"\t\t",inp2,"\t\tShifted!!")
reduced=1
while(reduced==1):
    for v in var:
        for prod in grammer[v]:
            if prod in stack:
                if prod[-1]==stack[-1]:
                    stack=stack.replace(prod,v)
                    print(stack,"\t\t",inp2,"\t\tReduced!!")
                    reduced=1
            else:
                reduced=0
print("=====================================================")
if(len(inp2)==0 and len(stack)==1 and stack[0]==var[0]):
    print("STRING PARSED SUCCESSFULLY!!")
else:
    print("STRING NOT PARSED!!!")
print("\n"*3)


# In[1]:


#EXPT 8 Leading Trailing
a = ["E=E+T",
     "E=T",
     "T=T*F",
     "T=F",
     "F=(E)",
     "F=i"]
rules = {} # dictionary for storing rules
terms = [] #array for terms
for i in a:
    temp = i.split("=")
 
    terms.append(temp[0])
    try:
        rules[temp[0]] += [temp[1]]
    except:
        rules[temp[0]] = [temp[1]]
terms = list(set(terms))
print(rules,terms)

def leading(gram, rules, term, start):
    s = []
    if gram[0] not in terms:
        return gram[0]
    elif len(gram) == 1:
        return [0]
    elif gram[1] not in terms and gram[-1] is not start:
        for i in rules[gram[-1]]:
            s+= leading(i, rules, gram[-1], start)
            s+= [gram[1]]
            return s

def trailing(gram, rules, term, start):
    s = []
    if gram[-1] not in terms:
        return gram[-1]
    elif len(gram) == 1:
        return [0]
    elif gram[-2] not in terms and gram[-1] is not start:
        for i in rules[gram[-1]]:
            s+= trailing(i, rules, gram[-1], start)
            s+= [gram[-2]]
 
        return s
leads = {}
trails = {}
for i in terms:
    s = [0]
    for j in rules[i]:
        s+=leading(j,rules,i,i)
    s = set(s)
    s.remove(0)
    leads[i] = s
    s = [0]
    for j in rules[i]:
        s+=trailing(j,rules,i,i)
    s = set(s)
    s.remove(0)
    trails[i] = s
for i in terms:
    print("LEADING("+i+"):",leads[i])
for i in terms:
    print("TRAILING("+i+"):",trails[i])


# In[2]:


#Expt 9 LR(0)
#Pragya Bharti RA1911030010063
gram = {
    "S":["CC"],
    "C":["aC","d"]
}
start = "S"
terms = ["a","d","$"]

non_terms = []
for i in gram:
    non_terms.append(i)
gram["S'"]= [start]


new_row = {}
for i in terms+non_terms:
    new_row[i]=""


non_terms += ["S'"]
# each row in state table will be dictionary {nonterms ,term,$}
stateTable = []
# I = [(terminal, closure)]
# I = [("S","A.A")]

def Closure(term, I):
    if term in non_terms:
        for i in gram[term]:
            I+=[(term,"."+i)]
    I = list(set(I))
    for i in I:
        # print("." != i[1][-1],i[1][i[1].index(".")+1])
        if "." != i[1][-1] and i[1][i[1].index(".")+1] in non_terms and i[1][i[1].index(".")+1] != term:
            I += Closure(i[1][i[1].index(".")+1], [])
    return I

Is = []
Is+=set(Closure("S'", []))


countI = 0
omegaList = [set(Is)]
while countI<len(omegaList):
    newrow = dict(new_row)
    vars_in_I = []
    Is = omegaList[countI]
    countI+=1
    for i in Is:
        if i[1][-1]!=".":
            indx = i[1].index(".")
            vars_in_I+=[i[1][indx+1]]
    vars_in_I = list(set(vars_in_I))
    # print(vars_in_I)
    for i in vars_in_I:
        In = []
        for j in Is:
            if "."+i in j[1]:
                rep = j[1].replace("."+i,i+".")
                In+=[(j[0],rep)]
        if (In[0][1][-1]!="."):
            temp = set(Closure(i,In))
            if temp not in omegaList:
                omegaList.append(temp)
            if i in non_terms:
                newrow[i] = str(omegaList.index(temp))
            else:
                newrow[i] = "s"+str(omegaList.index(temp))
            print(f'Goto(I{countI-1},{i}):{temp} That is I{omegaList.index(temp)}')
        else:
            temp = set(In)
            if temp not in omegaList:
                omegaList.append(temp)
            if i in non_terms:
                newrow[i] = str(omegaList.index(temp))
            else:
                newrow[i] = "s"+str(omegaList.index(temp))
            print(f'Goto(I{countI-1},{i}):{temp} That is I{omegaList.index(temp)}')

    stateTable.append(newrow)
print("\n\nList of I's\n")
for i in omegaList:
    print(f'I{omegaList.index(i)}: {i}')


#populate replace elements in state Table
I0 = []
for i in list(omegaList[0]):
    I0 += [i[1].replace(".","")]
print(I0)

for i in omegaList:
    for j in i:
        if "." in j[1][-1]:
            if j[1][-2]=="S":
                stateTable[omegaList.index(i)]["$"] = "Accept"
                break
            for k in terms:
                stateTable[omegaList.index(i)][k] = "r"+str(I0.index(j[1].replace(".","")))
print("\nStateTable")

print(f'{" ": <9}',end="")
for i in new_row:
    print(f'|{i: <11}',end="")

print(f'\n{"-":-<66}')
for i in stateTable:
    print(f'{"I("+str(stateTable.index(i))+")": <9}',end="")
    for j in i:
        print(f'|{i[j]: <10}',end=" ")
    print()


# In[5]:


#EXPT 10 prefix to postfix/prefix to infix/ three address code generation
#RA1911030010063 Pragya Bharti
OPERATORS = set(['+', '-', '*', '/', '(', ')'])
PRI = {'+':1, '-':1, '*':2, '/':2}

### INFIX ===> POSTFIX ###
def infix_to_postfix(formula):
    stack = [] # only pop when the coming op has priority 
    output = ''
    for ch in formula:
        if ch not in OPERATORS:
            output += ch
        elif ch == '(':
            stack.append('(')
        elif ch == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop() # pop '('
        else:
            while stack and stack[-1] != '(' and PRI[ch] <= PRI[stack[-1]]:
                output += stack.pop()
            stack.append(ch)
    # leftover
    while stack: 
        output += stack.pop()
    print(f'POSTFIX: {output}')
    return output

### INFIX ===> PREFIX ###
def infix_to_prefix(formula):
    op_stack = []
    exp_stack = []
    for ch in formula:
        if not ch in OPERATORS:
            exp_stack.append(ch)
        elif ch == '(':
            op_stack.append(ch)
        elif ch == ')':
            while op_stack[-1] != '(':
                op = op_stack.pop()
                a = exp_stack.pop()
                b = exp_stack.pop()
                exp_stack.append( op+b+a )
            op_stack.pop() # pop '('
        else:
            while op_stack and op_stack[-1] != '(' and PRI[ch] <= PRI[op_stack[-1]]:
                op = op_stack.pop()
                a = exp_stack.pop()
                b = exp_stack.pop()
                exp_stack.append( op+b+a )
            op_stack.append(ch)

    # leftover
    while op_stack:
        op = op_stack.pop()
        a = exp_stack.pop()
        b = exp_stack.pop()
        exp_stack.append( op+b+a )
    print(f'PREFIX: {exp_stack[-1]}')
    return exp_stack[-1]

### THREE ADDRESS CODE GENERATION ###
def generate3AC(pos):
    print("### THREE ADDRESS CODE GENERATION ###")
    exp_stack = []
    t = 1

    for i in pos:
        if i not in OPERATORS:
            exp_stack.append(i)
        else:
            print(f't{t} := {exp_stack[-2]} {i} {exp_stack[-1]}')
            exp_stack=exp_stack[:-2]
            exp_stack.append(f't{t}')
            t+=1

expres = input("INPUT THE EXPRESSION: ")
pre = infix_to_prefix(expres)
pos = infix_to_postfix(expres)
generate3AC(pos)


# In[6]:


# Expt 11 Intermediate code generation quadruple and triple
OPERATORS = set(['+', '-', '*', '/', '(', ')'])
PRI = {'+':1, '-':1, '*':2, '/':2}

### INFIX ===> POSTFIX ###
def infix_to_postfix(formula):
    stack = [] # only pop when the coming op has priority 
    output = ''
    for ch in formula:
        if ch not in OPERATORS:
            output += ch
        elif ch == '(':
            stack.append('(')
        elif ch == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop() # pop '('
        else:
            while stack and stack[-1] != '(' and PRI[ch] <= PRI[stack[-1]]:
                output += stack.pop()
            stack.append(ch)
    # leftover
    while stack: 
        output += stack.pop()
    print(f'POSTFIX: {output}')
    return output

### INFIX ===> PREFIX ###
def infix_to_prefix(formula):
    op_stack = []
    exp_stack = []
    for ch in formula:
        if not ch in OPERATORS:
            exp_stack.append(ch)
        elif ch == '(':
            op_stack.append(ch)
        elif ch == ')':
            while op_stack[-1] != '(':
                op = op_stack.pop()
                a = exp_stack.pop()
                b = exp_stack.pop()
                exp_stack.append( op+b+a )
            op_stack.pop() # pop '('
        else:
            while op_stack and op_stack[-1] != '(' and PRI[ch] <= PRI[op_stack[-1]]:
                op = op_stack.pop()
                a = exp_stack.pop()
                b = exp_stack.pop()
                exp_stack.append( op+b+a )
            op_stack.append(ch)

    # leftover
    while op_stack:
        op = op_stack.pop()
        a = exp_stack.pop()
        b = exp_stack.pop()
        exp_stack.append( op+b+a )
    print(f'PREFIX: {exp_stack[-1]}')
    return exp_stack[-1]

### THREE ADDRESS CODE GENERATION ###
def generate3AC(pos):
    print("### THREE ADDRESS CODE GENERATION ###")
    exp_stack = []
    t = 1

    for i in pos:
        if i not in OPERATORS:
            exp_stack.append(i)
        else:
            print(f't{t} := {exp_stack[-2]} {i} {exp_stack[-1]}')
            exp_stack=exp_stack[:-2]
            exp_stack.append(f't{t}')
            t+=1

expres = input("INPUT THE EXPRESSION: ")
pre = infix_to_prefix(expres)
pos = infix_to_postfix(expres)
generate3AC(pos)
def Quadruple(pos):
  stack = []
  op = []
  x = 1
  for i in pos:
    if i not in OPERATORS:
       stack.append(i)
    elif i == '-':
        op1 = stack.pop()
        stack.append("t(%s)" %x)
        print("{0:^4s} | {1:^4s} | {2:^4s}|{3:4s}".format(i,op1,"(-)"," t(%s)" %x))
        x = x+1
        if stack != []:
          op2 = stack.pop()
          op1 = stack.pop()
          print("{0:^4s} | {1:^4s} | {2:^4s}|{3:4s}".format("+",op1,op2," t(%s)" %x))
          stack.append("t(%s)" %x)
          x = x+1
    elif i == '=':
      op2 = stack.pop()
      op1 = stack.pop()
      print("{0:^4s} | {1:^4s} | {2:^4s}|{3:4s}".format(i,op2,"(-)",op1))
    else:
      op1 = stack.pop()
      op2 = stack.pop()
      print("{0:^4s} | {1:^4s} | {2:^4s}|{3:4s}".format(i,op2,op1," t(%s)" %x))
      stack.append("t(%s)" %x)
      x = x+1
print("The quadruple for the expression ")
print(" OP | ARG 1 |ARG 2 |RESULT  ")
Quadruple(pos)

def Triple(pos):
        stack = []
        op = []
        x = 0
        for i in pos:
          if i not in OPERATORS:
            stack.append(i)
          elif i == '-':
            op1 = stack.pop()
            stack.append("(%s)" %x)
            print("{0:^4s} | {1:^4s} | {2:^4s}".format(i,op1,"(-)"))
            x = x+1
            if stack != []:
              op2 = stack.pop()
              op1 = stack.pop()
              print("{0:^4s} | {1:^4s} | {2:^4s}".format("+",op1,op2))
              stack.append("(%s)" %x)
              x = x+1
          elif i == '=':
            op2 = stack.pop()
            op1 = stack.pop()
            print("{0:^4s} | {1:^4s} | {2:^4s}".format(i,op1,op2))
          else:
            op1 = stack.pop()
            if stack != []:           
              op2 = stack.pop()
              print("{0:^4s} | {1:^4s} | {2:^4s}".format(i,op2,op1))
              stack.append("(%s)" %x)
              x = x+1
print("The triple for given expression")
print("  OP | ARG 1 |ARG 2  ")
Triple(pos)


# In[ ]:
