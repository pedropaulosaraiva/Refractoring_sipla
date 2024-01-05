import os
import platform

import database.class_conn
import class_exception

class C_DBase():
    def __init__(self):

##########################

        self.DataBaseConn = database.class_conn.C_DBaseConn() #Criando a instância do Banco de Dados

################################# Métodos Novos

    def getSE_AT_DB(self):
        # Seleciona e salva as subestações presentes nos CTMT numa lista em ordem alfabética
        try:
            lista_de_subestacoes_de_alta_tensao = []

            subs = self.DataBaseConn.getSQLDB("CTMT","SELECT DISTINCT sub FROM ctmt ORDER BY sub")

            for sub in subs.fetchall():
                lista_de_subestacoes_de_alta_tensao.append(sub[0])

            return lista_de_subestacoes_de_alta_tensao
        except:
            raise class_exception.ExecDataBaseError("Erro ao pegar os Circuitos de Alta Tensão!")

    def getCirAT_MT_DB(self, nomeSE_AT):
        # Seleciona e salva os CTAT de uma determinada SUB numa lista
        try:
            lista_de_circuitos_de_alta_para_media = []

            ct_at = self.DataBaseConn.getSQLDB("CTAT", "SELECT DISTINCT nome FROM ctat WHERE nome LIKE '"+
                                               nomeSE_AT+"%' AND NOT (nome LIKE '%2' OR nome LIKE '%3' OR nome LIKE '%4') ORDER BY nome")

            for ctat in ct_at.fetchall():
                lista_de_circuitos_de_alta_para_media.append(ctat[0])

            return lista_de_circuitos_de_alta_para_media
        except:
            raise class_exception.ExecDataBaseError("Erro ao pegar os Circuitos de Média Tensão!")

    def getSE_MT_AL_DB(self, nomeSE_MT):
        # Seleciona e salva os CTMT de uma determinada SUB numa lista
        try:
            lista_de_alimentadores_de_media_tensao= []

            ct_mt = self.DataBaseConn.getSQLDB("CTMT","SELECT DISTINCT nome, cod_id FROM ctmt WHERE sub = '"+
                                               nomeSE_MT[0]+"'ORDER BY nome") #OBS: nomeSE_MT é uma lista

            for ctmt in ct_mt.fetchall():
                lista_de_alimentadores_de_media_tensao.append(ctmt)

            return lista_de_alimentadores_de_media_tensao
        except:
            raise class_exception.ExecDataBaseError("Erro ao pegar os Alimentadores de Média Tensão!")

    def getSE_MT_AL_TrafoDIST(self, codField):
        # Seleciona e salva os tranformadores de distribuição presentes num CTMT numa lista
        try:
            lista_transformadores_de_distribuicao = []

            transformadores = self.DataBaseConn.getSQLDB("UNTRD", "SELECT DISTINCT cod_id, pot_nom FROM  untrd WHERE ctmt = '" +
                                                         codField + "' AND pos = 'PD' ORDER BY cod_id")

            for transformador in transformadores.fetchall():
                lista_transformadores_de_distribuicao.append(transformador[0])

            return lista_transformadores_de_distribuicao

        except:
            raise class_exception.ExecData(
            "Erro no processamento do Banco de Dados para os Transformadores de Distribuição! ")