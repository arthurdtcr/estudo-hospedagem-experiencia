# 8ª refinação, carrosséis 1 a 5 (a partir do Juiz A, rodada 2)
import json, glob
def load(n): f=glob.glob(f'{n}-*/roteiro.json')[0]; return f, json.load(open(f))
def save(f,d): json.dump(d, open(f,'w'), ensure_ascii=False, indent=1)
def bloco(s, tipo, novo):
    for b in s['blocos']:
        if b[0]==tipo: b[1]=novo; return
    raise KeyError(tipo)

# C01
f,d=load('01'); S=d['slides']
S[3]['blocos']=[b for b in S[3]['blocos'] if b[0]!='titulo']+[['titulo','Às vezes é. Mas muitas vezes ele chegou até a <em>porta.</em>']]
S[4]['fecho']='Cada um custa <em>o clique que você pagou.</em>'
S[6]['lead']='Manda para quem anuncia e não sabe onde o cliente desiste.'
d['legenda']=d['legenda'].replace('Conhece alguém que ainda culpa o anúncio? Envia este post para ele.',
  'Conhece alguém que anuncia e não sabe onde o cliente desiste? Envia este post para ele.')
save(f,d)

# C02: a cena antes do dado; pausa quebrando o bloco de números
f,d=load('02'); S=d['slides']
S[1]['lead']='mais chance de virar conversa de verdade quando a resposta vem na primeira hora, e não na segunda.'
bloco(S[2],'corpo-suave','Em um dia, dá tempo de chamar o concorrente. E a vontade que o trouxe até você passa.')
S[3]['rotulo']=S[3]['titulo']='Quem responde rápido'
S[3]['nota']='23% nunca responderam. Teste com 2.241 empresas dos EUA, Harvard Business Review, 2011, antes do WhatsApp.'
capa,t7x,t60,t37,pausa,porque,lista,cta=S
d['slides']=[capa,porque,t7x,t60,pausa,t37,lista,cta]
d['legenda']=d['legenda'].replace('do que quem respondeu uma hora depois','do que quem respondeu na segunda hora')
save(f,d)

# C03: pausa antes das listas; slide do Luca mais leve; objeção da indicação
f,d=load('03'); S=d['slides']
S[1]['corpo']='Até quem chegou por indicação.'
S[2]['blocos']=[['manchete','Uma estrela a mais: de 5% a 9% <em>mais receita.</em>'],
  ['lead','Nos restaurantes independentes. Nas grandes redes, nenhum efeito.'],
  ['corpo','Rede famosa já chega com confiança. Negócio como o seu precisa provar.'],
  ['nota','Michael Luca, Harvard Business School, 2011. Yelp, Seattle.']]
capa,n97,luca,google,perfil,pausa,cta=S
d['slides']=[capa,n97,luca,pausa,google,perfil,cta]
d['legenda']=d['legenda'].replace('Pesquise hoje o nome',
  'Antes de mexer em qualquer anúncio de cliente, é isso que eu olho primeiro.\n\nPesquise hoje o nome')
save(f,d)

# C04: tira a repetição (3 e 5) e entra a fase de aprendizado (fato com fonte)
f,d=load('04'); S=d['slides']
bloco(S[1],'corpo-suave','A plataforma entrega primeiro para quem já estava quase comprando. Com mais verba, chega em quem nunca ouviu falar de você.')
S[2]['blocos']=[['manchete','Dobrar de uma vez faz o anúncio <em>reaprender.</em>'],
  ['corpo-suave','Mudança grande no orçamento devolve o conjunto de anúncios à fase de aprendizado. Por um tempo, a entrega oscila.'],
  ['nota','Central de Ajuda da Meta.']]
L=d['legenda']
L=L.replace('Dobrar a verba de tráfego pago quase nunca dobra as vendas.','Dobrar a verba de tráfego pago não costuma dobrar as vendas.')
L=L.replace('O segundo: quem chega de mais longe precisa de mais motivo para comprar. Oferta confusa, perfil fraco e resposta lenta já perdiam clientes. Com esse público mais frio, perdem ainda mais.',
  'O segundo: uma mudança grande no orçamento devolve o conjunto de anúncios da Meta à fase de aprendizado. Por um tempo, a entrega oscila.\n\nE quem chega de mais longe precisa de mais motivo para comprar. Oferta confusa, perfil fraco e resposta lenta já perdiam clientes. Com esse público mais frio, perdem ainda mais.')
d['legenda']=L
save(f,d)

# C05: sem sobreposição 3/4; fundador em uma voz só; CTA sem gancho de perda
f,d=load('05'); S=d['slides']
S[2]['itens'][1]=['A gente estuda antes','o que o seu cliente vê']
S[6]['nome']='Quem conduz sou eu, o <em>Arthur.</em>'
S[6]['corpo_suave']='Faço parte do Subido PRO, a mentoria do Pedro Sobral.'
S[6]['corpo']='Se eu não enxergar como ajudar, falo na hora.'
S[7]['lead']='Meia hora, direto comigo. Contratando ou não, o diagnóstico fica com você.'
d['legenda']=d['legenda'].replace('A pegadinha é que eu quero que você conheça o meu jeito de pensar. O resto é seu.',
  'A pegadinha é que eu quero que você conheça o meu jeito de pensar. O diagnóstico fica com você, contratando ou não.')
save(f,d)

# C01: slide 5 ficou com 41 palavras
f,d=load('01'); d['slides'][4]['itens'][2]=['No site','travou no celular']; save(f,d)
