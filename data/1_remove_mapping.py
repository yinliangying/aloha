# coding: utf-8

from __future__ import print_function
import os
import re
import json
import traceback
import sys
import pickle, gzip
from rdkit.Chem import AllChem
from rdkit import Chem
import copy
#import parser.Smipar as Smipar

def cano(smiles): # canonicalize smiles by MolToSmiles function
    return Chem.MolToSmiles(Chem.MolFromSmiles(smiles)) if (smiles != '') else ''


fp_train=open("train.txt")
fp_train_sample=open("train_sample","w")
fp_test=open("test.txt")
fp_test_sample=open("test_sample","w")
fp_test_id=open("test_id","w")
#fp_vocab=open("vocab","w")
#vocab= {}


#id,reactants>reagents>production
fp_train.readline()
for line in fp_train :
    if " |" in line:
        tmp_fields=line.strip().split(" |")
        line=tmp_fields[0]
    fields=line.strip().split(",")
    sample_id=fields[0]
    rxn_str=fields[1]
    try:
        rxn = AllChem.ReactionFromSmarts(rxn_str, useSmiles=True)
    except:
        print(rxn_str,file=sys.stderr)
        print(sample_id)
        traceback.print_exc()
        continue
    AllChem.RemoveMappingNumbersFromReactions(rxn)#去原子的号码
    output_smiles = AllChem.ReactionToSmiles(rxn)
    reactant,product_reagent=output_smiles.strip().split(">",1)
    out_dict={
          "inputs": "".join(list(product_reagent)),
          "targets": "".join(list(reactant)),
          "id":sample_id,
        }
    print(json.dumps(out_dict),file=fp_train_sample)

#id,reagents>production
fp_test.readline()
for line in fp_test:
    if " |" in line:
        tmp_fields = line.strip().split(" |")
        line = tmp_fields[0]
    fields = line.strip().split(",")
    sample_id = fields[0]
    rxn_str = fields[1]
    rxn_str="O>"+rxn_str
    try:
        rxn = AllChem.ReactionFromSmarts(rxn_str, useSmiles=True)
    except:
        print(rxn_str, file=sys.stderr)
        print(sample_id)
        traceback.print_exc()
        continue
    AllChem.RemoveMappingNumbersFromReactions(rxn)  # 去原子的号码
    output_smiles = AllChem.ReactionToSmiles(rxn)
    _, product_reagent = output_smiles.strip().split(">", 1)
    print("".join(list(product_reagent)), file=fp_test_sample)
    print(sample_id,file=fp_test_id)
    """
    reactant_list = []
    agent_list = []
    product_list = []
    split_rsmi = output_smiles.split('>')
    try:
        #reactants = cano(split_rsmi[0]).split('.')
        reactants = split_rsmi[0].split('.')
    except:
        print(split_rsmi[0])
        print(id)
        traceback.print_exc()
        continue
    try:
        #agents = cano(split_rsmi[1]).split('.')
        agents = split_rsmi[1].split('.')
    except:
        print(split_rsmi[1])
        print(id)
        traceback.print_exc()
        continue
    try:
        #products = cano(split_rsmi[2]).split('.')
        products = split_rsmi[2].split('.')
    except:
        print(split_rsmi[2])
        print(id)
        traceback.print_exc()
        continue 
    token_regex = "(\[[^\]]+]|Br?|Cl?|N|O|S|P|F|I|b|c|n|o|s|p|\(|\)|\.|= |  # |-|\+|\\\\|\/|:|~|@|\?|>|\*|\$|\%[0-9]{2}|[0-9])"
    for reactant in reactants:
        #print(re.split(token_regex, reactant))
        #reactant_list += Smipar.parser_list(reactant)
        reactant_list+=re.split(token_regex, reactant)
        reactant_list += '.'
    for agent in agents:
        #agent_list += Smipar.parser_list(agent)
        agent_list+=re.split(token_regex, agent)
        agent_list += '.'
    for product in products:
        #product_list += Smipar.parser_list(product)
        product_list+=re.split(token_regex, product)
        product_list += '.'
    reactant_list.pop()  # to pop last '.'
    agent_list.pop()
    product_list.pop()
    product_list += '>'
    product_list += agent_list
    out_product_list=[]
    out_reactant_list=[]
    for token in product_list:
        strip_token=token.strip()
        if strip_token!="":
            out_product_list.append(strip_token)
    for token in reactant_list:
        strip_token = token.strip()
        if strip_token != "":
            out_reactant_list.append(strip_token)
    print(" ".join(out_product_list),file=fp_train_sources)
    print(" ".join(out_reactant_list), file=fp_train_targets)
    for reactant_token in reactant_list:
        if reactant_token in vocab:
            vocab[reactant_token] += 1
        else:
            if reactant_token=="Cl":
                print("sdfsf")
            if reactant_token=="6":
                print("sdfsf")
            vocab[reactant_token] = 1
    for product_token in product_list:
        if product_token in vocab:
            vocab[product_token] += 1
        else:
            if product_token=="Cl":
                print("sdfsf")
            if product_token=="6":
                print("sdfsf")
            vocab[product_token] = 1
    """

#print("\n".join(list(vocab.keys())),file=fp_vocab)