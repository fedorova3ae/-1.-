# TODO Найдите количество книг, которое можно разместить на дискете
volume_mb = 1.44 #в Мб
pages = 100
lines = 50 #на одной странице
symbols = 25 #в одной строке
symbols_volume = 4 #в байтах
books_volume = pages * lines * symbols * symbols_volume
volume_b = volume_mb * 1024 * 1024 #в байтах
print("Количество книг, помещающихся на дискету:", int(volume_b//books_volume))
