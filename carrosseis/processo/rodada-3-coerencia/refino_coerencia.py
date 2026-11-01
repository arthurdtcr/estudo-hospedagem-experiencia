# 9ª refinação: coerência e simplicidade nos 15 (pedido do Arthur, 01/11/2026). Regras em CONVENCOES.md.
import json, glob
def load(n): f=glob.glob(f'{n}-*/roteiro.json')[0]; return f, json.load(open(f))
def save(f,d): json.dump(d, open(f,'w'), ensure_ascii=False, indent=1)
def rep(d,a,b):
    assert a in d['legenda'], (d['id'], a); d['legenda']=d['legenda'].replace(a,b)
def T(t,r,*b): return {'tipo':'texto','titulo':t,'rotulo':r,'blocos':[list(x) for x in b]}
def L(t,r,itens,fecho=None,inicio=None):
    s={'tipo':'lista','titulo':t,'rotulo':r,'itens':[list(x) for x in itens]}
    if fecho: s['fecho']=fecho
    if inicio: s['inicio']=inicio
    return s
def P(*l): return {'tipo':'pausa','titulo':'Pausa','linhas':list(l)}
SEGUE_C='Se você ainda não me segue, segue antes: direct de quem não segue cai em solicitações.'
SEGUE_S='Se você ainda não me segue, segue: a série continua.'
# As quatro perguntas do diagnóstico, iguais no C4, no C5 e no C15
QUATRO=[['A oferta','cabe em uma frase?'],['O Google e o perfil','passam confiança?'],
        ['O WhatsApp','responde em minutos?'],['A margem','cada cliente deixa mais do que custa?']]

# C1
f,d=load('01'); S=d['slides']
S[3]=T('No fim do mês','No fim do mês',['manchete','A conclusão: “anúncio não funciona.”'],['filete',''],
       ['titulo','Às vezes é verdade. Mas muitas vezes o anúncio trouxe o cliente <em>até a porta.</em>'])
rep(d,'Este é o primeiro de cinco posts sobre o caminho até a venda.','Este é o primeiro post de uma série sobre o que acontece depois do clique.\n\n'+SEGUE_S)
save(f,d)

# C2: os três dados juntos, depois a pausa
f,d=load('02'); S=d['slides']
q=S[5]; q.update(rotulo='E quase ninguém responde',titulo='E quase ninguém responde',lead='das empresas responderam na primeira hora. As outras deixaram o cliente esperando.',
  nota='23% nunca responderam. Teste com 2.241 empresas dos EUA. Harvard Business Review, 2011.'); q.pop('corpo',None)
S[4],S[5]=S[5],S[4]
S[7]['lead']='No diagnóstico gratuito de 30 minutos, a gente confere o seu tempo de resposta e onde o anúncio perde cliente.'
save(f,d)

# C3
f,d=load('03'); S=d['slides']
S[2]=T('Uma estrela','Uma estrela',['manchete','Uma estrela a mais: de 5% a 9% <em>mais receita.</em>'],
       ['corpo','Nos restaurantes independentes. Nas grandes redes, nenhum efeito. Quem não tem nome famoso precisa provar.'],
       ['nota','Michael Luca, Harvard Business School, 2011. Yelp, Seattle.'])
S[3]=P('O anúncio traz até a porta.','Se ele entra,','<em>depende do que ele encontra.</em>')
rep(d,'Pesquise hoje o nome',SEGUE_S+'\n\nPesquise hoje o nome')
save(f,d)

# C4: um slide a menos; a lista vira as quatro perguntas
f,d=load('04'); S=d['slides']
S[2]=T('O segundo motivo','O segundo motivo',['manchete','Aumento grande faz o anúncio <em>recomeçar a aprender.</em>'],
       ['corpo-suave','A plataforma volta a testar para quem mostrar. Por um tempo, o resultado sobe e desce.'],['nota','Central de Ajuda da Meta.'])
S[3]=P('Mais verba traz mais gente.','Mas essa gente encontra','<em>os mesmos problemas.</em>')
S[4]=L('Antes de aumentar','Antes de aumentar, confira',QUATRO,'Se algum falha, mais verba é <em>perder dinheiro mais rápido.</em>')
S[6]=T('E a pressa?','E a pressa?',['manchete','Parece mais lento. Lento é seguir pagando <em>pelo mesmo erro.</em>'],
       ['corpo','Com os quatro em ordem, aumentar a verba faz sentido. A gente não é contra aumentar. É contra aumentar antes.'])
S[7].update(titulo2='Antes de aumentar, <em>confira os quatro.</em>',lead='No diagnóstico gratuito de 30 minutos, a gente confere os quatro com você.')
del S[5]
rep(d,'E quem chega de mais longe precisa de mais motivo para comprar. Oferta confusa, perfil fraco e resposta lenta já perdiam clientes. Com esse público mais frio, perdem ainda mais.',
  'Mais verba traz mais gente. Mas essa gente encontra os mesmos problemas: oferta confusa, perfil que não convence, resposta lenta.')
rep(d,'Não sou contra escalar. Sou contra escalar antes de arrumar o caminho.','Não sou contra aumentar. Sou contra aumentar antes.')
rep(d,'Antes de aumentar, quatro perguntas: a oferta cabe em uma frase? Quem procura seu nome confia? Quanto tempo você leva para responder? Quanto custa um cliente, e quanto ele deixa no caixa?',
  'Antes de aumentar, quatro perguntas: a oferta cabe em uma frase? O seu Google e o seu perfil passam confiança? O seu WhatsApp responde em minutos? Cada cliente deixa mais do que custa?')
rep(d,'Depois comenta DIAGNÓSTICO e a gente faz isso com você em 30 minutos, de graça.','Depois comenta DIAGNÓSTICO e a gente confere os quatro com você em 30 minutos, de graça.')
save(f,d)

# C5: "o que a gente olha" = as mesmas quatro perguntas; 30 minutos em todo lugar
f,d=load('05'); S=d['slides']
S[2]['itens'][2]=['30 minutos','direto com o Arthur']
S[3]=L('O que a gente olha','O que a gente olha',QUATRO)
S[7]['lead']='30 minutos, direto comigo. Contratando ou não, o diagnóstico fica com você.'
rep(d,'eu olho o seu perfil, o seu Google Maps, o seu site e os seus anúncios do jeito que um cliente olha.',
  'eu olho a sua oferta, o seu Google, o seu perfil e o seu WhatsApp do jeito que um cliente olha. Na conversa, a gente vê se cada cliente deixa mais do que custa.')
rep(d,'Em meia hora você sai','Em 30 minutos você sai')
save(f,d)

# C6
f,d=load('06'); rep(d,'Conhece alguém que vive de indicação?',SEGUE_S+'\n\nConhece alguém que vive de indicação?'); save(f,d)

# C7: fato e conclusão sem abstração; pausa que leva à lista
f,d=load('07'); S=d['slides']
S[3]=T('Antes de desistir','Antes de desistir',['manchete','Uma vez não é <em>todas as vezes.</em>'],
       ['corpo-suave','“Não funcionou” diz o que aconteceu. “Não funciona para o meu negócio” precisa de prova.'])
S[4]=P('Anúncio não é aposta.','É teste.','<em>E teste se anota antes.</em>')
S[5]['rotulo']=S[5]['titulo']='Antes da próxima, anote'
S[5]['itens'][1]=['Quem responde','quem atende, e em quanto tempo']
S[6]['lead']='No diagnóstico gratuito de 30 minutos, a gente olha a última tentativa antes de falar da próxima.'
rep(d,'Mas tem uma diferença entre “não funcionou” e “não funciona para o meu negócio”. A primeira é um fato. A segunda é uma conclusão, e conclusão precisa de dado.',
  'Mas uma vez não é todas as vezes. “Não funcionou” diz o que aconteceu. “Não funciona para o meu negócio” precisa de prova.')
rep(d,'Se quiser que eu olhe a sua última tentativa antes da próxima, comenta DIAGNÓSTICO.','Depois comenta DIAGNÓSTICO e eu olho a sua última tentativa antes da próxima.')
save(f,d)

# C8
f,d=load('08'); S=d['slides']
S[2]=T('O que eles dizem','O que eles dizem',['manchete','Esses números dizem se o anúncio <em>chamou atenção.</em>'],
       ['corpo','Não dizem se ele pagou a conta. E campanha feita para dar clique entrega clique.'])
S[4]['itens']=[['Custo por contato','quanto custa cada pessoa que chamou'],['Contato que vira cliente','de cada dez, quantos compram'],
  ['Custo por cliente','verba dividida pelos clientes do anúncio'],['Margem','quanto cada cliente deixa, já pago o anúncio']]
rep(d,'Salve este post e leve',SEGUE_S+'\n\nSalve este post e leve')
save(f,d)

# C9: do mais simples ao mais técnico
f,d=load('09'); S=d['slides']
efeito=S[4]; efeito['rotulo']=efeito['titulo']='Por que importa'
simples=L('Comece pelo simples','Comece pelo simples',[['Uma pergunta','“como você conheceu a gente?”'],
  ['Uma mensagem pronta por anúncio','“vi o anúncio da promoção”'],['Etiquetas no WhatsApp Business','contato, orçamento, cliente']],
  'No fim do mês, você vê <em>qual anúncio trouxe cliente.</em>')
site=L('No site','No site',[['Pixel','avisa a plataforma de cada venda ou pedido'],['Links com etiqueta','mostram qual anúncio trouxe a visita']],
  'Perfeito não existe. <em>O básico, sim.</em>')
d['slides']=S[:4]+[simples,efeito,site,S[7]]
rep(d,'Salve este post e comece',SEGUE_S+'\n\nSalve este post e comece')
save(f,d)

# C10: problema, porquê, alternativa, honestidade
f,d=load('10'); S=d['slides']
S[2]['fecho']='Para vender todo mês, <em>é por aqui.</em>'
S[4]['blocos']=[['manchete','Às vezes o botão <em>basta.</em>'],['corpo-suave','Para um post que já foi bem, uma novidade na sua região ou um evento no fim de semana.']]
S[6]['lead']='No diagnóstico gratuito de 30 minutos, a gente olha o que você pede para a plataforma hoje e o que acontece depois do clique.'
d['slides']=[S[0],S[1],S[3],S[5],S[2],S[4],S[6]]
rep(d,'Se quiser que eu olhe o que você está pedindo para a plataforma hoje, comenta DIAGNÓSTICO.','Depois comenta DIAGNÓSTICO e eu olho o que você está pedindo para a plataforma hoje.')
save(f,d)

# C11: a pausa liga os dois canais antes da escolha, e não depois do "não divida"
f,d=load('11'); S=d['slides']
S[2]['blocos'][1][1]='Encanador 24 horas. Dentista perto de mim. Advogado trabalhista. A pessoa sabe o que quer. Só não escolheu de quem.'
S[7]['lead']='E o seu negócio, anuncia onde hoje?'
d['slides']=S[:4]+[S[6],S[4],S[5],S[7]]
save(f,d)

# C12: a conta em três passos que o leitor consegue repetir
f,d=load('12'); S=d['slides']
S[4]['blocos']=[['manchete','Existe um mínimo: <em>o piso.</em>'],
  ['corpo-suave','Divida a verba pelo custo de um contato. Se der só alguns contatos por semana, a plataforma não tem com o que aprender.']]
S[6]=L('A conta da verba','A conta da verba',[['Quantos clientes a mais','você consegue atender por mês'],['Vezes o teto','o máximo por cliente'],
  ['Nunca abaixo do piso','senão a plataforma não aprende']],'A mensalidade da agência <em>também entra.</em>')
S[7]['lead']='No diagnóstico gratuito de 30 minutos, com o seu preço, a sua margem e quantos clientes você consegue atender.'
rep(d,'A conta fica assim: o teto, vezes quantos clientes a mais você consegue atender, nunca abaixo do piso.',
  'A conta fica assim: quantos clientes a mais você consegue atender por mês, vezes o teto. Nunca abaixo do piso.')
rep(d,'Se quiser fazer essa conta com os seus números, comenta DIAGNÓSTICO.','Depois comenta DIAGNÓSTICO e a gente faz essa conta com os seus números.')
save(f,d)

# C13: sem frase-enigma
f,d=load('13'); S=d['slides']
S[3]['fecho']='No fim do mês, você decide <em>com número, não com palpite.</em>'
S[5]=P('Desligar cedo demais é pressa.','Tarde demais é teimosia.','<em>Na data combinada é método.</em>')
S[7]['lead']='No diagnóstico gratuito de 30 minutos, a gente combina com você o que medir, em quanto tempo e quem registra a venda.'
rep(d,'Com volume, o chute vira critério.','No fim do mês, você decide com número, não com palpite.')
rep(d,'Se quiser começar sabendo quando vai saber, comenta DIAGNÓSTICO.','Depois comenta DIAGNÓSTICO e a gente combina isso com você.')
save(f,d)

# C14: a pausa termina na garantia, que é o assunto do slide seguinte
f,d=load('14'); S=d['slides']
S[2]['itens'][0][1]='o certo é sim: conta, pixel e cartão seus'
S[4]=P('Ninguém controla tudo','entre o anúncio e a venda.','<em>Por isso, ninguém pode garantir.</em>')
rep(d,'Por isso garantia não é a pergunta certa. Processo é.','Por isso, ninguém pode garantir resultado. Quem garante está vendendo promessa.')
save(f,d)

# C15: gancho novo, "Nunca faça anúncio pago" + "se..."
f,d=load('15')
d['titulo']='Nunca faça anúncio pago se...'
d['slides']=[
 {'tipo':'capa','titulo':'Capa','texto':'Nunca faça <em>anúncio pago</em>','sub':'se a sua empresa ainda não está pronta para o cliente.'},
 T('Por quê','Por quê',['manchete','O anúncio só traz o cliente <em>até a porta.</em>'],
   ['corpo-suave','O que ele encontra depois decide se compra. Se encontra problema, você pagou para ele ir embora.']),
 L('Não está pronta se','Não está pronta se',[['A oferta','não cabe em uma frase'],['O Google e o perfil','parados, sem avaliação recente'],
   ['O WhatsApp','demora para responder'],['A margem','cada cliente custa mais do que deixa']],'Marcou um? <em>Arrume antes de anunciar.</em>'),
 P('Anúncio não conserta','o que vem depois dele.','<em>Só mostra mais rápido.</em>'),
 T('Quando está pronta','Quando está pronta',['manchete','Com os quatro em ordem, <em>anuncie.</em>'],
   ['corpo-suave','Oferta clara, resposta rápida, avaliação recente e margem com folga. Aí o anúncio acelera o que já funciona.']),
 {'tipo':'retrato','titulo':'Arthur','foto':'Foto do Arthur · P&amp;B','nome':'Quem diz isso sou eu, o <em>Arthur.</em>','cargo':'Fundador da Impulse',
  'corpo_suave':'Sim, eu vivo de anúncio pago.','corpo':'Por isso mesmo, prefiro adiar o seu a começar um que vai te frustrar.'},
 T('O que você leva','O que você leva',['manchete','Do diagnóstico, você sai sabendo <em>o que arrumar primeiro.</em>'],
   ['corpo-suave','Na ordem do que mais trava. Muita coisa você resolve sozinho, sem gastar nada com anúncio.']),
 {'tipo':'cta','titulo':'CTA','manchete':'Nunca faça anúncio pago antes da hora.','titulo2':'Descubra <em>se a sua já chegou.</em>',
  'lead':'No diagnóstico gratuito de 30 minutos, a gente confere os quatro pontos com você.','chave':'Comente <b>Diagnóstico</b>'}]
d['legenda']='\n\n'.join([
 'Nunca faça anúncio pago se a sua empresa ainda não está pronta para o cliente. Sim, quem diz isso vive de tráfego pago.',
 'O anúncio só traz o cliente até a porta. O que ele encontra depois decide se ele compra. Se encontra problema, você pagou para ele ir embora.',
 'Antes de anunciar, confira quatro pontos: a oferta cabe em uma frase? O seu Google e o seu perfil têm avaliação recente e post novo? O seu WhatsApp responde em minutos? Cada cliente deixa mais do que custa?',
 'Se algum falhou, arrume antes. Muita coisa você resolve sozinho, sem gastar nada com anúncio.',
 'Se os quatro estão em ordem, aí sim: anuncie. O anúncio acelera o que já funciona.',
 SEGUE_C,
 'Depois comenta DIAGNÓSTICO e a gente confere os quatro com você.'])
save(f,d)

# Ajustes de limite (40 palavras)
f,d=load('04'); d['slides'][4]['rotulo']='Antes de aumentar'; save(f,d)
f,d=load('08'); s=d['slides'][4]; s['rotulo']=s['titulo']='O que falta'
s['itens']=[['Custo por contato','quanto custa cada pessoa que chama'],['Contato que vira cliente','de cada dez, quantos compram'],
  ['Custo por cliente','verba dividida pelos clientes'],['Margem','o que sobra de cada cliente']]; save(f,d)
f,d=load('13'); s=d['slides'][3]
s['itens']=[['Semana um','mede do clique à venda'],['Semana dois','mostra o que traz contato'],['Semana três','separa o fraco do forte'],['Semana quatro','dá o primeiro custo por cliente']]
s['fecho']='Aí você decide <em>com número, não com palpite.</em>'; save(f,d)
f,d=load('14'); d['slides'][2]['itens'][0][1]='sim, com conta, pixel e cartão seus'; save(f,d)
