def rotate(string, n):
    """Rotate characters in a string. Expects string and n (int) for 
       number of characters to move.

       if n is positive move characters from beginning to end, e.g.:
            rotate('hello', 2) would return 'llohe'

       if n is negative move characters to the start of the string, e.g:
            rotate('hello', -2) would return 'lohel'

       There are many ways to solve this. Which one is most elegant and
       has the best performance (hint: check stdlib)
    """
    return string[n:]+string[0:n]
