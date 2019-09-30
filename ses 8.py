first=0
second=1
strang1=''
strang2=''
s = 'azcbobobegghakl'
while second<len(s):
    if second>=len(s):
        break
    elif s[first]<=s[second]:
        strang1+=s[first:second+1]
        while second<=len(s):
            second+=1
            if second>=len(s):
                break
            elif s[second]>=strang1[-1]:
                strang1+=s[second]
                if len(strang1)>len(strang2):
                    strang2=strang1
            else:
                if len(strang1)>len(strang2):
                    strang2=strang1
                strang1=''
                first=second-1
                break
    else:
        if len(s[first])>len(strang2):
            strang2=s[first]
        first+=1
        second+=1
print("Longest substring in alphabetical order is:" + strang2)