unipt-stats
===========

*__en:__ Utility to make useful statistics queries to democratic decisions in the OpenStreetMap's wiki.*

Utilitário que possibilita consultas estatísticas úteis para decisões democráticas no [wiki](http://wiki.openstreetmap.org) do projeto [OpenStreetMap](http://www.openstreetmap.org).

No código, é usado preferencialmente inglês. Nos arquivos `.md` e nas *issues*, se você fala português __fluentemente__, use-o. Se não, use inglês. Inicialmente este software é criado para responder a [anseios do OpenStreetMap lusófono](http://wiki.openstreetmap.org/wiki/Category_talk:User_pt).

O unipt-stats é disponibilizado sob a [Expat License](LICENSE), também conhecida ambiguamente como "[MIT License](https://en.wikipedia.org/wiki/Expat_License)" — existe mais de uma "licença do MIT".

## Instruções iniciais

As instruções que seguem até o final do documento constituem o uso mais fácil que o autor identificou. Você pode preferir outros comandos equivalentes.


Se você pretende contribuir com código, configure adequadamente o seu ambiente de desenvolvimento, especialmente o [Git](http://git-scm.com/book/pt-br). Dê preferência a fazer *pull-request*. Mas você também pode enviar *git patch* para o e-mail do autor: [alexandre.mbm@gmail.com](mailto:alexandre.mbm@gmail.com).

## Dependências

```bash
$ sudo apt-get install bash git python
```

Testado em Ubuntu 12.04.4 LTS.


## Instalar

Clonar o repositório Git:

```bash
$ git clone https://github.com/alexandre-mbm/unipt-stats.git
```

Baixar dados CSV:

```bash
$ cd unipt-stats
$ cd csv
$ bash download.sh
```

Mais informações podem ser encontradas no [`csv/README.md`](csv/README.md).

## Usar

Se você está no diretório `csv/` do passo anterior, volte ao diretório raiz `unipt-stats`:
```bash
$ cd ../
```

Executar:

```bash
$ python unipt-stats.py
br      = 5837
pt      = 4127
br + pt = 9964
br ∪ pt = 9718
```

Esta __primeira versão__ fornece um resultado muito básico. O que está acima significa:

```
br      = 5837 usuários mapearam algo no Brasil
pt      = 4127 usuários mapearam algo em Portugal
br + pt = 9964 é a soma aritmética dos valores acima
br ∪ pt = 9718 usuários mapearam algo no Brasil ou em Portugal
br ∩ pt =  246 usuários mapearam algo no Brasil e em Portugal
```

Próximas versões deverão receber parâmetros e trazer ajuda `--help`.

5 de Abril de 2014 00:25

## Participe!

Se você é um usuário OSM lusófono, participe das [discussões que motivam o desenvolvimento do unipt-stats](http://wiki.openstreetmap.org/wiki/Category_talk:User_pt).

Se você tem __requisitos ou questões propriamente para o software__, prefira criar ou comentar *issues* neste repositório invés de gerar novas discussões no wiki, no fórum ou nas listas de e-mails do projeto OpenStreetMap.
