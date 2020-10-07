import re

# validador de cpfs:
cpf = """
878.784.485-78
878.784.485-79
878.784.485-80
878.784.485-81
"""
cpf_reg_exp = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', flags=re.M)
# print(cpf_reg_exp.findall(cpf))


# validador de ips:
# compiler para ler:
ip_reg_exp = re.compile(r'''
    ^ #começa com
        (?: # não sera salvo na memoria
            (?: # não sera salvo na memoria
                #ranges
                25[0-5]|
                2[0-4][0-9]|
                1[0-9]{2}|
                [1-9][0-9]|
                [0-9]
            )
            \.? # escapa o ponto e o deixa opicional
        ){4} # repete 4 vezes
        \b # borada para garantir que não exista um ponto no final, ja que é opcional
    $ # termina com 
     
''', flags=re.X)
# para cópia:
ip_reg_exp = re.compile(r'^(?:(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])\.?){4}\b$')
myipv4 = '10.0.0.10'
for i in range(301):
    ip = f'{i}.{i}.{i}.{i}'
    print(ip, ip_reg_exp.findall(ip))
