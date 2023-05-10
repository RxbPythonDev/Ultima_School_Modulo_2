import hashlib
import getpass

def validar_login(cursor):
    email = input('Digite seu e-mail: ')
    senha = getpass.getpass('Digite sua senha: ')

    sql = 'select * from usuario where email = ? and senha = ?'

    senha = hashlib.sha256(senha.encode('utf-8')).hexdigest()

    valores = [email, senha]
    consulta = cursor.execute(sql, valores)

    usuario = None
    for resultado in consulta:
        usuario = resultado
        break

    if usuario is None:
        raise Exception('Email ou Senha inválidos!')
    return usuario