from func import med, qtd_med, sep, est, maior, conc
 
QTD = 10
 
 
def ler():

    nom = []
    n = []
 
    for i in range(QTD):
        nm = input(f"Digite o nome do aluno {i + 1}: ")
        v = float(input(f"Digite a nota de {nm}: "))
 
        nom = nom + [nm]
        n = n + [v]
 
    return nom, n
 
 
def main():
    nom, n = ler()
 
    print("\n===== RESULTADOS =====")
 
    # 2) Media das notas
    m = med(n)
    print(f"\nMedia da turma: {m:.2f}")
 
    # 3) Alunos acima ou igual a media
    q = qtd_med(n, m)
    print(f"Quantidade de alunos com nota >= media: {q}")
 
    # 4) Separacao de notas em posicoes pares e impares
    par, imp = sep(n)
    print(f"Notas em posicoes pares:   {par}")
    print(f"Notas em posicoes impares: {imp}")
 
    # 5) Estatisticas de aprovacao/recuperacao/reprovacao
    pa, pr, pv = est(n)
    print(f"\nPercentual de aprovados (>= 7,0):    {pa:.1f}%")
    print(f"Percentual em recuperacao (5,0 a 6,9): {pr:.1f}%")
    print(f"Percentual de reprovados (< 5,0):     {pv:.1f}%")
 
    # 6) Maior nota e aluno correspondente
    mx, a = maior(n, nom)
    print(f"\nMaior nota: {mx} - Aluno: {a}")
 
    # 7) Vetor de conceitos
    c = conc(n)
    print("\nConceitos por aluno:")
    for i in range(QTD):
        print(f"  {nom[i]}: nota {n[i]:.1f} -> conceito {c[i]}")
 
 
if __name__ == "__main__":
    main()