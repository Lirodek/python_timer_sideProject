def solution(today, terms, privacies):
    answer = []
    term={}
    ty, tm, td = today.split('.')
    ty,tm,td = int(ty),int(tm),int(td)
    for i in terms:
        t = i.split()
        term[t[0]] = t[1]
    
    for j,i in enumerate(privacies):
        t = i.split()
        period = int(term[t[1]])
        py = int(period / 12)
        pm = period % 12 
        yy,mm,dd = t[0].split(".")
        yy = int(yy) + py
        mm = int(mm) + pm
        dd = int(dd)
        if mm > 12:
            yy += 1
            mm -= 12
            
        if j == 2:
            print(ty,tm,td)
            print(yy,mm,dd)
            
        if ty > yy: 
            answer.append(j+1)
        elif ty==yy and tm > mm: 
            answer.append(j+1)
        elif ty==yy and tm == mm and td >= dd:
            answer.append(j+1)
            
    return answer