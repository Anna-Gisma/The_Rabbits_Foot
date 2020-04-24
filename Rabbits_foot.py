def TheRabbitsFoot(s, encode):
    
    res = []
    new_res = []
    F = []
    ind = 0
    k = 0

    if encode:
        ss = ''.join(s.split())
        L = len(ss)
        sqr_ss = L**0.5
        if sqr_ss%1 > 0: # если корень не целое число
            l_b = int(sqr_ss//1) # нижняя граница
            h_b = l_b + 1  # верхняя граница
        else:
            l_b = h_b = sqr_ss 
        if h_b * l_b < L: # если длина строки больше, чем матрица
            l_b += 1
        for j in range(h_b): #разбиениепо матрице
            a = []
            x = l_b + ind
            if x > L:
                x = L
            for i in range(ind, x): 
                a.append(ss[i])
                ind = i + 1
            if len(a) < l_b:
                while len(a)< l_b:   #обавляем пробелы, если не хватило символов 
                    a.append(' ')
            res.append(a)

        for i in range(l_b): #переворачиваем строки в столбцы, убираем пробелы
            f = ''.join([f[i]for f in res if f[i]!= ' '])
            new_res.append(f)
        new_res_str = ' '.join(new_res)
    

    else:
        ss = ''.join(s.split())
        L = len(s)
        sqr_ss = L**0.5
        if sqr_ss%1 > 0: # если корень не целое число
            l_b = int(sqr_ss//1) # нижняя граница
            h_b = int(l_b + 1)  # верхняя граница
        else:
            h_b = l_b = int(sqr_ss)
        if h_b * l_b < L: # если длина строки больше, чем матрица
            h_b += 1
        list_s = list(s)
        for i in range(l_b):
            a = []
            x = h_b +k
            if x > L:
                x = L
            for j in range(k, x):
                if list_s[j] != ' ':
                    a.append(list_s[j])
                k = j + 1
            if len(a) < h_b:
                a.append(' ')
            res.append(a)
        for i in range(h_b): #переворачиваем строки в столбцы, убираем пробелы
            f = ''.join([f[i]for f in res if f[i]!= ' '])
            new_res.append(f)
        new_res_str = ''.join(new_res)
        
    return new_res_str
    
print(TheRabbitsFoot('шшосау ласос апссу соеаш ашилк', False))        
   
                
    
    

 
            
    
        
