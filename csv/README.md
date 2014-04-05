# Dados CSV

O unipt-stats requer esses dados. Baixe-os com este comando:
```bash
$ bash download.sh
```

Isso deverá criar dois arquivos `.csv` neste diretório. Verifique:
```bash
$ ls *.csv
userstats-br.csv  userstats-pt.csv
```

## Importação

Os arquivos CSV são usados para popular ou atualizar uma base de dados MongoDB. Se você seguiu as instruções de [README.md/Dependências](README.md/Dependências), basta certificar-se de que o serviço do banco de dados está executando e comandar a importação.

```bash
$ sudo service mongodb status
mongodb stop/waiting
$ sudo service mongodb start
mongodb start/running, process 10713

$ bash import.sh
```

O resultado do `import.sh` deverá ser algo assim:
```
connected to: 127.0.0.1
		303054/474624	63%
			3400	1133/second
		416626/474624	87%
			5000	833/second
		471965/474624	99%
			5800	644/second
imported 5838 objects
connected to: 127.0.0.1
		311361/340231	91%
			3700	1233/second
imported 4128 objects
```

O procedimento pode não ser tão rápido, porque é feita uma confrontação entre o que já existia no MongoDB e o que existe em cada CSV.

## mongo ‒ acesso ao MongoDB pelo Terminal

Você pode querer consultar o banco de dados e efetuar algum teste. Para isso, terá de aprender a usar o mongo. Comece assim:

```bash
$ mongo
MongoDB shell version: 2.0.4
connecting to: test
> use unipt-stats
switched to db unipt-stats
> db.portugal.find().count()
4127
> exit
bye
```

Também pode ser muito útil simplesmente consultar a ajuda:

```
$ mongo
MongoDB shell version: 2.0.4
connecting to: test
> help
	db.help()                    help on db methods
	db.mycoll.help()             help on collection methods
	rs.help()                    help on replica set methods
	help admin                   administrative help
	help connect                 connecting to a db help
	help keys                    key shortcuts
	help misc                    misc things to know
	help mr                      mapreduce

	show dbs                     show database names
	show collections             show collections in current database
	show users                   show users in current database
	show profile                 show most recent system.profile entries with time >= 1ms
	show logs                    show the accessible logger names
	show log [name]              prints out the last segment of log in memory, 'global' is default
	use <db_name>                set current database
	db.foo.find()                list objects in collection foo
	db.foo.find( { a : 1 } )     list objects in foo where a == 1
	it                           result of the last line evaluated; use to further iterate
	DBQuery.shellBatchSize = x   set default number of items to display on shell
	exit                         quit the mongo shell
> exit
bye
```

Se você precisar limpar toda a base de dados para então reiniciá-la com nova importação, faça:

```bash
$ mongo
> use unipt-stats
> db.dropDatabase()
> exit
```
