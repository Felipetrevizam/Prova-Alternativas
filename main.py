# Prova com 5 perguntas e alternativas a,b,c,d

# Dicionario:
prova = {"Pergunta1": ["As sociedades antigas consideravam a escravidão como um direito adquirido.\
Na Grécia, os escravos eram originários de:", "a) capturas de guerras ou através de compras", "b) capturas\
de guerra ou através de escambo", "c) comprados na África ou através de escambos", "d) dos países pobres", "a"],
         "Pergunta2": ["Os gregos eram religiosos, podemos destacar duas característica fundamental da\
religião grega", "a) monoteísmo e antropomorfismo", "b) monoteísmo e crença em animais", "c) politeísmo e\
antropomorfismo", "d) antropomorfismo e existências de demônio", "c"],
         "Pergunta3": ["Durante a Monarquia, a sociedade romana já se dividia em grandes grupos sociais", "a) \
aristocratas, clientes, plebeus e escravos", "b) patrícios, clientes, plebeus e escravos", "c) patrícios, clientes,\
plebeus e servos", "d) aristocratas, clientes, plebeus e servos", "c"],
         "Pergunta4": ["A função básica da colônia era", "a) ser uma continuação da metrópole", "b) prover os lucros\
necessários para a burguesia mercantil", "c) receber os lucros da metrópole", "d) agrupar as pessoas que não queria\
ficar na metrópole", "b"],
         "Pergunta5": ["A filosofia iluminista preocupou-se com o estudo da", "a) sociedade e da razão", "b) natureza e\
da razão", "c) natureza e da sociedade", "d) natureza e da sociedade", "c"]}

respostas = []
for pergunta in prova:
    print(prova[pergunta][0], prova[pergunta][1], prova[pergunta][2], prova[pergunta][3], prova[pergunta][4], "Insira a resposta como 'a', 'b', 'c' ou 'd'", sep='\n')
    respostas.append(input("Resposta: "))
    print("\n")

resultado = 0

for pergunta, resposta in zip(prova, respostas):
    if resposta == prova[pergunta][5]:
        print(f"Resposta da {pergunta} está correta")
        resultado += 2
    else:
        print(f"Resposta da {pergunta} está errada")

print(f"\nSua nota é: {resultado}")

