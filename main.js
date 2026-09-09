/* =========================================================================
   ESTUDO: HOSPEDAGEM DE EXPERIENCIA
   Motor de movimento e interacao.

   Vocabulario fechado, quatro gestos e nada alem:
     1. revelacao de texto por linha, com mascara subindo por baixo
     2. parallax de imagem em tres camadas
     3. contadores numericos que sobem ao entrar na tela
     4. tracado de SVG desenhado conforme o scroll

   Regras que valem para o arquivo inteiro:
     - o conteudo existe e e legivel sem este script
     - prefers-reduced-motion desliga os quatro gestos, nunca a interacao
     - nada anima largura, altura ou posicao. So transform e opacity.
   ========================================================================= */

(function () {
  'use strict';

  document.documentElement.classList.add('js');

  var reduzir = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var temGSAP = typeof window.gsap !== 'undefined' && typeof window.ScrollTrigger !== 'undefined';
  var animar = temGSAP && !reduzir;

  if (temGSAP) gsap.registerPlugin(ScrollTrigger);

  /* -----------------------------------------------------------------------
     PRELOADER
     Teto real de 1,2s. Se os recursos vierem antes, sai antes. Preloader
     falso que segura o usuario e hostilidade.
     --------------------------------------------------------------------- */

  function preloader() {
    var el = document.querySelector('.preloader');
    if (!el) return Promise.resolve();

    var alvo = el.querySelector('.preloader__contador');
    if (reduzir) { el.hidden = true; return Promise.resolve(); }

    var TETO = 1200;
    var inicio = performance.now();
    var pronto = false;
    var quadro;

    window.addEventListener('load', function () { pronto = true; }, { once: true });

    return new Promise(function (resolve) {
      function passo(agora) {
        var decorrido = agora - inicio;
        var progresso = Math.min(1, decorrido / TETO);
        // quando os recursos chegam antes do teto, acelera para o fim
        if (pronto) progresso = Math.min(1, progresso + 0.35);
        if (alvo) alvo.textContent = Math.round(progresso * 100);

        if (progresso < 1) {
          quadro = requestAnimationFrame(passo);
          return;
        }
        cancelAnimationFrame(quadro);
        sair();
      }

      function sair() {
        if (!animar) { el.hidden = true; resolve(); return; }
        gsap.to(el, {
          yPercent: -100,
          duration: 0.56,
          ease: 'power4.inOut',
          onComplete: function () { el.hidden = true; }
        });
        // a cortina sobrepoe o primeiro gesto em 200ms, para nao existir
        // um vazio entre o preloader e o capitulo 1
        setTimeout(resolve, 360);
      }

      quadro = requestAnimationFrame(passo);
    });
  }

  /* -----------------------------------------------------------------------
     SCROLL SUAVE
     --------------------------------------------------------------------- */

  function scrollSuave() {
    if (!animar || typeof window.Lenis === 'undefined') return null;

    var lenis = new Lenis({
      duration: 1.1,
      easing: function (t) { return Math.min(1, 1.001 - Math.pow(2, -10 * t)); },
      smoothWheel: true,
      syncTouch: false
    });

    lenis.on('scroll', ScrollTrigger.update);
    gsap.ticker.add(function (t) { lenis.raf(t * 1000); });
    gsap.ticker.lagSmoothing(0);
    return lenis;
  }

  /* -----------------------------------------------------------------------
     GESTO 1: revelacao de texto por linha
     Envolve cada linha visual em .linha > span e sobe a partir de 105%.
     So em titulo e frase-tese. Aplicado a paragrafo corrido, o site pisca.
     --------------------------------------------------------------------- */

  function quebrarEmLinhas(el) {
    var texto = el.textContent.trim();
    var palavras = texto.split(/\s+/);
    el.textContent = '';

    var medidor = document.createElement('span');
    palavras.forEach(function (p, i) {
      var s = document.createElement('span');
      s.textContent = p;
      s.className = 'palavra';
      medidor.appendChild(s);
      if (i < palavras.length - 1) medidor.appendChild(document.createTextNode(' '));
    });
    el.appendChild(medidor);

    // agrupa por posicao vertical real, que e o unico jeito honesto de
    // saber onde o navegador quebrou a linha
    var linhas = [];
    var atual = null;
    var topoAtual = null;

    Array.prototype.forEach.call(medidor.querySelectorAll('.palavra'), function (p) {
      var topo = Math.round(p.offsetTop);
      if (topoAtual === null || Math.abs(topo - topoAtual) > 2) {
        topoAtual = topo;
        atual = [];
        linhas.push(atual);
      }
      atual.push(p.textContent);
    });

    el.textContent = '';
    var alvos = [];
    var caixas = [];
    linhas.forEach(function (palavrasDaLinha) {
      var wrap = document.createElement('span');
      wrap.className = 'linha';
      var inner = document.createElement('span');
      inner.textContent = palavrasDaLinha.join(' ');
      wrap.appendChild(inner);
      el.appendChild(wrap);
      alvos.push(inner);
      caixas.push(wrap);
    });

    return { alvos: alvos, caixas: caixas };
  }

  function gestoLinhas() {
    var elementos = document.querySelectorAll('[data-revelar]');
    if (!elementos.length) return;

    if (!animar) return; // o texto ja esta no DOM, legivel

    Array.prototype.forEach.call(elementos, function (el) {
      var r = quebrarEmLinhas(el);
      var alvos = r.alvos, caixas = r.caixas;
      if (!alvos.length) return;

      var heroi = el.classList.contains('display-hero');
      // 120 e nao 105: precisa cobrir o respiro de 0.14em que a mascara ganhou
      // para nao cortar a perna do g, senao vaza uma fresta durante a subida.
      gsap.set(alvos, { yPercent: 120, opacity: 0 });

      ScrollTrigger.create({
        trigger: el,
        start: 'top 82%',
        once: true,
        onEnter: function () {
          gsap.to(alvos, {
            yPercent: 0,
            opacity: 1,
            duration: 0.8,
            ease: 'expo.out',
            // o heroi tem tres linhas enormes e precisa de tempo de leitura
            stagger: heroi ? 0.18 : 0.09,
            // A mascara existe so para esconder a linha antes de ela subir.
            // Mantida depois do fim, ela corta a perna do g e do p, porque
            // a altura de linha e menor que 1. Some assim que cumpre a funcao.
            onComplete: function () {
              caixas.forEach(function (c) { c.style.overflow = 'visible'; });
            }
          });
        }
      });
    });
  }

  /* -----------------------------------------------------------------------
     GESTO 2: parallax em tres camadas
     Nunca mais que 26% de deslocamento, senao a foto sai do enquadramento.
     No celular cai para 60% do valor.
     --------------------------------------------------------------------- */

  function gestoParallax() {
    if (!animar) return;

    var estreito = window.matchMedia('(max-width: 767px)').matches;
    var f = estreito ? 0.6 : 1;

    Array.prototype.forEach.call(document.querySelectorAll('.palco'), function (palco) {
      var camadas = palco.querySelectorAll('.camada');
      var desloc = [-8, -16, -26];

      Array.prototype.forEach.call(camadas, function (camada, i) {
        gsap.to(camada, {
          yPercent: (desloc[i] || -12) * f,
          ease: 'none',
          scrollTrigger: {
            trigger: palco,
            start: 'top bottom',
            end: 'bottom top',
            scrub: 0.8,
            // will-change so enquanto ativo: tres camadas promovidas na GPU
            // de um celular intermediario derrubam a taxa de quadros
            onToggle: function (self) {
              camada.style.willChange = self.isActive ? 'transform' : 'auto';
            }
          }
        });
      });
    });
  }

  /* -----------------------------------------------------------------------
     GESTO 3: contadores
     1600ms e proposital. Rapido demais e o numero nao le como dado.
     O valor final ja esta no HTML, entao o dado existe sem JavaScript.
     --------------------------------------------------------------------- */

  function gestoContadores() {
    var alvos = document.querySelectorAll('[data-contar]');
    if (!alvos.length || !animar) return;

    Array.prototype.forEach.call(alvos, function (el) {
      var final = parseFloat(el.dataset.contar);
      if (isNaN(final)) return;

      var decimais = (el.dataset.decimais | 0);
      var prefixo = el.dataset.prefixo || '';
      var sufixo = el.dataset.sufixo || '';
      var estado = { v: 0 };

      // reserva a largura final para o rotulo abaixo nao pular a cada quadro
      el.style.minWidth = el.getBoundingClientRect().width + 'px';

      ScrollTrigger.create({
        trigger: el,
        start: 'top 85%',
        once: true,
        onEnter: function () {
          gsap.to(estado, {
            v: final,
            duration: 1.6,
            ease: 'power2.out',
            onUpdate: function () {
              el.textContent = prefixo + estado.v.toLocaleString('pt-BR', {
                minimumFractionDigits: decimais,
                maximumFractionDigits: decimais
              }) + sufixo;
            }
          });
        }
      });
    });
  }

  /* -----------------------------------------------------------------------
     GESTO 4: tracado de SVG
     stroke-dasharray medido com getTotalLength, nunca chumbado.
     --------------------------------------------------------------------- */

  function gestoTracado() {
    var paths = document.querySelectorAll('[data-tracar]');
    if (!paths.length || !animar) return;

    /* O COMPRIMENTO TEM QUE SER MEDIDO NO ESPACO CERTO

       Com vector-effect="non-scaling-stroke", que e o que mantem a linha com
       2,5px em qualquer tela, o tracejado passa a ser medido em pixel de
       tela. So que getTotalLength() devolve unidade do viewBox, e as duas
       coisas so batem quando o SVG e desenhado no tamanho exato do viewBox.

       Aqui nao e: o viewBox tem 800 e o SVG desenha a 1088, escala 1,36. A
       linha tem 890 de viewBox, ou seja 1210px reais, e o dash mandava 890.
       Sobravam 320px, 26% do fim da linha, que nunca apareciam por mais que
       se rolasse. O ultimo degrau ficava sempre pela metade.

       Medir na tela resolve, e mantem a espessura constante. */
    function medidaDoTraco(path) {
      var comprimento = path.getTotalLength();
      var svg = path.ownerSVGElement;
      var caixa = svg && svg.viewBox && svg.viewBox.baseVal;
      if (!caixa || !caixa.width) return comprimento;

      var naTela = svg.getBoundingClientRect().width;
      if (!naTela) return comprimento;

      var semEscala = path.getAttribute('vector-effect') === 'non-scaling-stroke' ||
                      window.getComputedStyle(path).vectorEffect === 'non-scaling-stroke';

      return semEscala ? comprimento * (naTela / caixa.width) : comprimento;
    }

    Array.prototype.forEach.call(paths, function (path) {
      /* Arma o tracejado e devolve o ponto de partida. Uma funcao so para as
         duas coisas, porque elas precisam ser sempre o mesmo numero. O
         invalidateOnRefresh chama isto de novo quando a janela muda de
         largura, e a escala junto. */
      function armar() {
        var comprimento = medidaDoTraco(path);
        gsap.set(path, { strokeDasharray: comprimento });
        return comprimento;
      }

      armar();

      /* O gatilho e a figura, nunca a secao.

         Com a secao inteira como gatilho, o traco se distribui por titulo,
         diagrama, quatro degraus e cinco paragrafos. O grafico fica no topo
         dessa altura toda, entao ele sai da tela com a linha pela metade e
         nunca se ve a escada chegar no ultimo degrau. Amarrado a figura, o
         traco comeca quando ela entra e fecha antes de ela sair. */
      var alvo = path.closest('figure') || path.closest('section') || path;

      gsap.fromTo(path,
        { strokeDashoffset: function () { return armar(); } },
        {
          strokeDashoffset: 0,
          ease: 'none',
          scrollTrigger: {
            trigger: alvo,
            start: 'top 85%',
            end: 'bottom 75%',
            scrub: 0.6,
            invalidateOnRefresh: true
          }
        }
      );
    });
  }

  /* -----------------------------------------------------------------------
     GESTO 5: a imagem abre de um quadro estreito para a sangria total
     Herdado das referencias. So clip-path e transform, nada de layout.
     Sem JavaScript a imagem ja nasce aberta, entao nada se perde.
     --------------------------------------------------------------------- */

  function gestoAberturaDeImagem() {
    var figs = document.querySelectorAll('[data-abrir]');
    if (!figs.length || !animar) return;

    var estreito = window.matchMedia('(max-width: 767px)').matches;
    // no celular a abertura e menor: com pouca largura, recorte grande
    // some com a foto antes de ela ser reconhecivel
    var recorte = estreito ? 10 : 19;

    Array.prototype.forEach.call(figs, function (fig) {
      gsap.set(fig, { clipPath: 'inset(0% ' + recorte + '% 0% ' + recorte + '%)' });

      var tl = gsap.timeline({
        scrollTrigger: {
          trigger: fig,
          start: 'top 95%',
          end: 'top 35%',
          scrub: 0.7,
          onToggle: function (self) {
            fig.style.willChange = self.isActive ? 'clip-path' : 'auto';
          }
        }
      });

      tl.to(fig, { clipPath: 'inset(0% 0% 0% 0%)', ease: 'none' }, 0);
    });
  }

  /* -----------------------------------------------------------------------
     GESTO 6: zoom na entrada e afastamento na saida
     A foto entra grande e assenta ate a escala real no meio da tela.
     Depois recua e escurece, como se saisse de cena para tras.
     E o que faz a imagem parecer viva durante a passagem toda, e nao so
     no instante em que aparece.
     --------------------------------------------------------------------- */

  function gestoZoomEAfastamento() {
    if (!animar) return;

    var estreito = window.matchMedia('(max-width: 767px)').matches;
    var entrada = estreito ? 1.12 : 1.20;   // no celular a foto e menor, zoom forte distorce
    var saida   = estreito ? 0.97 : 0.93;

    Array.prototype.forEach.call(document.querySelectorAll('.palco'), function (palco) {
      var img = palco.querySelector('.camada img');
      if (!img) return;

      var heroi = palco.id === 'capitulo-1';

      var tl = gsap.timeline({
        scrollTrigger: {
          trigger: palco,
          start: heroi ? 'top top' : 'top bottom',
          end: 'bottom top',
          scrub: 0.9,
          onToggle: function (self) {
            img.style.willChange = self.isActive ? 'transform' : 'auto';
          }
        }
      });

      if (heroi) {
        // o heroi ja esta na tela ao carregar: so abre, nunca recua
        gsap.set(img, { scale: entrada });
        tl.to(img, { scale: 1.02, ease: 'none' }, 0);
      } else {
        gsap.set(img, { scale: entrada });
        tl.to(img, { scale: 1, ease: 'none', duration: 0.55 }, 0)
          .to(img, { scale: saida, opacity: 0.72, ease: 'none', duration: 0.45 }, 0.55);
      }
    });
  }

  /* -----------------------------------------------------------------------
     GESTO 7: revelacao palavra por palavra
     Reservado as frases-chave. Aplicado a texto corrido, o site inteiro
     pisca e a leitura fica pior, nao melhor.
     --------------------------------------------------------------------- */

  function gestoPalavras() {
    var alvos = document.querySelectorAll('[data-palavras]');
    if (!alvos.length || !animar) return;

    Array.prototype.forEach.call(alvos, function (el) {
      // guarda a palavra em ambar ANTES de desmontar, senao o destaque some
      // e a regra da cor unica por capitulo se perde
      var ambar = {};
      Array.prototype.forEach.call(el.querySelectorAll('.ambar'), function (a) {
        a.textContent.trim().split(/\s+/).forEach(function (p) { ambar[p] = true; });
      });

      var texto = el.textContent.trim();
      var partes = texto.split(/\s+/);
      if (partes.length > 40) return; // frase longa demais, nao vale o custo

      el.textContent = '';
      var palavras = [];
      partes.forEach(function (p, i) {
        var caixa = document.createElement('span');
        caixa.className = 'palavra-caixa';
        var dentro = document.createElement('span');
        // a pontuacao gruda na palavra, entao compara sem ela
        if (ambar[p.replace(/[.,:;!?]+$/, '')]) dentro.className = 'ambar';
        dentro.textContent = p;
        caixa.appendChild(dentro);
        el.appendChild(caixa);
        if (i < partes.length - 1) el.appendChild(document.createTextNode(' '));
        palavras.push(dentro);
      });

      gsap.set(palavras, { yPercent: 110, opacity: 0 });

      ScrollTrigger.create({
        trigger: el,
        start: 'top 88%',
        once: true,
        onEnter: function () {
          gsap.to(palavras, {
            yPercent: 0,
            opacity: 1,
            duration: 0.62,
            ease: 'expo.out',
            stagger: 0.035,
            onComplete: function () {
              // solta o corte, senao a perna do g fica presa como antes
              Array.prototype.forEach.call(el.querySelectorAll('.palavra-caixa'), function (c) {
                c.style.overflow = 'visible';
              });
            }
          });
        }
      });
    });
  }

  /* -----------------------------------------------------------------------
     GESTO 8: REVELACAO DO CAPITULO 10
     O oitavo gesto, e o unico que quebra a regra dos sete. Existe porque a
     abertura do capitulo da pratica e o ponto em que o estudo vira peca, e
     o corte de escuro para claro precisa de um movimento a altura.

     Tres estagios, todos presos ao scroll, nenhum em tempo fixo:
       0,0 a 1,0  a foto se desfaz em barras verticais e some
       0,8 a 1,7  entram selo, titulo e a linha seca
       1,5 a 3,2  entram as tres cartas, uma atras da outra

     Acima de 1024px a secao fica fixa durante os tres. Abaixo nao fixa
     nada: tres cartas mais titulo nao cabem em 100svh de celular, e prender
     a tela de quem le em pe, no WhatsApp, e o oposto do que este site quer.
     --------------------------------------------------------------------- */

  function gestoRevelacao() {
    var secao = document.querySelector('[data-revelacao]');
    if (!secao || !animar) return;

    var palco = secao.querySelector('.revelacao__palco');
    var hero = secao.querySelector('.revelacao__hero');
    var foto = hero && hero.querySelector('img');
    if (!palco || !hero || !foto) return;

    var veu = secao.querySelector('.revelacao__veu');
    var cabeca = secao.querySelectorAll('.revelacao__selo, .revelacao__titulo, .revelacao__linha');
    var cartas = secao.querySelectorAll('.carta');

    /* O VEU NAO PODE DEPENDER DE ONDE O SCROLLTRIGGER ACHA QUE A SECAO ESTA

       A primeira versao acendia e apagava o veu num gatilho proprio, de
       'top bottom' ate 'top top'. So que essa conta usa a posicao medida da
       secao, e e exatamente ela que sai do lugar quando a pagina cresce
       depois do carregamento. Resultado: o veu fazia a passagem inteira com
       a secao ainda abaixo da janela, e quando a foto finalmente chegava na
       tela ela ja estava acesa. Continuava aparecendo de uma vez.

       Agora o veu nasce opaco e so abre dentro do trecho fixado, que e um
       intervalo consistente consigo mesmo. Antes do pin a tela mostra
       carvao, o mesmo do capitulo 9, entao nao existe emenda visivel. Se a
       medida errar, o pior caso e a tela ficar escura um pouco antes da
       hora, nunca a foto saltar pronta. */
    function prepararEntrada() {
      if (veu) gsap.set(veu, { opacity: 1 });
      gsap.set(hero, { scale: 1.06, transformOrigin: '50% 50%' });
    }

    /* Larguras irregulares, em peso. Sequencia fixa e nao aleatoria: o
       efeito precisa ser o mesmo em toda visita, senao nao da para ajustar
       nem para reproduzir um defeito. */
    var PESOS = [7, 4, 11, 6, 9, 5, 13, 4, 8, 6, 10, 5, 7, 5];

    /* ---- O UNICO NUMERO PARA MEXER NO RITMO ----
       Quantas telas de rolagem os tres estagios ocupam. Maior deixa tudo
       mais lento, menor mais rapido, e a proporcao entre os estagios nao
       muda porque a linha do tempo inteira e esticada junto.
       380 era rapido demais. */
    var TELAS_DE_ROLAGEM = 600;

    function montaBarras(quantidade) {
      var antigas = hero.querySelectorAll('.revelacao__barra');
      Array.prototype.forEach.call(antigas, function (b) { b.remove(); });

      var pesos = PESOS.slice(0, quantidade);
      var total = pesos.reduce(function (a, b) { return a + b; }, 0);
      var url = foto.getAttribute('src');
      var esquerda = 0;
      var barras = [];

      pesos.forEach(function (peso) {
        var largura = peso / total * 100;

        var barra = document.createElement('div');
        barra.className = 'revelacao__barra';
        barra.style.left = esquerda + '%';
        /* 1px a mais para a barra encostar na vizinha. Como a fatia se mede
           em cqw, esse pixel extra so repete o pixel do lado, e a costura
           de subpixel some sem a foto sair do lugar. */
        barra.style.width = 'calc(' + largura + '% + 1px)';

        var fatia = document.createElement('div');
        fatia.className = 'revelacao__fatia';
        fatia.style.left = (-esquerda) + 'cqw';
        fatia.style.setProperty('--foto', 'url("' + url + '")');

        barra.appendChild(fatia);
        hero.appendChild(barra);
        barras.push(barra);
        esquerda += largura;
      });

      return barras;
    }

    function limpa(barras) {
      Array.prototype.forEach.call(barras, function (b) { b.remove(); });
      gsap.set(cabeca, { clearProps: 'all' });
      gsap.set(cartas, { clearProps: 'all' });
      if (veu) gsap.set(veu, { clearProps: 'all' });
      gsap.set(hero, { clearProps: 'all' });
    }

    ScrollTrigger.matchMedia({

      '(min-width: 1024px)': function () {
        secao.classList.add('js-revelacao-ativa');
        var barras = montaBarras(14);
        prepararEntrada();

        gsap.set(cabeca, { yPercent: 40, opacity: 0 });
        gsap.set(cartas, { y: 60, opacity: 0 });

        /* pausada na criacao: linha do tempo solta comeca a tocar sozinha no
           tique seguinte, e quem manda nela aqui e o scroll */
        var linha = gsap.timeline({ paused: true });

        /* estagio 0: a foto nasce do escuro. E o primeiro movimento depois
           que a tela trava, e nao um quarto de tempo parado: o compasso de
           espera agora e o proprio veu abrindo devagar. */
        linha.to(veu, {
          opacity: 0, ease: 'power2.in', duration: 0.55
        }, 0);
        linha.to(hero, {
          scale: 1, ease: 'none', duration: 0.85
        }, 0);

        // a foto inteira e parada, antes de se desfazer
        linha.to({}, { duration: 0.3 }, 0.55);

        // estagio 1: barras alternam para cima e para baixo enquanto somem
        linha.to(barras, {
          yPercent: function (i) { return i % 2 === 0 ? -108 : 108; },
          opacity: 0,
          ease: 'power2.inOut',
          duration: 1.1,
          stagger: { each: 0.045, from: 'edges' }
        }, 0.85);

        // estagio 2
        linha.to(cabeca, {
          yPercent: 0, opacity: 1, ease: 'expo.out', duration: 0.9, stagger: 0.12
        }, 1.75);

        // estagio 3
        linha.to(cartas, {
          y: 0, opacity: 1, ease: 'expo.out', duration: 0.9, stagger: 0.42
        }, 2.5);

        /* Compasso de saida. Sem ele a ultima carta assenta no mesmo ponto
           em que o pin solta, e a tela destrava em cima do movimento. */
        linha.to({}, { duration: 0.55 }, 4);

        var st = ScrollTrigger.create({
          trigger: secao,
          start: 'top top',
          end: '+=' + TELAS_DE_ROLAGEM + '%',
          pin: palco,
          scrub: 0.6,
          animation: linha,
          invalidateOnRefresh: true,
          /* Depois do trilho do capitulo 4, que esta acima na pagina e cujo
             espacador desloca esta secao inteira. Declarado mesmo sendo o
             menor: e o que faz o ScrollTrigger ordenar a remedida em vez de
             usar a ordem em que os gatilhos foram criados.
             Ver PRIORIDADE DE MEDIDA, no fim deste arquivo. */
          refreshPriority: 1
          /* sem anticipatePin: ele fixa alguns pixels antes da conta e, num
             bloco de tela cheia, esse adiantamento aparece como salto */
        });

        return function () {
          secao.classList.remove('js-revelacao-ativa');
          st.kill();
          linha.kill();
          limpa(barras);
        };
      },

      '(max-width: 1023px)': function () {
        /* Sem fixar. As barras se desfazem enquanto a faixa cruza a tela.

           A classe e outra, de proposito. A do desktop carrega junto altura
           de tela cheia e hero fora do fluxo, que no celular nao servem. O
           que as duas precisam dividir e uma coisa so: apagar a foto de
           base. Sem isso as barras animam POR CIMA dela, cada uma com a
           mesma foto dentro, e o que aparece sao copias deslocadas da
           imagem sobre ela mesma. Alem de parecer defeito, a dissolucao
           nao acontece: as barras saem e revelam a mesma foto que ja
           estava ali. Com a foto de base apagada elas revelam o creme, que
           e o fundo do capitulo, e a faixa escura se desfaz na pagina
           clara. E a mesma ideia do desktop, na escala do celular. */
        secao.classList.add('js-revelacao-movel');
        var barras = montaBarras(7);

        var st1 = gsap.to(barras, {
          yPercent: function (i) { return i % 2 === 0 ? -108 : 108; },
          opacity: 0,
          ease: 'none',
          stagger: { each: 0.05, from: 'edges' },
          scrollTrigger: {
            /* O gatilho e a secao, nao o hero. O hero agora e sticky, e a
               caixa de um elemento sticky muda de lugar sozinha conforme
               ele gruda e desgruda: medir por ele devolve numero que anda.
               A secao fica parada, entao a conta e estavel. */
            trigger: secao,
            start: 'top top',
            /* Faixa larga pelo mesmo motivo do desktop: em curso curto a
               dissolucao passa antes de o olho registrar que era uma foto.
               Como o conteudo corre por tras enquanto isso, e essa largura
               que faz o titulo e a primeira carta atravessarem a foto ainda
               se desfazendo, em vez de chegarem numa tela ja limpa. */
            end: '+=180%',
            scrub: 0.5,
            invalidateOnRefresh: true
          }
        });

        gsap.set(cartas, { y: 40, opacity: 0 });
        var st2 = gsap.to(cartas, {
          y: 0, opacity: 1, ease: 'expo.out', duration: 0.7, stagger: 0.16,
          scrollTrigger: { trigger: secao.querySelector('.revelacao__cartas'), start: 'top 85%', once: true }
        });

        return function () {
          secao.classList.remove('js-revelacao-movel');
          [st1, st2].forEach(function (t) {
            t.scrollTrigger && t.scrollTrigger.kill();
            t.kill();
          });
          limpa(barras);
        };
      }

    });
  }

  /* -----------------------------------------------------------------------
     TRILHO HORIZONTAL
     Acima de 1024px o ScrollTrigger fixa a secao e empurra os paineis.
     Abaixo, o mesmo HTML vira empilhamento vertical. Nenhum no e movido.
     --------------------------------------------------------------------- */

  function trilhoHorizontal() {
    var secao = document.querySelector('[data-trilho]');
    if (!secao || !animar) return;

    var trilho = secao.querySelector('.trilho');
    if (!trilho) return;

    ScrollTrigger.matchMedia({
      '(min-width: 1024px)': function () {
        secao.classList.add('js-trilho-ativo');

        /* Medido por funcao, nao por valor fixo. Guardado numa variavel, o
           espacador deste pin congela com a medida do primeiro instante, e
           como ele fica antes do capitulo 10, qualquer erro aqui desloca a
           secao fixada de la inteira. Com funcao, o invalidateOnRefresh
           recalcula de verdade. */
        var medir = function () { return trilho.scrollWidth - trilho.clientWidth; };
        if (medir() <= 0) return;

        var tween = gsap.to(trilho, {
          x: function () { return -medir(); },
          ease: 'none',
          scrollTrigger: {
            trigger: secao,
            start: 'top top',
            end: function () { return '+=' + medir(); },
            pin: true,
            scrub: 0.6,
            invalidateOnRefresh: true,
            /* Este pin tem que ser remedido ANTES do pin do capitulo 10.
               Ele fica antes na pagina e o espacador dele empurra tudo que
               vem depois. Medido fora de ordem, o capitulo 10 trava 1184px
               cedo demais, que e exatamente a distancia deste trilho.
               Numero maior e remedido primeiro. Ver PRIORIDADE DE MEDIDA. */
            refreshPriority: 2
          }
        });

        return function () {
          secao.classList.remove('js-trilho-ativo');
          gsap.set(trilho, { x: 0 });
          tween.scrollTrigger && tween.scrollTrigger.kill();
          tween.kill();
        };
      }
    });
  }

  /* -----------------------------------------------------------------------
     INTERACAO
     Tudo abaixo funciona com movimento reduzido. Retorno de estado nao e
     decoracao, entao nunca e desligado.
     --------------------------------------------------------------------- */

  function acordeao() {
    Array.prototype.forEach.call(document.querySelectorAll('.acordeao__gatilho'), function (b) {
      b.addEventListener('click', function () {
        var aberto = b.getAttribute('aria-expanded') === 'true';
        b.setAttribute('aria-expanded', String(!aberto));
      });
    });
  }

  /* O "+" das cartas do capitulo 10. Nao abre janela nem dialogo: o resumo
     ja esta no HTML, dentro da propria carta, e o botao so troca o estado.
     Sem foco preso, sem rolagem travada, sem nada para fechar com Escape
     alem do proprio botao. Abrir um resumo fecha os outros dois, senao as
     tres fotos somem atras de texto ao mesmo tempo. */
  function resumoDasCartas() {
    var botoes = document.querySelectorAll('.carta__mais');

    Array.prototype.forEach.call(botoes, function (b) {
      b.addEventListener('click', function () {
        var abrindo = b.getAttribute('aria-expanded') !== 'true';
        Array.prototype.forEach.call(botoes, function (outro) {
          outro.setAttribute('aria-expanded', String(outro === b && abrindo));
        });
      });
    });
  }

  /* -----------------------------------------------------------------------
     PAINEL DE DIAGNOSTICO

     So existe com ?debug na URL. Nenhum visitante ve isto, e por isso ele
     pode ficar no arquivo sem atrapalhar. Existe porque a aba em segundo
     plano mente sobre tudo que importa aqui, e sem numeros da tela de quem
     esta olhando eu corrijo no escuro.

     Uso: abrir o site com ?debug=1 e capturar a tela no momento do defeito.
     --------------------------------------------------------------------- */

  function painelDeDiagnostico() {
    if (window.location.search.indexOf('debug') < 0) return;

    var p = document.createElement('div');
    p.style.cssText =
      'position:fixed;left:8px;top:8px;z-index:9999;background:rgba(0,0,0,.86);' +
      'color:#7CFC7C;font:11px/1.55 ui-monospace,monospace;padding:9px 11px;' +
      'white-space:pre;pointer-events:none;letter-spacing:.02em';
    document.body.appendChild(p);

    function pinta() {
      var sec = document.querySelector('[data-revelacao]');
      var palco = document.querySelector('.revelacao__palco');
      var veu = document.querySelector('.revelacao__veu');
      var hero = document.querySelector('.revelacao__hero');

      var st = null;
      if (temGSAP && palco) {
        st = ScrollTrigger.getAll().filter(function (t) { return t.pin === palco; })[0];
      }

      var topoReal = sec ? Math.round(sec.getBoundingClientRect().top + window.scrollY) : -1;
      var texto = '';
      texto += 'janela      ' + window.innerWidth + ' x ' + window.innerHeight + '\n';
      texto += 'scrollY     ' + Math.round(window.scrollY) + '\n';
      texto += 'gsap        ' + temGSAP + '   animar ' + animar + '\n';
      texto += 'classe      ' + (sec ? sec.classList.contains('js-revelacao-ativa') : 'sem secao') + '\n';
      texto += 'barras      ' + document.querySelectorAll('.revelacao__barra').length + '\n';
      texto += 'topo real   ' + topoReal + '\n';

      if (st) {
        texto += 'pin start   ' + Math.round(st.start) + '\n';
        texto += 'pin end     ' + Math.round(st.end) + '\n';
        texto += 'ERRO MEDIDA ' + (topoReal - Math.round(st.start)) + ' px\n';
        texto += 'progresso   ' + st.progress.toFixed(3) + '\n';
        texto += 'palco pos   ' + window.getComputedStyle(palco).position + '\n';
      } else {
        texto += 'PIN         nao existe\n';
      }

      texto += 'veu opac    ' + (veu ? window.getComputedStyle(veu).opacity : 'sem veu') + '\n';
      texto += 'hero transf ' + (hero ? window.getComputedStyle(hero).transform.slice(0, 26) : 'sem hero');

      p.textContent = texto;
      requestAnimationFrame(pinta);
    }

    pinta();
  }

  /* -----------------------------------------------------------------------
     GRAFICO DO RISCO, capitulo 5

     O diagrama e a lista de degraus abaixo dele dizem a mesma coisa em dois
     formatos. Aqui os dois passam a se apontar: mirar numa faixa do grafico
     acende o bloco de texto que a explica, e o contrario tambem.

     Faixa larga em vez de ponto: acertar um circulo de 5px com o dedo nao
     acontece. Cada alvo cobre a coluna inteira do grafico.

     Funciona com movimento reduzido, porque retorno de estado nao e
     decoracao. So depende de JavaScript, e sem ele o texto dos degraus
     continua inteiro logo abaixo.
     --------------------------------------------------------------------- */

  function graficoDoRisco() {
    var figura = document.querySelector('[data-risco]');
    if (!figura) return;

    var lista = document.querySelector('.degraus');
    var detalhes = figura.querySelectorAll('[data-detalhe]');
    var alvos = figura.querySelectorAll('[data-faixa]');
    var degraus = lista ? lista.querySelectorAll('[data-degrau]') : [];
    if (!detalhes.length || !lista) return;

    function acende(indice) {
      Array.prototype.forEach.call(detalhes, function (d) {
        if (d.getAttribute('data-detalhe') === String(indice)) {
          d.setAttribute('data-ativo', '');
        } else {
          d.removeAttribute('data-ativo');
        }
      });

      Array.prototype.forEach.call(degraus, function (l) {
        if (l.getAttribute('data-degrau') === String(indice)) {
          l.setAttribute('data-ativo', '');
        } else {
          l.removeAttribute('data-ativo');
        }
      });

      if (indice === null) {
        lista.removeAttribute('data-algum-ativo');
      } else {
        lista.setAttribute('data-algum-ativo', '');
      }
    }

    function apaga() { acende(null); }

    function liga(el, indice) {
      el.addEventListener('mouseenter', function () { acende(indice); });
      el.addEventListener('focus', function () { acende(indice); });
      el.addEventListener('blur', apaga);
      // no toque nao existe mouseleave: o proximo toque troca, e sair do
      // grafico apaga
      el.addEventListener('touchstart', function () { acende(indice); }, { passive: true });
    }

    Array.prototype.forEach.call(alvos, function (r) {
      liga(r, Number(r.getAttribute('data-faixa')));
    });
    Array.prototype.forEach.call(degraus, function (l) {
      liga(l, Number(l.getAttribute('data-degrau')));
    });

    figura.addEventListener('mouseleave', apaga);
    lista.addEventListener('mouseleave', apaga);
  }

  function equacao() {
    Array.prototype.forEach.call(document.querySelectorAll('.variavel'), function (b) {
      function abrir() { b.setAttribute('aria-expanded', 'true'); }
      function fechar() { b.setAttribute('aria-expanded', 'false'); }
      b.addEventListener('mouseenter', abrir);
      b.addEventListener('mouseleave', fechar);
      b.addEventListener('focus', abrir);
      b.addEventListener('blur', fechar);
      b.addEventListener('click', function () {
        b.setAttribute('aria-expanded', String(b.getAttribute('aria-expanded') !== 'true'));
      });
    });
  }

  function alternador() {
    Array.prototype.forEach.call(document.querySelectorAll('[data-alternador]'), function (grupo) {
      var botoes = grupo.querySelectorAll('.alternador__botao');
      Array.prototype.forEach.call(botoes, function (b) {
        b.addEventListener('click', function () {
          Array.prototype.forEach.call(botoes, function (o) {
            var ativo = o === b;
            o.setAttribute('aria-selected', String(ativo));
            var painel = document.getElementById(o.getAttribute('aria-controls'));
            if (painel) painel.hidden = !ativo;
          });
        });
      });
    });
  }

  function diagnostico() {
    var raiz = document.querySelector('.diagnostico');
    if (!raiz) return;

    var placarNum = raiz.querySelector('.placar__numero');
    var placarTxt = raiz.querySelector('.placar__texto');
    var leituras = placarTxt ? JSON.parse(placarTxt.dataset.faixas || '[]') : [];
    var respostas = {};

    function atualizar() {
      var sims = 0;
      var total = raiz.querySelectorAll('.pergunta').length;
      Object.keys(respostas).forEach(function (k) { if (respostas[k] === 'sim') sims++; });

      if (placarNum) placarNum.textContent = sims + ' de ' + total;
      if (placarTxt && leituras.length) {
        var faixa = leituras.find(function (f) { return sims >= f.min && sims <= f.max; });
        if (faixa) placarTxt.textContent = faixa.texto;
      }
    }

    Array.prototype.forEach.call(raiz.querySelectorAll('.pergunta'), function (p, i) {
      Array.prototype.forEach.call(p.querySelectorAll('.pergunta__botao'), function (b) {
        b.addEventListener('click', function () {
          var valor = b.dataset.resposta;
          respostas[i] = valor;
          Array.prototype.forEach.call(p.querySelectorAll('.pergunta__botao'), function (o) {
            o.setAttribute('aria-pressed', String(o === b));
          });
          // a leitura construtiva so aparece quando ele responde nao
          p.classList.toggle('esta-aberta', valor === 'nao');
          atualizar();
        });
      });
    });

    atualizar();
  }

  /* -----------------------------------------------------------------------
     PROGRESSO E MEDICAO
     --------------------------------------------------------------------- */

  function progresso() {
    var barra = document.querySelector('.progresso');
    if (!barra || !animar) return;

    gsap.to(barra, {
      scaleX: 1,
      ease: 'none',
      scrollTrigger: { trigger: document.body, start: 'top top', end: 'bottom bottom', scrub: 0.3 }
    });
  }

  function medirLeitura() {
    var marcos = [25, 50, 75, 100];
    var disparados = {};

    function envia(pct) {
      if (typeof window.fbq === 'function') {
        window.fbq('trackCustom', 'LeituraEstudo', { profundidade: pct });
      }
      if (typeof window.dataLayer !== 'undefined') {
        window.dataLayer.push({ event: 'leitura_estudo', profundidade: pct });
      }
    }

    function checar() {
      var alturaDoc = document.documentElement.scrollHeight - window.innerHeight;
      if (alturaDoc <= 0) return;
      var pct = Math.round((window.scrollY / alturaDoc) * 100);
      marcos.forEach(function (m) {
        if (pct >= m && !disparados[m]) { disparados[m] = true; envia(m); }
      });
    }

    window.addEventListener('scroll', checar, { passive: true });
    checar();
  }

  /* Repassa o UTM do link para o WhatsApp, para o follow-up saber quem abriu */
  function marcarWhatsapp() {
    var params = new URLSearchParams(window.location.search);
    var origem = params.get('utm_content') || params.get('utm_source');
    if (!origem) return;

    Array.prototype.forEach.call(document.querySelectorAll('a[href*="wa.me"]'), function (a) {
      try {
        var url = new URL(a.href);
        var texto = url.searchParams.get('text') || '';
        url.searchParams.set('text', texto + '\n\n[' + origem + ']');
        a.href = url.toString();
      } catch (e) { /* link malformado, deixa como esta */ }
    });
  }

  /* -----------------------------------------------------------------------
     REDE DE SEGURANCA
     Texto escondido esperando um gatilho que nunca chega e o pior defeito
     possivel aqui: o prospect abre o link e a pagina esta vazia. Passados
     alguns segundos, tudo que ainda estiver invisivel aparece na marra.
     --------------------------------------------------------------------- */

  function redeDeSeguranca() {
    if (!animar) return;

    setTimeout(function () {
      var presos = document.querySelectorAll('.linha > span, .palavra-caixa > span');
      var soltos = 0;

      Array.prototype.forEach.call(presos, function (s) {
        if (parseFloat(getComputedStyle(s).opacity) < 0.9) {
          var r = s.getBoundingClientRect();
          // so resgata o que ja passou pela tela: o resto ainda vai animar normal
          if (r.top < window.innerHeight * 1.2) {
            gsap.set(s, { yPercent: 0, opacity: 1 });
            soltos++;
          }
        }
      });

      Array.prototype.forEach.call(document.querySelectorAll('[data-abrir]'), function (f) {
        var c = getComputedStyle(f).clipPath;
        if (c && c !== 'none' && f.getBoundingClientRect().top < window.innerHeight) {
          gsap.set(f, { clipPath: 'inset(0% 0% 0% 0%)' });
        }
      });

      if (soltos) console.log('[estudo] rede de seguranca liberou ' + soltos + ' trechos');
    }, 5000);
  }

  /* -----------------------------------------------------------------------
     PARTIDA
     --------------------------------------------------------------------- */

  function iniciar() {
    acordeao();
    resumoDasCartas();
    graficoDoRisco();
    painelDeDiagnostico();
    equacao();
    alternador();
    diagnostico();
    marcarWhatsapp();
    medirLeitura();

    preloader().then(function () {
      scrollSuave();
      gestoLinhas();
      gestoParallax();
      gestoContadores();
      gestoTracado();
      gestoAberturaDeImagem();
      gestoZoomEAfastamento();
      gestoPalavras();
      /* Os dois que fixam a tela entram na ordem em que aparecem na pagina:
         trilho e o capitulo 4, revelacao e o capitulo 10. A ordem de criacao
         e o criterio de desempate do ScrollTrigger, entao criar o de baixo
         primeiro fazia o capitulo 10 ser medido antes de o espacador do
         trilho existir. Ver PRIORIDADE DE MEDIDA, no fim deste arquivo. */
      trilhoHorizontal();
      gestoRevelacao();
      progresso();
      redeDeSeguranca();
      if (temGSAP) ScrollTrigger.refresh();
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', iniciar);
  } else {
    iniciar();
  }

  // fontes chegando depois mudam a quebra de linha e a altura das secoes
  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(function () { if (temGSAP) ScrollTrigger.refresh(); });
  }

  /* -----------------------------------------------------------------------
     IMAGEM QUE CHEGA DEPOIS MOVE TUDO QUE VEM ABAIXO

     Com loading="lazy" a imagem so baixa quando o scroll se aproxima, e cada
     uma que assenta empurra o resto da pagina para baixo. O ScrollTrigger
     mediu start e end uma vez, no comeco, e nao remede sozinho.

     O estrago aparece longe da causa: a secao fixada do capitulo 10 travava
     1147px antes do lugar, ou seja, ainda dentro do capitulo 9. Dava a
     impressao de que a tela cortava do nada na entrada, e de que soltava
     numa tela clara sem motivo na saida. Nao era o gesto, era a medida.
     --------------------------------------------------------------------- */

  if (temGSAP) {
    var pedido;
    var remedir = function () {
      clearTimeout(pedido);
      // agrupa varias imagens que chegam juntas num refresh so
      pedido = setTimeout(function () { ScrollTrigger.refresh(); }, 140);
    };

    Array.prototype.forEach.call(document.images, function (img) {
      if (img.complete) return;
      img.addEventListener('load', remedir, { once: true });
      img.addEventListener('error', remedir, { once: true });
    });

    // rede final: o load pega o que escapou de fonte, imagem e layout tardio
    window.addEventListener('load', remedir, { once: true });
  }

  /* -----------------------------------------------------------------------
     PRIORIDADE DE MEDIDA
     Por que os dois pins declaram refreshPriority

     Sintoma, medido em 9 de setembro de 2026 numa janela de 1920x911: o pin
     do capitulo 10 comecava em 15529 enquanto o topo real da secao estava em
     16714. Erro de 1185px, e um refresh nao corrigia, porque nao era medida
     velha. Era ordem de medida.

     A conta fecha exata: o trilho do capitulo 4 fixa a tela por 1184px. Esse
     numero e a diferenca inteira.

     O que acontece por dentro. Para remedir, o ScrollTrigger tira o
     espacamento dos pins, mede tudo e devolve o espacamento depois. Quem for
     medido antes de o espacador do trilho voltar mede uma pagina 1184px mais
     curta. Sem refreshPriority declarado o desempate e a ordem de criacao, e
     o gestoRevelacao era criado antes do trilhoHorizontal.

     O estrago aparecia longe da causa, nas duas pontas do capitulo 10:

       Entrada. O pin travava 1184px cedo, ainda dentro do capitulo 9. O
       palco estava 1184px abaixo no documento e o pin o jogava para
       position:fixed, top 0. A tela cortava seco para a foto. O veu de
       entrada nao tinha como cobrir isso: o bloco inteiro se teleportava
       para dentro da janela ja aceso.

       Saida. O pin soltava 1184px antes do lugar onde o palco assenta no
       fim do espacador. Sobrava esse tanto de creme vazio, o fundo do
       .revelacao sem nada em cima, e so depois o palco voltava a subir na
       tela, mostrando o titulo primeiro e as tres cartas de novo, agora
       paradas. Era a impressao de ser teleportado para cima.

     Um defeito so, duas emendas quebradas. Nenhuma das duas era problema de
     gesto, de easing ou de duracao, e por isso mexer no movimento nunca
     resolveu.

     Regra que sai disso: **todo ScrollTrigger que fixa a tela nesta pagina
     declara refreshPriority, e o de cima recebe o numero maior.** Numero
     maior remede primeiro. Basta a chave existir nas vars para o
     ScrollTrigger passar a ordenar a remedida em vez de usar a ordem de
     criacao, entao declarar nos dois nao e redundancia, e o que liga a
     ordenacao. Se um terceiro pin entrar, ele entra nessa escala pela
     posicao dele na pagina, e o painel de ?debug=1 mostra ERRO MEDIDA para
     conferir: tem que ser 0.
     --------------------------------------------------------------------- */
})();
