#this is from pythons standard library(built into the langauge) so I dont consider it an external lib
import itertools
#checks to see if the colors in dict_vertex is valid for the dict_G
def is_proper(dict_G, dict_vertex):
  for key in dict_G:
    #print(key, ':')
    list = dict_G[key]
    for value in list:
      #print(value)
      #conditional that checks to see if a invalid vertex coloring is present
      if(dict_vertex[key] == dict_vertex[value]):
        return False
  #Since the loop is finished and no colors have been invalid return true
  return True
#Creates the sequence to apply to the vertex list ie: 3 vertex with chrom 2 -> [1, 2, 1] 
def make_sequence(vertex_list, color_sequence):
  new_seq = []
  #Make new dictionary using number sequence
  number_value = 0
  for i in range(len(vertex_list)):
    #reset number if it exceeds list size
    if(number_value >= len(color_sequence)):
      #print('Color seq reset')
      number_value -= number_value
    #print('start i:', i)
    #make sequence for permutation_dictionary
    new_seq.append(color_sequence[number_value])
    #print('color: ', color_sequence[number_value])
    #else increment number_value
    if(number_value <= len(color_sequence)-1):
      number_value += 1
  return new_seq
#FIXME: implement scan for just one chromatic number
#FIXME: implement permutation from the sequence
def make_dictionary(vertex_list, perm_list):
  new_dict = {}
  perm_count = 0
  for v in range(len(vertex_list)):
    if(perm_count >= len(perm_list)):
      perm_count -= perm_count
    #print('vertex:', vertex_list[v])
    #print('perm_list:', perm_list[perm_count])

    new_dict.update({vertex_list[v] : perm_list[perm_count]})
    if(perm_count < len(perm_list)):
      perm_count += 1
  return new_dict
def greedy(dict_G, vertex_list):
  #Scan graph for highest degree
  if(len(dict_G) == 1 and len(vertex_list) == 1):
    easy = {vertex_list[0]: 1}
    return easy
  max_degree = 1
  chrom_degree = 1
  #find biggest degree
  for key in dict_G:
    list = dict_G[key]
    if(len(list) > max_degree):
      max_degree = len(list)
      max_key = key
  new_dict = {}
  #if chrom_degree = 1 do this,
  if(chrom_degree == 1):
    for vertex in vertex_list:
      new_dict.update({vertex: 1})
    if(is_proper(dict_G, new_dict)):
      return new_dict
    else:
      #print('incrementing chrom num')
      chrom_degree += 1
  #while loop if chrom_degree greater than 1
  while(chrom_degree <= max_degree + 1):
    #Create color_sequence
    color_sequence = []
    for num in range(chrom_degree):
      color_sequence.append(num+1)
      
    #call make_sequence()
    degree_seq = make_sequence(vertex_list, color_sequence)
    #Make list of all permutations using python's itertool functions
    perm_list = itertools.permutations(degree_seq, None)
    #iterate thru each sequence in list
    for seq in perm_list:
      #print(seq)
      temp_sequence = []
      for number in seq:
        #print(number)
        temp_sequence.append(number)
      #create dictionary from new temp sequence
      new_dict = make_dictionary(vertex_list, temp_sequence)
      #test dictionary if true break and return, else continue thru loop
      if(is_proper(dict_G, new_dict)):
        return new_dict
    #if not found in loop and isnt max_degree increment and try again
    #print('incrementing chrom to :', chrom_degree+1)
    chrom_degree += 1
    #DEBUG: print degree_seq
    #for yeet in range(len(degree_seq)):
    #  print('degree: ', degree_seq[yeet])
    #call permutation_list and use it for make_dictionary
    
  return "Error"
  
#~~~is_proper test cases~~~#
#example_G = {"A" : ["B", "C"], "B" : ["A", "C"], "C" : ["A", "B"]}
#example_V = {"A" : 1, "B" : 2, "C" : 3}
#example_V_wrong = {"A" : 1, "B" : 1, "C" : 3}
#print(is_proper(example_G, example_V))
#print(is_proper(example_G, example_V_wrong))
#
#oddcycle_G = {"A" : ["B", "E"], "B" : ["A", "C"], "C" : ["B", "D"], "D" : ["C", "E"], "E" : ["A", "D"]}
#oddcycle_V = {"A" : 1, "B" : 2, "C" : 1, "D" : 2, "E" : 3}
#oddcycle_V_wrong = {"A" : 1, "B" : 2, "C" : 1, "D" : 2, "E" : 1}
#print('oddcycle:',is_proper(oddcycle_G, oddcycle_V))
#print('oddcycle_wrong:',is_proper(oddcycle_G, oddcycle_V_wrong))
#
#evencycle_G = {"A" : ["B", "F"], "B" : ["A", "C"], "C" : ["B", "D"], "D" : ["C", "E"], "E" : ["D", "F"], "F": ["A", "E"]}
#evencycle_V = {"A" : 1, "B" : 2, "C" : 1, "D" : 2, "E" : 1, "F" : 2}
#print('evencycle:',is_proper(evencycle_G, evencycle_V))
#
#bipartite_G = {"A" : ["B",  "C", "D", "E"], "B" : "A", "C" : "A", "D" : "A", "E" : "A"}
#bipartite_V = {"A" : 1, "B" : 2, "C" : 2, "D" : 2, "E" : 2}
#print('bipartite:', is_proper(bipartite_G, bipartite_V))
#
#lonevertex_G = {"A" : ["C", "D", "B"], "B" : ["C", "A", "D"], "C" : ["A", "B"], "D" : ["A", "B"], "E": "", "F" : ""}
#lonevertex_V = {"A" : 1, "B" : 2, "C" : 3, "D" : 3, "E" : 1, "F" : 1}
#print('lonevertex:',is_proper(lonevertex_G, lonevertex_V))

#~~~greedy() test cases~~~#
#test_example: chrom = 2
#greedy_example_G = {"A" : ["B","C"],"B" : ["A"],"C" : ["A"]}
#greedy_example_V = ["A","B","C"]
#print(greedy(greedy_example_G, greedy_example_V))

#test_max_degree+1: Chrom = 3
#greedy_maxplusone_G = {"A" : ["B", "C"], "B" : ["A", "C"], "C" : ["A", "B"]}
#greedy_maxplusone_V = ["A", "B", "C"]
#print(greedy(greedy_maxplusone_G, greedy_maxplusone_V))

#test_oddcycle: Chrom = 3
#greed_oddcycle_G = {"A" : ["B", "E"], "B" : ["A", "C"], "C" : ["B", "D"], "D" : ["C", "E"], "E" : ["A", "D"]}
#greed_oddcycle_V = ["A", "B", "C", "D", "E"]
#print(greedy(greed_oddcycle_G,greed_oddcycle_V))

#degree_one_test: Chrom = 1
#greed_single_G = {"A"}
#greed_single_V = ["A"]
#print(greedy(greed_single_G,greed_single_V))

#bipartite_test: Chrom = 2
#greed_bipart_G = {"A" : ["B","F"], "B": ["A", "C"], "C": ["B", "D"], "D": ["C", "E"], "E": ["D","F"], "F":["A","E"]}
#greed_bipart_V = ["A", "B", "C", "D", "E","F"]
#print(greedy(greed_bipart_G,greed_bipart_V))

#lone_vertex's test: chrom = 3
#greed_lonevertex_G = {"A" : ["C", "D", "B"], "B" : ["C", "A", "D"], "C" : ["A", "B"], "D" : ["A", "B"], "E": "", "F" : ""}
#greed_lonevertex_V = ["A","B","C","D","E","F"]
#print(greedy(greed_lonevertex_G,greed_lonevertex_V))

#Complete graph of 5: chrom = 5
  #Oh lawd almighty
#greed_complete_G = {}
#greed_complete_V= ["A","B","C","D","E"]
#a = {"A": ["B", "C", "D", "E"]}
#b = {"B": ["A", "C", "D", "E"]}
#c = {"C": ["A", "B", "D", "E"]}
#d = {"D": ["A", "B", "C", "E"]}
#e = {"E": ["A","B", "C", "D"]}
#greed_complete_G.update(a)
#greed_complete_G.update(b)
#greed_complete_G.update(c)
#greed_complete_G.update(d)
#greed_complete_G.update(e)
#print(greedy(greed_complete_G,greed_complete_V))