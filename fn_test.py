from utils import *
import numpy as np
# a = np.array([[1,2,3,4],[1,'O','O','O'],[1,2,3,4],[1,2,2,'O']])
# print(len(a[0]))
# print(a)

# nset_li = [] #set of entities level i
# all_en  = [] #set of all en

# for i in range(len(a[0])):
#     set_li = a[:,[i]]
#     set_li = np.reshape(set_li,(len(set_li)))
    
#     index  = np.argwhere(set_li=='O')
#     set_li = np.delete(set_li, index)
    
#     all_en.extend(set(set_li))
#     nset_li.append(len(set(set_li)))
    
# print(nset_li)
# print(all_en)
# print(sum(nset_li))

#print(len(set(all_en)))
# assert sum(nset_li) == len(set(all_en)), '*** Entity Overlab ***'

def _test_overlapping(words_tags_nested_):
    sent_idx_en = []
    for s in words_tags_nested_:
        s = s[1].split('|')
        idx_ens = []
        for idx_en in s:
            idxe = idx_en.split('-')[0]
            
            if(idxe != 'O'):
                idx_ens.append(int(idxe))
            else:
                idx_ens.append('O')
#         print(idx_ens)
        sent_idx_en.append(idx_ens)
    
    
    
    sent_idx_en = np.array(sent_idx_en)
    nset_li = [] #set of entities level i
    all_en  = [] #set of all en

    for i in range(len(sent_idx_en[0])):
        set_li = sent_idx_en[:,[i]]
        set_li = np.reshape(set_li,(len(set_li)))
        
        index  = np.argwhere(set_li=='O')
        set_li = np.delete(set_li, index)
        
        all_en.extend(set_li)
        nset_li.append(len(set(set_li)))
    if( sum(nset_li) != len(set(all_en))):
#        assert sum(nset_li) == len(set(all_en)), '*** Entity Overlab ***'
#        print('Overlapping :',sum(nset_li),len(set(all_en)))
        return True
    else:
        return False
    
