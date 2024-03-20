new_name_list = []
def fund_names_morewords_five(list):
    #new_name_list=['Mouse','laptop']
    for name in name_list:
        if len(name)>=5:
          new_name_list.append(name)
    print(new_name_list)

name_list=['prasanna','saeen','butu','ranjita','gopi','rupa','soham','litu']
fund_names_morewords_five(name_list)