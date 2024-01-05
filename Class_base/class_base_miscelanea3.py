import sqlite3
import timeit

#Nova
inicio = timeit.default_timer()

lista_de_alimentadores_de_media_tensao= []

#ct_mt = self.DataBaseConn.getSQLDB("CTMT","SELECT * FROM ctmt;")
conn_ctmt = sqlite3.connect("CTMT.sqlite")
ct_mt = conn_ctmt.cursor()
ct_mt.execute("SELECT DISTINCT nome, cod_id FROM ctmt WHERE sub = '" +
              "LDF" + "' ORDER BY nome")

for linha in ct_mt.fetchall():
    lista_de_alimentadores_de_media_tensao.append(linha)

print(lista_de_alimentadores_de_media_tensao)
conn_ctmt.close()

fim = timeit.default_timer()
print("O tempo de exec nova é : %f" % (fim - inicio))


#Velha
inicio = timeit.default_timer()

lista_de_alimentadores_de_media_tensao_disponiveis= []

#ct_mt = self.DataBaseConn.getSQLDB("CTMT","SELECT * FROM ctmt;")
conn_ctmt = sqlite3.connect("CTMT.sqlite")
ct_mt = conn_ctmt.cursor()
ct_mt.execute("SELECT DISTINCT nome, sub, cod_id FROM ctmt ORDER BY nome")

for linha in ct_mt.fetchall():

    if linha[1] == "LDF":
        lista_de_alimentadores_de_media_tensao_disponiveis.append( (linha[0], linha[2]))

lista_de_alimentadores_de_media_tensao_disponiveis_filtrados=(sorted(set(lista_de_alimentadores_de_media_tensao_disponiveis)))

print(lista_de_alimentadores_de_media_tensao_disponiveis_filtrados)
conn_ctmt.close()

fim = timeit.default_timer()
print("O tempo de exec velha é : %f" % (fim - inicio))