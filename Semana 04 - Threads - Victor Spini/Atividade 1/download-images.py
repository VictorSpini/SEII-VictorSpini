// Victor Spini Paranaiba - 11611EMT005

# Inicia-se importando os módulos que permite execução de thread, solicitações HTTP e apoio para trabalhar com funções de tempo
import concurrent.futures  # Interface para processos e threads de forma assincrona
import time  # Para utilizar funções relacionadas a tempo
import requests  # Suporte para solicitações em formato HTTP

img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
    'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
    'https://images.unsplash.com/photo-1507143550189-fed454f93097',
    'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
    'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
    'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
    'https://images.unsplash.com/photo-1516972810927-80185027ca84',
    'https://images.unsplash.com/photo-1550439062-609e1531270e',
    'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
]

t1 = time.perf_counter()  # Definição de t1 para performance counter

# Download da imagem por meio da função em que o conteudo da URL é escrito em um novo arquivo
# for img_url in img_urls:
def download_image(img_url):
    img_bytes = requests.get(img_url).content  # Realiza a recuperação do conteudo da URL indicada
    img_name = img_url.split(
        '/'
    )[3]  # Utiliza-se a barra '/' para dividir a string e guarda o nome da imagem depois do split
    img_name = f'{img_name}.jpg'  # Formato do arquivo definido como jpg
    with open(img_name,
              'wb') as img_file:  # Salva o conteúdo da URL e finalização a criação do arquivo
        img_file.write(img_bytes)
        print(f'{img_name} was downloaded...')


with concurrent.futures.ThreadPoolExecutor() as executor:  # Executor de processos e threads de forma assincrona
    executor.map( download_image, img_urls)  # O executor faz download da lista de imagens de forma simultânea

t2 = time.perf_counter()  # Contabilização de t2 para o contador de performance

print(f'Finished in {t2-t1} seconds')
