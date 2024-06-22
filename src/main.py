import sys
from gerador_de_paginas import generate_pages, generate_page_requests
from substituicao_de_pagina import PageReplacementSimulator

def main():
    if len(sys.argv) != 6:
        print("Uso: python main.py [diretório_das_páginas] [algoritmo_de_substituição_de_páginas] [número_de_frames_de_memória] [quantidade_de_páginas_únicas] [quantidades_de_páginas_requeridas]")
        return
    
    directory = sys.argv[1]
    algorithm = sys.argv[2].upper()
    num_frames = int(sys.argv[3])
    num_unique_pages = int(sys.argv[4])
    num_page_requests = int(sys.argv[5])
    
    generate_pages(directory, num_unique_pages)
    requests = generate_page_requests(num_page_requests, num_unique_pages)

    simulator = PageReplacementSimulator(algorithm, num_frames)
    simulator.run(requests, directory)
    
    # Mostrar a sequência de páginas requeridas, caso desejado;
    # print("\nSequência de páginas requeridas:", requests)

if __name__ == "__main__":
    main()
