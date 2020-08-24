def free(i,j,board):
    return (board['row'][i]==0 and board['column'][j]==0 and board['NWtoSE'][j-i]==0 and board['SWtoNE'][j+i]==0)
        


def fill(i,j,board):
    board['row'][i]=1
    board['column'][j]=1
    board['NWtoSE'][j-i]=1
    board['SWtoNE'][j+i]=1
    board['queen'][i]=j

def undo(i,j,board):
    board['row'][i]=0
    board['column'][j]=0
    board['NWtoSE'][j-i]=0
    board['SWtoNE'][j+i]=0
    board['queen'][i]=-1


def show(board):
        for i in sorted(board['queen'].keys()):
            print((i,board['queen'][i]))


def initialize(n):
    board={'row':{},
            'column':{},
            'NWtoSE':{},
            'SWtoNE':{},
            'queen':{}
            }

    for i in range(n):
        board['row'][i]=0
        board['column'][i]=0
        board['queen'][i]=-1
    
    for i in range(-(n-1),n):
        board['NWtoSE'][i]=0


    for i in range(2*n-1):
        board['SWtoNE'][i]=0

    return board



def place(i,board):
    n=len(board['queen'].keys())
    for j in range(n):
        if free(i,j,board):
            fill(i,j,board)
            if(i==n-1):
                return True
            else:
                extendsol=place(i+1,board)
            if(extendsol):
                return True 
            else:
                undo(i,j,board)
    else:
        return False                    

def main():
    n=int(input("Enter the no of queen you want"))

    board=initialize(n)
    
    if place(0,board):
        show(board)


main()