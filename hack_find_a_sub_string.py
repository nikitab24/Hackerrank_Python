def count_substring(string, sub_string):
    lenofsubstring = len(sub_string)
    l = []
    count = 0
    if(len(string)>=1 or len(string)<=200):
        for i in range(len(string)):
            x=''
            if((len(string) - i)>=lenofsubstring):
                for j in range(i,i+lenofsubstring):
                    x = x + string[j]
                l.append(x)
    for i in l:
        if(i == sub_string):
            count = count + 1

    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
