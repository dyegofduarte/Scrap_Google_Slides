from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from PIL import Image
import time
import os
import sys
import shutil


# Argumento
OUTPUT_DIR = "slides_capturados"

# Verifica argumentos
if (sys.argv[1].lower()) == "l":
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)  # Remove a pasta inteira
        os.makedirs(OUTPUT_DIR)    # Cria novamente vazia
        print(f"Pasta '{OUTPUT_DIR}' foi zerada.")
    else:
        os.makedirs(OUTPUT_DIR)
        print(f"Pasta '{OUTPUT_DIR}' criada (já estava inexistente).")
    sys.exit(0)


elif len(sys.argv) != 3:
    print("Uso: python3 script.py <quantidade_de_slides> <url_dos_slides>")
    print("Uso: python3 script.py l ou L")
    sys.exit(1)

# Argumentos
NUM_SLIDES = int(sys.argv[1])
SLIDES_URL = sys.argv[2]
#OUTPUT_DIR = "slides_capturados"
OUTPUT_PDF = os.path.join(OUTPUT_DIR, "apresentacao.pdf")

# Configura o navegador
options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

# Cria pasta de saída
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Abre a apresentação
driver.get(SLIDES_URL)
time.sleep(5)

# Captura os slides
for i in range(NUM_SLIDES):
    filename = os.path.join(OUTPUT_DIR, f"slide_{i+1}.png")
    time.sleep(3)
    driver.save_screenshot(filename)
    print(f"Slide {i+1} salvo em {filename}")

    # Avança para o próximo slide
    try:
        body = driver.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.ARROW_RIGHT)
    except:
        print("Não foi possível avançar para o próximo slide.")
        break

driver.quit()
print("Captura finalizada.")

# Converte imagens em PDF
images = []
for i in range(1, NUM_SLIDES + 1):
    path = os.path.join(OUTPUT_DIR, f"slide_{i}.png")
    if os.path.exists(path):
        img = Image.open(path).convert("RGB")
        images.append(img)

if images:
    images[0].save(OUTPUT_PDF, save_all=True, append_images=images[1:])
    print(f"PDF gerado com {len(images)} slides: {OUTPUT_PDF}")
else:
    print("Nenhuma imagem encontrada para gerar o PDF.")