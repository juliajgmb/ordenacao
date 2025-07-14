import time
import sys
import os

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def read_input_file(filename):
    with open(filename, 'r') as f:
        return list(map(int, f.read().split()))

def write_output_file(filename, data):
    with open(filename, 'w') as f:
        f.write(' '.join(map(str, data)))

def main():
    if len(sys.argv) < 2:
        print("Uso: python ordenacao.py <arquivo1.in> <arquivo2.in> ...")
        sys.exit(1)

    for arquivo in sys.argv[1:]:
        print(f"\nArquivo: {arquivo}")
        dados = read_input_file(arquivo)

        # Selection Sort
        dados_selection = dados[:]
        start = time.time()
        ordenado_selection = selection_sort(dados_selection)
        end = time.time()
        tempo_selection = end - start
        out_selection = arquivo.replace(".in", ".selection.out")
        write_output_file(out_selection, ordenado_selection)
        print(f"SelectionSort: {tempo_selection:.6f} segundos | saída: {out_selection}")

        # Insertion Sort
        dados_insertion = dados[:]
        start = time.time()
        ordenado_insertion = insertion_sort(dados_insertion)
        end = time.time()
        tempo_insertion = end - start
        out_insertion = arquivo.replace(".in", ".insertion.out")
        write_output_file(out_insertion, ordenado_insertion)
        print(f"InsertionSort: {tempo_insertion:.6f} segundos | saída: {out_insertion}")

if __name__ == "__main__":
    main()
