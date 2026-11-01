# 8ª refinação, carrosséis 11 a 15 (a partir do Juiz C, rodada 2)
import json, glob
def load(n): f=glob.glob(f'{n}-*/roteiro.json')[0]; return f, json.load(open(f))
def save(f,d): json.dump(d, open(f,'w'), ensure_ascii=False, indent=1)
def rep(d,a,b):
    assert a in d['legenda'], a; d['legenda']=d['legenda'].replace(a,b)

# C11: "não divida" antes da pausa; o mapa entra; slide duplo mais leve; chave igual à pergunta
f,d=load('11'); S=d['slides']
S[2]['blocos'][1][1]+=' E muitas vezes escolhe pelo mapa.'
S[4]['blocos'][0]['itens']=[x for x in S[4]['blocos'][0]['itens'] if 'compara' not in x]
S[5],S[6]=S[6],S[5]
S[7]['chave']='Comente <b>Google, Instagram ou nenhum</b>'
save(f,d)

# C12: piso que o leitor calcula; pausa com o caso "teto abaixo do piso"; capa com mais curiosidade
f,d=load('12'); S=d['slides']
S[0]['texto']='Quanto investir em anúncio? <em>A resposta não começa pela verba.</em>'
S[3]['blocos'][1][1]+=' Desde que o seu caixa aguente esperar.'
S[4]['blocos'][1]=['corpo-suave','Divida a verba pelo custo de um contato. Se der poucos contatos por semana, a plataforma não tem com que aprender.']
S[5]['linhas']=['Se o teto não alcança o piso,','a verba certa, hoje,','<em>é nenhuma.</em>']
S[6]['itens']=[['O teto','quanto você pode pagar por um cliente'],['Vezes','os clientes a mais que você consegue atender'],
  ['Nunca abaixo','do piso que a plataforma precisa']]
rep(d,'Um detalhe que muda tudo: quanto custa um cliente depende também de quem atende o contato.\n\n','')
rep(d,'Tem também o piso: verba que mal gera contato não ensina nada à plataforma, e parece que anúncio não funciona.',
  'Tem também o piso: divida a verba pelo custo de um contato. Se der poucos contatos por semana, a plataforma não tem com que aprender, e parece que anúncio não funciona. Se o teto não alcança o piso, a verba certa, hoje, é nenhuma.')
save(f,d)

# C13: o slide 2 admite o que a capa pergunta; cronograma sem contradição; CTA concreto
f,d=load('13'); S=d['slides']
S[1]['rotulo']=S[1]['titulo']='A resposta honesta'
S[1]['blocos']=[['manchete','Antes de olhar a sua conta, <em>ninguém sabe.</em>'],
  ['corpo-suave','Depende do seu volume, da oferta e do atendimento. O que dá para combinar é o que o primeiro mês precisa responder: quem compra de você.']]
S[3]['itens']=[['Semana um','liga a medição, do clique à venda'],['Semana dois','mostra o que traz contato'],
  ['Semana três','separa o fraco do forte'],['Semana quatro','mostra o primeiro custo por cliente']]
S[3]['fecho']='Com volume, <em>o chute vira critério.</em>'
S[7]['titulo2']='Comece sabendo <em>quando vai saber.</em>'
S[7]['lead']='No diagnóstico gratuito, a gente combina com você o que medir, em quanto tempo e quem registra a venda. São 30 minutos.'
rep(d,'quem compra de você, e por que compra.','quem compra de você.')
rep(d,'Um mês bem feito mede do clique à venda, mostra o que traz contato, corta o fraco e mostra o primeiro custo por cliente.',
  'Um mês bem feito liga a medição do clique à venda, mostra o que traz contato, separa o fraco do forte e mostra o primeiro custo por cliente. Com volume, o chute vira critério.')
rep(d,'Se quiser começar sabendo o que medir, comenta DIAGNÓSTICO.','Se quiser começar sabendo quando vai saber, comenta DIAGNÓSTICO.')
save(f,d)

# C14: o "não" da garantia em público; pausa que fecha o raciocínio; sem repetir "já te respondeu"
f,d=load('14'); S=d['slides']
S[2]['itens'][2][1]='alguém com nome, que fala com você'
S[3]['itens'][1][1]='se disser sim, desconfie'
S[4]['linhas']=['Ninguém controla tudo','entre o anúncio e a venda.','<em>Por isso, processo vale mais que garantia.</em>']
S[5]['blocos'][1]=['corpo','A conta fica no seu nome. Quem mexe nela, você conhece. Garantia de resultado, a gente não dá. E vai precisar dos seus números de venda.']
rep(d,'(Se disser sim, já te respondeu.)','(Se disser sim, desconfie.)')
rep(d,'Salve para usar na próxima conversa.','Se você ainda não me segue, segue: a série continua.\n\nSalve para usar na próxima conversa.')
save(f,d)

# C15: sem slide-espelho; pausa que não repete o fundador; o Google nomeado
f,d=load('15'); S=d['slides']
S[2]['itens'][2]=['O Google','perfil parado, sem avaliação recente']
S[3]={'tipo':'texto','titulo':'Quando é hora','rotulo':'Quando é hora','blocos':[
  ['manchete','Com os quatro de pé, anunciar <em>acelera o que já funciona.</em>'],
  ['corpo-suave','Oferta em uma frase. Resposta em minutos. Avaliação recente. Margem com folga.']]}
S[4]['blocos'][0]=['manchete','Do diagnóstico, você não sai com um não. Sai sabendo <em>o que arrumar primeiro.</em>']
S[5]['linhas']=['Anúncio não conserta','o que vem depois dele.','<em>Só mostra mais rápido.</em>']
rep(d,'se o perfil está parado e sem avaliação','se o seu Google está parado e sem avaliação recente')
save(f,d)

# C12: o slide do piso não repete 'aprender'
f,d=load('12'); d['slides'][4]['blocos'][1][1]='Divida a verba pelo custo de um contato. Se der poucos contatos por semana, ela fica no escuro.'; save(f,d)
