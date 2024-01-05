import sqlite3
import timeit

sqlStrUNTRD = "SELECT DISTINCT cod_id, pot_nom FROM  untrd WHERE ctmt = '" + "950" + "' AND pos = 'PD'"

lista_dados = []
conn_ctmt = sqlite3.connect("UNTRD.sqlite")
ct_mt = conn_ctmt.cursor()
dadosUNTRD = ct_mt.execute(sqlStrUNTRD)

for lnhUNTRD in dadosUNTRD.fetchall():  # Pegando o Transformador

    #  if lnhUNTRD[0] in listTrafoBT:

    ##Verificar a questão do X e do Y

    # tmp_dados = [lnhUNTRD[0],lnhUNTRD[1]]
    tmp_dados = lnhUNTRD[0]

    lista_dados.append(tmp_dados)

lista_dados = sorted(set(lista_dados))

print(lista_dados)