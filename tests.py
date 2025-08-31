from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем 
наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод 
get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный 
экземпляр класса BooksCollector()


class TestBooksCollector:

    def test_add_new_book_add_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Маленький принц')
        # Проверяем, что длина словаря равна 1
        assert len(collector.get_books_genre()) == 1


class TestBooksCollector:
     
     def test_add_new_book_not_add_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.add_new_book('Война и мир')  # Попытка добавить ту же 
книгу
        # Проверяем, что книга добавлена только один раз
        assert list(collector.get_books_genre().keys()).count('Война и 
мир') == 1


class TestBooksCollector:

    def test_set_book_genre_valid(self):
        collector = BooksCollector()
        collector.add_new_book('Анна Каренина')
        # Устанавливаем допустимый жанр
        collector.set_book_genre('Анна Каренина', 'Детективы')
        # Проверяем, что жанр установлен правильно
        assert collector.get_book_genre('Анна Каренина') == 'Детективы'


class TestBooksCollector:

    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Анна Каренина')
        # Устанавливаем допустимый жанр
        collector.set_book_genre('Анна Каренина', 'Детективы')
        # Попытка установить несуществующий жанр
        collector.set_book_genre('Анна Каренина', 'Неизвестный жанр')
        # Жанр не должен измениться
        assert collector.get_book_genre('Анна Каренина') == 'Детективы'


class TestBooksCollector:

    def test_set_book_genre_nonexistent_book(self):
        collector = BooksCollector()
        # Попытка установить жанр для несуществующей книги
        collector.set_book_genre('Не существующая книга', 'Фантастика')
        # Проверяем, что для несуществующей книги жанр не установлен
        assert collector.get_book_genre('Не существующая книга') is None


class TestBooksCollector:

    def test_get_book_genre_existing(self):
        collector = BooksCollector()
        collector.add_new_book('Мастер и Маргарита')
        collector.set_book_genre('Мастер и Маргарита', 'Фантастика')
        # Проверка существующей книги
        assert collector.get_book_genre('Мастер и Маргарита') == 
'Фантастика'


class TestBooksCollector:

    def test_get_book_genre_nonexistent(self):
        collector = BooksCollector()
        # Проверка несуществующей книги
        assert collector.get_book_genre('Некоторая книга') is None


class TestBooksCollector:

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга1')
        collector.set_book_genre('Книга1', 'Фантастика')
        collector.add_new_book('Книга2')
        collector.set_book_genre('Книга2', 'Ужасы')
        result = collector.get_books_with_specific_genre('Фантастика')
        #Проверяем, что 'Книга1' есть в результате — потому что она 
принадлежит к этому жанру.
        assert 'Книга1' in result
        #Проверяем, что 'Книга2' не входит в результат — потому что она 
принадлежит к другому жанру.
        assert 'Книга2' not in result


class TestBooksCollector:

    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга3')
        collector.set_book_genre('Книга3', 'Мультфильмы')
        genre_dict = collector.get_books_genre()
        #Проверяем словарь и жанр добавленный в него.
        assert isinstance(genre_dict, dict)
        assert genre_dict['Книга3'] == 'Мультфильмы'


class TestBooksCollector:

    def test_get_books_for_children_includes_multfilmy(self):
        collector = BooksCollector()
        collector.add_new_book('Книга5')
        collector.set_book_genre('Книга5', 'Мультфильмы')
        children_books = collector.get_books_for_children()
        assert 'Книга5' in children_books


class TestBooksCollector:

    def test_get_books_for_children_excludes_horrors(self):
        collector = BooksCollector()
        collector.add_new_book('Книга5')
        collector.set_book_genre('Книга5', 'Ужасы')
        children_books = collector.get_books_for_children()
        assert 'Книга5' not in children_books


class TestBooksCollector:

    def test_add_book_in_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book('Книга7')
        collector.set_book_genre('Книга7', 'Комедии')
        collector.add_book_in_favorites('Книга7')
        # Проверка, что книга добавлена в favorites
        assert 'Книга7' in collector.get_list_of_favorites_books()


class TestBooksCollector:

    def test_add_book_in_favorites_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book('Книга7')
        collector.set_book_genre('Книга7', 'Комедии')
        collector.add_book_in_favorites('Книга7')
        # Попытка добавить повторно — не должно дублироваться
        collector.add_book_in_favorites('Книга7')
        favorites = collector.get_list_of_favorites_books()
        assert favorites.count('Книга7') == 1


class TestBooksCollector:

    def test_add_book_in_favorites_nonexistent(self):
        collector = BooksCollector()
        # Попытка добавить несуществующую книгу
        collector.add_book_in_favorites('Не существующая')
        # Проверка, что не добавилась
        assert 'Не существующая' not in 
collector.get_list_of_favorites_books()


class TestBooksCollector:

    def test_delete_book_from_favorites_successful(self):
        collector = BooksCollector()
        collector.add_new_book('Книга8')
        collector.set_book_genre('Книга8', 'Детективы')
        collector.add_book_in_favorites('Книга8')
        # Удаляем из избранного
        collector.delete_book_from_favorites('Книга8')
        # Проверяем, что книга больше не в списке избранных
        assert 'Книга8' not in collector.get_list_of_favorites_books()


class TestBooksCollector:

    def test_favorites_list_initially_empty(self):
        collector = BooksCollector()
        assert collector.get_list_of_favorites_books() == []  


class TestBooksCollector:  

    def test_favorites_list_after_adding_book(self):
        collector = BooksCollector()
        collector.add_new_book('Книга9')
        collector.set_book_genre('Книга9', 'Фантастика')
        collector.add_book_in_favorites('Книга9')
        # Проверяем, что книга есть в списке избранных
        favs = collector.get_list_of_favorites_books()
        assert 'Книга9' in favs  

