import data_puller_and_processor
dpp=data_puller_and_processor
txtFile=open("src/CharNamesList.txt","r")
charList=txtFile.readlines()

##FIX BUG FOUND HERE
def run_request(tokens):
    print(len(tokens))
    site = ""
    potential_name = ""
    char_found=False
    if tokens[0].lower()=="?doc":
        if tokens[1].lower()=="show" or tokens[1].lower()=="stats":
            name_index=1
            while name_index <len(tokens) and char_found == False:
                name_index+=1
                print(name_index)
                potential_name+=tokens[name_index]+" "
                for char_name in charList:
                    split_line=char_name.split(";")
                    name_set=split_line[0].split(",")
                    for name_set_element in name_set:
                        if str(name_set_element).strip().lower() == str(potential_name).strip().lower():
                            char_found = True
                            site = split_line[1]
                            break
                    if char_found == True:
                        break

            #Fix this part
            move_index = name_index + 1
            move=""
            while move_index < len(tokens):
                move+=tokens[move_index]+" "
                move_index+=1

            test = dpp.isolate_req_move_post_data(dpp.get_all_moves(site),move.strip())
            if test == False:
                return "This move is not found kiddo sorry"
            if test != False:
                return test