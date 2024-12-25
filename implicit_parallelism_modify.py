import concurrent.futures
def pangkat(x):
    return x**2

angka = [1,2,3,4,5]

with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(pangkat, num) for num in angka]
    results = [future.result() for future in futures]
    
print("Hasil:", results)