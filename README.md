# Scrap_Google_Slides

Script usado para capturar os slides do Google qu são embutidos em páginas Web

1 - Para usar esse script, primeiro é necessário se obter a quantidade de slides a se captura e a url dos slides 

2 - Use a ferramenta de inspeça de codigo do navegador para encontrar os slides normalmente em uma tag de iframe como a de exemplo abaixo:
<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vRmbcweNnoSWPv6ZUviWGBCsbAsJI1k0vWvbPDsamyUphdYzi1AzS3RaRZrucxFQZJdQkIT5SoQld1e/pubembed?start=false&amp;loop=false&amp;delayms=3000" width="1280" height="749" frameborder="0" allowfullscreen="allowfullscreen"></iframe>

<br>
3 - Capture somente a url do https até "pub" ou pubembd como no exemplo abaixo:
https://docs.google.com/presentation/d/e/2PACX-1vRmbcweNnoSWPv6ZUviWGBCsbAsJI1k0vWvbPDsamyUphdYzi1AzS3RaRZrucxFQZJdQkIT5SoQld1e/pub

4 - com essa URL a chamada do scrip é 
python Slides_Google_Scrap.py <QUANTIDADE_DE_SLIDES> <URL>

5 - Vai ser gerado um pdf com o nome "apresentacao.pdf" cm todos os slides capturados


OBS: 
- cada slides vai estar dentro da pasta "slides_capturados" no formato png
- se for realizada outra execução sem limpara a pasta, o script vai sobrescrever os arquivos na pasta de slides, por via das dúvidas limpe a pasta para evitar que slides antigos não sejam usados na nova apresentação

Para limpar aa pasta dos slides capturados use a opção "l" ou "L"
  python Slides_Google_Scrap.py L

