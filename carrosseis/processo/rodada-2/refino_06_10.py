# 8ª refinação, carrosséis 6 a 10 (a partir do Juiz B, rodada 2)
import json, glob
def load(n): f=glob.glob(f'{n}-*/roteiro.json')[0]; return f, json.load(open(f))
def save(f,d): json.dump(d, open(f,'w'), ensure_ascii=False, indent=1)
def rep(d,a,b):
    assert a in d['legenda'], a; d['legenda']=d['legenda'].replace(a,b)

# C06: pausa com ideia nova; itens precisos; uma cena; CTA inclui o leitor
f,d=load('06'); S=d['slides']
S[2]['blocos'].append(['corpo-suave','E aí vem o mês em que o telefone não toca.'])
S[3]['itens'][2]=['Planejar','sem saber o próximo mês, ninguém contrata']
S[4]['linhas']=['Mês bom, parece que o negócio cresceu.','Mês ruim, parece crise.','<em>Era só a indicação.</em>']
S[7]['itens'][3]=['Mantenha','o anúncio ligado, cobrindo a diferença']
S[8]['lead']='Você ou alguém que você conhece vive de indicação?'
save(f,d)

# C07: slide 3 por sintoma (com atendimento); slide 6 vira decisões, sem repetir o 3
f,d=load('07'); S=d['slides']
S[2]['rotulo']=S[2]['titulo']='Onde travou'
S[2]['itens']=[['Ninguém clicou','público ou oferta'],['Clicaram e não chamaram','o caminho'],
  ['Chamaram e não compraram','o atendimento'],['Venderam e não sobrou','a margem']]
S[2]['fecho']='Cada sintoma tem <em>conserto diferente.</em>'
S[5]['rotulo']=S[5]['titulo']='Antes da próxima, escreva'
S[5]['itens']=[['Quem compra','e por que compraria agora'],['Quem responde','quem chamar, e em quanto tempo'],
  ['Quanto tempo','vai rodar antes de julgar'],['Quanto pode custar','um cliente, no máximo']]
rep(d,'Foi o público? A oferta? O que a pessoa encontrou depois do clique? A campanha desligada antes de ter dados? Ou a margem, que nunca ia fechar? Cada uma tem um conserto diferente.',
  'Ninguém clicou? Clicaram e não chamaram? Chamaram e ninguém respondeu a tempo? Venderam e não sobrou nada? Cada sintoma tem um conserto diferente.')
save(f,d)

# C08: frase-chave em destaque; um exemplo que faz sentir o engano do clique; uma ação só
f,d=load('08'); S=d['slides']
S[1]['blocos'][1]=['corpo-suave','E no fim do mês, a pergunta continua: quantas vendas vieram daí?']
S[2]['blocos']=[['manchete','Campanha que mira clique <em>entrega clique.</em>'],
  ['corpo','Esses números não estão errados. Dizem se o anúncio chamou atenção. Não dizem se ele pagou a conta.']]
S[3]['rotulo']=S[3]['titulo']='Os números que faltam'
exemplo={'tipo':'texto','titulo':'Um exemplo','rotulo':'Um exemplo','blocos':[
  ['manchete','Dois anúncios, mesma verba.'],
  ['corpo','O A trouxe mais cliques. O B, menos cliques e mais clientes.'],
  ['corpo-suave','Pelo relatório de clique, você desligaria <em>o B.</em>']]}
S.insert(3, exemplo)
rep(d,'Qual desses quatro você sabe hoje de cabeça?\n\n','Se você não sabe nenhum dos quatro de cabeça, este post é para você.\n\n')
save(f,d)

# C09: WhatsApp antes do técnico; jargão para a legenda; uma pausa no meio
f,d=load('09'); S=d['slides']
S[1]['blocos']=[['manchete','“Acho que <em>do Instagram.</em>”'],
  ['corpo-suave','É a resposta de muito dono de negócio. Não por descuido: ninguém montou o jeito de saber.']]
S[3]={'tipo':'pausa','titulo':'Pausa','linhas':['Sem saber de onde veio a venda,','você pode cortar o que funcionava.','<em>E manter o que não.</em>']}
S[5]['itens']=[['Pixel','avisa a plataforma de cada venda ou pedido'],['Links com etiqueta','mostram qual anúncio trouxe a visita'],
  ['Uma pergunta','“como você conheceu a gente?”']]
S[5], S[6] = S[6], S[5]
save(f,d)

# C10: precisão do slide 6 (quem vende pelo WhatsApp); Gerenciador apresentado; o botão explicado no slide
f,d=load('10'); S=d['slides']
S[1]['rotulo']=S[1]['titulo']='O botão'
S[1]['blocos'][1]=['corpo-suave','No Instagram, Turbinar. No Facebook, Impulsionar. Mostra seu post para mais gente e pede uma visita ou mensagem.']
S[2]['rotulo']=S[2]['titulo']='O que só o Gerenciador tem'
S[2]['itens']=[['Objetivo','de venda ou cadastro'],['Teste','vários anúncios lado a lado'],
  ['Onde aparece','feed, stories ou reels, você escolhe'],['Relatório','qual anúncio e público trouxe resultado']]
S[5]['blocos']=[['manchete','O botão procura quem interage. O Gerenciador pode procurar <em>quem compra.</em>'],
  ['corpo-suave','Desde que ele saiba quem comprou. Sem essa medição, os dois procuram quase a mesma pessoa.']]
rep(d,'o Gerenciador só procura quem compra se o seu site mede cada venda.',
  'o Gerenciador só procura quem compra se ele fica sabendo de cada venda, pelo site ou pelo WhatsApp.')
save(f,d)
