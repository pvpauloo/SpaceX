import re
import openpyxl
from datetime import date


class ModuloProcessamento:

    def Geral(self, opc, arquivos):
        dicionario = dict()
        conjunto = []
        field39 = ''
        for file in arquivos:
            arquivo = open(f'{file}', 'r', encoding='utf-8')
            v = True
            while v:
                linha = arquivo.readline()
                if linha.__contains__('<'):
                    if linha.__contains__('<log realm="mastercard-channel/'):
                        log = re.search('\d+\-\d+\-\d+T\d+:\d+:\d+\.\d+', linha)
                        linha = arquivo.readline()
                        linha = arquivo.readline()
                        linha = arquivo.readline()
                        linha = arquivo.readline()
                        if linha.__contains__('<field id="0" value="0420"/>') \
                                or linha.__contains__('<field id="0" value="0110"/>') \
                                or linha.__contains__('<field id="0" value="0400"/>') \
                                or linha.__contains__('<field id="0" value="0120"/>') \
                                or linha.__contains__('<field id="0" value="0400"/>') \
                                or linha.__contains__('<field id="0" value="0100"/>'):
                            field0 = re.findall(r'\d+', linha.strip(" "))
                            field2 = re.search('\d+______\d+', arquivo.readline().strip(" "))
                            if field2.group().__contains__('______'):
                                field3 = re.findall(r'\d+', arquivo.readline().strip(" "))
                                field4 = re.findall(r'\d+', arquivo.readline().strip(" "))
                                field5 = re.findall(r'\d+', arquivo.readline().strip(" "))
                                field6 = re.findall(r'\d+', arquivo.readline().strip(" "))
                                field7 = re.findall(r'\d+', arquivo.readline().strip(" "))
                                field9 = re.findall(r'\d+', arquivo.readline().strip(" "))
                                field10 = re.findall(r'\d+', arquivo.readline().strip(" "))
                                field11 = re.findall(r'\d+', arquivo.readline().strip(" "))
                                linha = arquivo.readline()
                                if field0.__contains__('0100'):
                                    if log:
                                        dicionario.clear()
                                        dicionario['Data'] = log.group()
                                        dicionario['MTI'] = field0[1]
                                        dicionario['Card Number'] = field2[0]
                                        dicionario['Processing Code'] = field3[1]
                                        dicionario['Amount Transaction'] = field4[1]
                                        dicionario['Amount Settlement'] = field5[1]
                                        dicionario['Amount Billing'] = field6[1]
                                        dicionario['Transmission Date Time'] = field7[1]
                                        dicionario['Conversion, settlement'] = field9[1]
                                        dicionario['Conversion rate, billing'] = field10[1]
                                        dicionario['Terminal Code'] = field11[1]
                                        dicionario['Response Code'] = ''
                                        dicionario['ORIGINAL MTI'] = ''
                                        dicionario['ORIGINAL TERMINAL'] = ''
                                        dicionario['ORIGINAL TIMESTAMP'] = ''
                                        conjunto.append(dicionario.copy())
                                    else:
                                        dicionario.clear()
                                        dicionario['Data'] = log
                                        dicionario['MTI'] = field0[1]
                                        dicionario['Card Number'] = field2[0]
                                        dicionario['Processing Code'] = field3[1]
                                        dicionario['Amount Transaction'] = field4[1]
                                        dicionario['Amount Settlement'] = field5[1]
                                        dicionario['Amount Billing'] = field6[1]
                                        dicionario['Transmission Date Time'] = field7[1]
                                        dicionario['Conversion, settlement'] = field9[1]
                                        dicionario['Conversion rate, billing'] = field10[1]
                                        dicionario['Terminal Code'] = field11[1]
                                        dicionario['Response Code'] = ''
                                        dicionario['ORIGINAL MTI'] = ''
                                        dicionario['ORIGINAL TERMINAL'] = ''
                                        dicionario['ORIGINAL TIMESTAMP'] = ''
                                        conjunto.append(dicionario.copy())
                                else:
                                    while not linha.__contains__('<field id="39" value="'):
                                        linha = arquivo.readline().strip(" ")
                                        if linha.__contains__('<field id="39" value="'):
                                            field39 = re.findall(r'\d+', linha)
                                    while not linha.__contains__('<isomsg id="90">'):
                                        if len(linha) != 0:
                                            linha = arquivo.readline().strip(" ")
                                            if linha.__contains__('<isomsg id="90">'):
                                                arquivo.readline()
                                                field90_1 = re.findall(r'\d+', arquivo.readline().strip(" "))
                                                field90_2 = re.findall(r'\d+', arquivo.readline().strip(" "))
                                                field90_3 = re.findall(r'\d+', arquivo.readline().strip(" "))
                                                if log:
                                                    dicionario.clear()
                                                    dicionario['Data'] = log.group()
                                                    dicionario['MTI'] = field0[1]
                                                    dicionario['Card Number'] = field2[0]
                                                    dicionario['Processing Code'] = field3[1]
                                                    dicionario['Amount Transaction'] = field4[1]
                                                    dicionario['Amount Settlement'] = field5[1]
                                                    dicionario['Amount Billing'] = field6[1]
                                                    dicionario['Transmission Date Time'] = field7[1]
                                                    dicionario['Conversion, settlement'] = field9[1]
                                                    dicionario['Conversion rate, billing'] = field10[1]
                                                    dicionario['Terminal Code'] = field11[1]
                                                    dicionario['Response Code'] = field39[1]
                                                    dicionario['ORIGINAL MTI'] = field90_1[1]
                                                    dicionario['ORIGINAL TERMINAL'] = field90_2[1]
                                                    dicionario['ORIGINAL TIMESTAMP'] = field90_3[1]
                                                    conjunto.append(dicionario.copy())
                                                else:
                                                    dicionario.clear()
                                                    dicionario['Data'] = log
                                                    dicionario['MTI'] = field0[1]
                                                    dicionario['Card Number'] = field2[0]
                                                    dicionario['Processing Code'] = field3[1]
                                                    dicionario['Amount Transaction'] = field4[1]
                                                    dicionario['Amount Settlement'] = field5[1]
                                                    dicionario['Amount Billing'] = field6[1]
                                                    dicionario['Transmission Date Time'] = field7[1]
                                                    dicionario['Conversion, settlement'] = field9[1]
                                                    dicionario['Conversion rate, billing'] = field10[1]
                                                    dicionario['Terminal Code'] = field11[1]
                                                    dicionario['Response Code'] = field39[1]
                                                    dicionario['ORIGINAL MTI'] = field90_1[1]
                                                    dicionario['ORIGINAL TERMINAL'] = field90_2[1]
                                                    dicionario['ORIGINAL TIMESTAMP'] = field90_3[1]
                                                    conjunto.append(dicionario.copy())
                                        else:
                                            linha = '<isomsg id="90">'

                if len(linha) == 0:
                    v = False
                    arquivo.close()

        if opc:
            ModuloProcessamento.NewExcel('self', conjunto)

        return conjunto

    def NewExcel(self, conjunto):
        data = date.today()
        workbook = openpyxl.Workbook()
        worksheet = workbook.active
        worksheet.title = 'TRANSACOES'
        worksheet['A1'] = 'Data'
        worksheet['B1'] = 'MTI'
        worksheet['C1'] = 'Card Number'
        worksheet['D1'] = 'Processing Code'
        worksheet['E1'] = 'Amount Transaction'
        worksheet['F1'] = 'Amount Settlement'
        worksheet['G1'] = 'Amount Billing'
        worksheet['H1'] = 'Transmission Date Time'
        worksheet['I1'] = 'Conversion, settlement'
        worksheet['J1'] = 'Conversion rate, billing'
        worksheet['K1'] = 'Terminal Code'
        worksheet['L1'] = 'Response Code'
        worksheet['M1'] = 'ORIGINAL MTI'
        worksheet['N1'] = 'ORIGINAL TERMINAL'
        worksheet['O1'] = 'ORIGINAL TIMESTAMP'

        for i, conjunto in enumerate(conjunto):
            i += 2
            worksheet[f'A{i}'] = conjunto['Data']
            worksheet[f'B{i}'] = conjunto['MTI']
            worksheet[f'C{i}'] = conjunto['Card Number']
            worksheet[f'D{i}'] = conjunto['Processing Code']
            worksheet[f'E{i}'] = conjunto['Amount Transaction']
            worksheet[f'F{i}'] = conjunto['Amount Settlement']
            worksheet[f'G{i}'] = conjunto['Amount Billing']
            worksheet[f'H{i}'] = conjunto['Transmission Date Time']
            worksheet[f'I{i}'] = conjunto['Conversion, settlement']
            worksheet[f'J{i}'] = conjunto['Conversion rate, billing']
            worksheet[f'K{i}'] = conjunto['Terminal Code']
            worksheet[f'L{i}'] = conjunto['Response Code']
            worksheet[f'M{i}'] = conjunto['ORIGINAL MTI']
            worksheet[f'N{i}'] = conjunto['ORIGINAL TERMINAL']
            worksheet[f'O{i}'] = conjunto['ORIGINAL TIMESTAMP']
            nomearqui = conjunto["Transmission Date Time"]
        workbook.save(f'Resultados/Q2_Processado-{nomearqui}.xlsx')
