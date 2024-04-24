h= float(input('Digite sua altura: '))
ph= (72.7*h)- 58
pm= (62.1*h)-44.7
print('Com {}M de altura o peso ideal é :\n{:.1f}KG para homens.\n{:.1f}KG para mulheres.'.format(h,ph,pm))