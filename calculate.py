
def calculate(days):
    if days < 15:
        return 0
    elif days < 30:
        return days*50
    elif days < 60:
        return days*80
    else:
        return days*100
    
    
