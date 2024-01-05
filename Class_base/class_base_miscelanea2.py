import sqlite3
import timeit

#Nova
inicio = timeit.default_timer()
lista_de_circuitos_de_alta_para_media=[]
#ct_at = self.DataBaseConn.getSQLDB("CTAT","SELECT * FROM ctat;")
conn_ctmt = sqlite3.connect("CTAT.sqlite")
ct_at = conn_ctmt.cursor()
ct_at.execute("SELECT DISTINCT nome FROM ctat WHERE nome LIKE '"+
              "FDR%" + "' AND NOT (nome LIKE '%2' OR nome LIKE '%3' OR nome LIKE '%4')  ORDER BY nome")

for ctat in ct_at.fetchall():
    lista_de_circuitos_de_alta_para_media.append(ctat[0])

print(lista_de_circuitos_de_alta_para_media)
conn_ctmt.close()

fim = timeit.default_timer()
print("O tempo de exec nova é : %f" % (fim - inicio))


#Velha
inicio = timeit.default_timer()
lista_de_circuitos_de_alta_para_media=[]

#ct_at = self.DataBaseConn.getSQLDB("CTAT","SELECT * FROM ctat;")
conn_ctmt = sqlite3.connect("CTAT.sqlite")
ct_at = conn_ctmt.cursor()
ct_at.execute("SELECT DISTINCT nome FROM ctat ORDER BY nome")

for ctat in ct_at.fetchall():
    if ctat[0][0:3] == "FDR":
        lista_de_circuitos_de_alta_para_media.append(ctat[0])

for elemento in lista_de_circuitos_de_alta_para_media:
    if elemento[-1] == "2":
        lista_de_circuitos_de_alta_para_media.remove(elemento)

lista_de_circuitos_de_alta_para_media_filtradas=(sorted(set(lista_de_circuitos_de_alta_para_media)))

print(lista_de_circuitos_de_alta_para_media_filtradas)

conn_ctmt.close()
fim = timeit.default_timer()
print("O tempo de exec velha é : %f" % (fim - inicio))