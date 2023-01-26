def factorize(*number):
    list_num = []
    
    for el in number:
        new_el = el
        
        while new_el != 0:
            
            if el % new_el == 0:
                list_num.append(new_el)
                
            new_el = new_el - 1
            
        list_num.reverse()
        print(list_num)
        list_num = []  
         
    return        
                    
factorize(128, 255, 99999, 10651060)                     