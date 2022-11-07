def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    ans = ''
    for i in range(n):
        if i==0:
            ans+=''+str(i)
        else :   
           ans+=','+str(i)
    return ans
print(main(4))
   