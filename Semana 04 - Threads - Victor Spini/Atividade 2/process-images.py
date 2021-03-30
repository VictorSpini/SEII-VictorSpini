// Victor Spini Paranaiba - 11611EMT005

# Inicia-se importando os módulos que permite execução de processos ou thread e apoio para trabalhar com funções de tempo e filtro de imagens
import concurrent.futures  # Interface para processos e threads de forma assincrona
import time  # Para utilizar funções relacionadas a tempo

from PIL import Image, ImageFilter	# Suporte para filtro de imagem

img_names = [
    'photo-1516117172878-fd2c41f4a759.jpg',
    'photo-1532009324734-20a7a5813719.jpg',
    'photo-1524429656589-6633a470097c.jpg',
    'photo-1530224264768-7ff8c1789d79.jpg',
    'photo-1564135624576-c5c88640f235.jpg',
    'photo-1541698444083-023c97d3f4b6.jpg',
    'photo-1522364723953-452d3431c267.jpg',
    'photo-1513938709626-033611b8cc03.jpg',
    'photo-1507143550189-fed454f93097.jpg',
    'photo-1493976040374-85c8e12f0c0e.jpg',
    'photo-1504198453319-5ce911bafcde.jpg',
    'photo-1530122037265-a5f1f91d3b99.jpg',
    'photo-1516972810927-80185027ca84.jpg',
    'photo-1550439062-609e1531270e.jpg',
    'photo-1549692520-acc6669e2f0c.jpg'
]

t1 = time.perf_counter()	# Definição de t1 para performance counter

size = (1200, 1200)

# É aplicado um filtro do tipo gaussiano nas imagens conforme função abaixo
# for img_name in img_names:
def process_image(img_name):
    img = Image.open(img_name)	# Abre a imagem

    img = img.filter(ImageFilter.GaussianBlur(15))	# Filtro Gaussiano aplicado

    img.thumbnail(size)				
    img.save(f'processed/{img_name}')		
    print(f'{img_name} was processed...')	# Salva o arquivo após processamento e exibe mensagem


# with concurrent.futures.ThreadPoolExecutor() as executor:
with concurrent.futures.ProcessPoolExecutor() as executor:	# Executor de processos e threads de forma assincrona
    executor.map(process_image, img_names)			# O executor processa a lista de imagens de forma simultânea

t2 = time.perf_counter()	# Contabilização de t2 para o contador de performance

print(f'Finished in {t2-t1} seconds')
