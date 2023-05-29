<h1>Url Info Extractor</h1>

<h2>Utilize essa biblioteca para extrair informaçoes de URLs</h2>

Ex:<br>

url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"

<li>Queres saber qual o campo onde as variaveis estao?</li>

"bytebank.com/<strong style="color: red;">cambio</strong>?quantidade=100&moedaOrigem=real&moedaDestino=dolar"

<li>Queres extrair quais as variaveis?</li>

"bytebank.com/cambio?<strong style="color: red;">quantidade=100</strong>&<strong style="color: red;">moedaOrigem=real</strong>&<strong style="color: red;">moedaDestino=dolar</strong>"

<li>Queres saber se o url e valida para esse tipo de extraçao?</li>

"bytebank.com/cambio" -> Nao valido<br>
"bytebank.com/" -> Nao valido<br>

Nesse topico e levantado um exceçao para ajudar a consertar o problema.

Essa biblioteca essa capacidade de fazer essas distinçoes para que consiga extrair
o maximo de informaçoes possivel para o objetivo que voce deseja alcançar!