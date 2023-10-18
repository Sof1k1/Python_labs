# TODO Найдите количество книг, которое можно разместить на дискете

volume_of_mb = 1.44
pages = 100
rows_on_page = 50
simbols_on_row = 25
volume_of_simbol = 4

volume_of_b = volume_of_mb * 1024 * 1024
volume_of_book = volume_of_simbol * simbols_on_row * rows_on_page * pages
books = int(volume_of_b // volume_of_book)

print("Количество книг, помещающихся на дискету:", books)