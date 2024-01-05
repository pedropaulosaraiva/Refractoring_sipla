import sqlite3

#Função velha 1
lista_de_subestacoes_de_alta_tensao_disponivel_formato_proprio_do_banco = []
lista_de_subestacoes_de_alta_tensao_disponivel = []

# ct_at = self.DataBaseConn.getSQLDB("CTAT","SELECT * FROM ctat;")
##ct_at = self.DataBaseConn.getSQLDB("CTMT", "SELECT sub FROM ctmt;")
conn_ctmt = sqlite3.connect("CTMT.sqlite")
ct_at = conn_ctmt.cursor()
ct_at. execute("SELECT sub FROM ctmt")

for ctat in ct_at.fetchall():
    # lista_de_subestacoes_de_alta_tensao_disponivel_formato_proprio_do_banco.append(ctat[3])
    lista_de_subestacoes_de_alta_tensao_disponivel_formato_proprio_do_banco.append(ctat[0])

lista_de_subestacoes_de_alta_tensao_disponivel_formato_proprio_do_banco_filtradas = (
    sorted(set(lista_de_subestacoes_de_alta_tensao_disponivel_formato_proprio_do_banco)))

for lista_sub in lista_de_subestacoes_de_alta_tensao_disponivel_formato_proprio_do_banco_filtradas:
    lista_de_subestacoes_de_alta_tensao_disponivel.append(lista_sub[0:3])

lista_de_subestacoes_de_alta_tensao_disponivel_filtrada = (
    sorted(set(lista_de_subestacoes_de_alta_tensao_disponivel)))

print(lista_de_subestacoes_de_alta_tensao_disponivel_filtrada)

conn_ctmt.close()

#proposta de função nova
lista_de_subestacoes_de_alta_tensao_disponivel_filtrada = []

conn_ctmt = sqlite3.connect("CTMT.sqlite")
ct_at = conn_ctmt.cursor()
ct_at.execute("SELECT DISTINCT sub FROM ctmt ORDER BY sub")

for ctat in ct_at.fetchall():
    lista_de_subestacoes_de_alta_tensao_disponivel_filtrada.append(ctat[0])

print(lista_de_subestacoes_de_alta_tensao_disponivel_filtrada)
conn_ctmt.close()

