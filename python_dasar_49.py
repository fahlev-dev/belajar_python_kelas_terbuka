'''type hints untuk fungsi'''

# def fungsi(parameter):
#     print(parameter)

# fungsi(1)
# fungsi("Ucup")


def sepuluh_pangkat(argument:int) -> int:
    '''FUNGSI DENGAN HINTS'''
    output = 10 ** argument
    return output

HASIL = sepuluh_pangkat(2)
print(HASIL)

def display(argument:string):
    print(argument)

display("Ucup")