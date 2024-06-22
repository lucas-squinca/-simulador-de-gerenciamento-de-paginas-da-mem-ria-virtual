import os
import time

class PageReplacementSimulator:
    def __init__(self, algorithm, num_frames):
        self.algorithm = algorithm
        self.num_frames = num_frames
        self.frames = [-1] * num_frames
        self.page_faults = 0
        self.page_history = []

    def load_page(self, page, directory):
        page_file = os.path.join(directory, f"{page}.pag")
        with open(page_file, 'r') as f:
            return f.read()

    def display_frames(self):
        print(f"Frames: {self.frames}")
    
    def fifo(self, page, directory):
        if page not in self.frames:
            self.page_faults += 1
            self.frames.pop(0)
            self.frames.append(page)
        self.display_frames()

    def lru(self, page, directory):
        if page not in self.frames:
            self.page_faults += 1
            if -1 in self.frames:
                self.frames[self.frames.index(-1)] = page
            else:
                lru_page = self.page_history.pop(0)
                self.frames[self.frames.index(lru_page)] = page
        else:
            self.page_history.remove(page)
        self.page_history.append(page)
        self.display_frames()

    def run(self, requests, directory):
        for page in requests:
            print(f"\nPágina Requerida: {page}")
            content = self.load_page(page, directory)
            if self.algorithm == 'FIFO':
                self.fifo(page, directory)
            elif self.algorithm == 'LRU':
                self.lru(page, directory)
            print(f"Conteúdo: {content}")
            time.sleep(1)
        print(f"\nTotal de Falhas de Página: {self.page_faults}")