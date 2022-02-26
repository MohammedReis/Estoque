from itertools import chain


def Cripto(senha):
    chave = 8
    traduzir = ''
    chave *= 1
    for criptografar in senha:
        if criptografar.isalpha():
            num = ord(criptografar)
            num += chave
            if criptografar.isupper():
                if num> ord('Z'):
                    num-=26
                elif num< ord('A'):
                    num +=26
            
            elif criptografar.islower():
                if num > ord('z'):
                        num-=26
                elif num < ord('a'):
                    num +=26
            traduzir += chr(num)
            
        else:
            traduzir += criptografar
    return traduzir

def Descripto(senha):
    chave = 8
    traduzir = ''
    chave *= -1
    for criptografar in senha:
        if criptografar.isalpha():
            num = ord(criptografar)
            num += chave
            if criptografar.isupper():
                if num> ord('Z'):
                    num-=26
                elif num< ord('A'):
                    num +=26
            
            elif criptografar.islower():
                if num > ord('z'):
                        num-=26
                elif num < ord('a'):
                    num +=26
            traduzir += chr(num)
            
        else:
            traduzir += criptografar
    return traduzir
