import sys
sys.path.insert(1, '../')
from assertEquals import assertEquals

def average(salaries):
    return ((sum(salaries))-(min(salaries)+max(salaries))) / (len(salaries)-2)

tests = [
[[4000,3000,1000,2000],2500.00000],
[[1000,2000,3000],2000.00000]
]
for i in tests:
    print(assertEquals(average(i[0]),i[1]))