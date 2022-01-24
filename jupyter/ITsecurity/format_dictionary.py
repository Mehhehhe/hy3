def format_dictionary(value_dict,more_indent="default"):
    payload = ""    #   Using string concatenate
    payload += "{\n" if(more_indent == "default") else " {\n" # Add '{' to blank string [option: default], Add '{' with space to blank string [option: any]
    
    for i in value_dict:    #   Looping thorugh keys in dictionary
        
        if (type(i) is str):    # Check if current key is string or not.
            
            if (type(value_dict.get(i)) is not dict):   # Check if value at current key is dictionary or not.
                
                if (type(value_dict.get(i)) is str):    # Check if value at current key is string or not.
                    #   Add current key and its value to string [option: default], Add with more tab [option: any]
                    payload += '\t\"'+str(i)+'\"'+": \""+str(value_dict.get(i))+"\",\n" if (more_indent == "default") else '\t\t\"'+str(i)+'\"'+": \""+str(value_dict.get(i))+"\",\n" 
                
                else:   # Current key's value is not string
                    payload += '\t\"'+str(i)+'\"'+": "+value_dict.get(i)+",\n" if (more_indent == "default") else '\t\t\"'+str(i)+'\"'+": "+value_dict.get(i)+",\n"
            
            else:   #   Current key's value is dictionary
                payload += '\t\"'+str(i)+'\"'+": "+format_dictionary(value_dict.get(i),"yes")
        
        else:   #   Current key is not string
            if (type(value_dict.get(i)) is not dict):
                if (type(value_dict.get(i)) is str):
                    payload += '\t\"'+i+'\"'+": \""+str(value_dict.get(i))+"\",\n" if (more_indent == "default") else '\t\t\"'+i+'\"'+": \""+str(value_dict.get(i))+"\",\n" 
                else:
                    payload += '\t\"'+i+'\"'+": "+value_dict.get(i)+",\n" if (more_indent == "default") else '\t\t\"'+i+'\"'+": "+value_dict.get(i)+",\n"
            else:
                payload += '\t\"'+i+'\"'+": "+format_dictionary(value_dict.get(i),"yes")
    
    #   Add '}' for closing string [option: default], with tab [option: any]
    payload += '}' if(more_indent == "default") else '\t},\n'
    return payload