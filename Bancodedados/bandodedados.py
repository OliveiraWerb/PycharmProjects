import mysql.connector

conectado = mysql.connector.connect(
    user='root',
    password='',
    host='127.0.0.1',
    database='frequencia'
)

cursor = conectado.cursor()

lista_cursos = {'1':'Redes de Computadores', '2':'ADS'}

inserir_dados = "INSERT INTO " \
                "cadastro(mat, nome, sobrenome, curso, telefone, endereco)" \
                "VALUES(%s, %s, %s, %s, %s, %s)"
buscar_dados = "SELECT * FROM cadastro"

dados = ['202202326', 'Joao dandara', 'Mesquita', '01', '85988180053', 'Rua Toba']

#cursor.execute(inserir_dados, dados)
#conectado.commit()

cursor.execute(buscar_dados)
resultado = cursor.fetchall()

curso = str(resultado[0][4])
print(curso)
print(type(curso))
print(lista_cursos[curso])


cursor.close()
conectado.close()