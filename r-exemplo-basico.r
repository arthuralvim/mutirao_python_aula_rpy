
# acessando uma constante
pi

a <- 10
a = 10
b = 15
a + b # resultado da soma de a + b


valores = c(6, 7, 4, 3, 2, 0, 0, 6)
valores[4]
length(valores)
min(valores)
max(valores)

sum(valores)
prod(valores)
sort(valores)
mean(valores)
median(valores)
sd(valores)
var(valores)

he <- c(10, 2, 23, 11, 14, 35, 46, 32, 13, 51, 27, 49)
ha <- he
var(he)
cov(ha, he)
cor(ha, he)

sqr<-function(x){return(x*x); }
sqr(4)
eleva3<-function(a){ return(a*a*a); }
eleva3(3)


help.start()    # Ajuda em geral
help(exemplo)   # Ajuda sobre a função exemplo
?exemplo        # mesma coisa
apropos("exemplo")  # Lista todas funções com a string "exemplo"
example(foo)   # show an example of function foo

getwd()         # imprime o diretório de trabalho atual - cwd
setwd("c:/docs/mydir")  # mudar o diretório de trabalho
dir()           # Lista arquivos do cwd.
ls(all=TRUE)    # lista objetos todos objetos
rm()            # remove objetos
history()       # Mostra os 25 últimos comandos
savehistory(file="historico") # Salva seu histórico de comandos
            # default is ".Rhistory"
loadhistory(file="historico") # Carrega seu histórico de comandos

save.image() # Salva tudo que foi criado em um arquivo .RData no cwd
save(object list,file="objetos.RData") # Para salvar objetos específicos
load("objetos.RData") # Carregar os objetos na sessão corrente

pdf("mygraph.pdf")
png("mygraph.png")
jpeg("mygraph.jpg")
bmp("mygraph.bmp")
postscript("mygraph.ps")
jpeg("c:/mygraphs/myplot.jpg") # Salvando saída de um gráfico em jpeg.
plot(x)
dev.off()


.libPaths() # get library location
library()   # see all packages installed
search()    # see packages currently loaded
detach("package:nomepacote") #remove pacote

chooseCRANmirror() # Escolha o repositório
install.packages("ISwR", dependencies = TRUE)
library (ISwR) # Carrega pacote
install.packages("caminho.do.arquivo/pacote.tar.gz",repos=NULL)

# options (CRAN="http://cran.r-project.org") Repositório principal
options(CRAN = "http://www.vps.fmvz.usp.br/CRAN/")
# Escolhe-se o Repositório CRAN da USP
install.packages(available.packages()[,1])
# Instala todos os pacotes disponíveis lá
