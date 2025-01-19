def verificar_aniversarios(alunos):
    registro = set()
    for aluno in alunos:
        aniversario = aluno['aniversario']
        if aniversario in registro:
            return f"Par encontrado: {aluno['nome']} tem o mesmo aniversário que outro aluno."
        registro.add(aniversario)
    return "Nenhum par encontrado."

# Exemplo de uso
alunos = [
    {'nome': 'Alice', 'aniversario': '01/03'},
    {'nome': 'Bob', 'aniversario': '02/02'},
    {'nome': 'Charlie', 'aniversario': '01/01'}
]

resultado = verificar_aniversarios(alunos)
print(resultado)