from main import BooksCollector

# создаем фикстуру

@pytest.fixture
def collector():
    return BooksCollector()
    
# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
# ошибка из-за переноса комментария устранена 
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self, collector):

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()



    def test_add_new_book_add_one_book(self, collector):
        collector.add_new_book('Маленький принц')
        # Проверяем, что длина словаря равна 1
        assert len(collector.get_books_genre()) == 1


     
    def test_add_new_book_not_add_duplicate(self, collector):
        collector.add_new_book('Война и мир')
        collector.add_new_book('Война и мир')  # Попытка добавить ту же книгу
        # Проверяем, что книга добавлена только один раз
        # ошибка из-за переноса комментария устранена
        assert list(collector.get_books_genre().keys()).count('Война и мир') == 1



    def test_set_book_genre_valid(self, collector):
        collector.add_new_book('Анна Каренина')
        # Устанавливаем допустимый жанр
        collector.set_book_genre('Анна Каренина', 'Детективы')
        # Проверяем, что жанр установлен правильно
        assert collector.get_book_genre('Анна Каренина') == 'Детективы'



    def test_set_book_genre_invalid_genre(self, collector):
        collector.add_new_book('Анна Каренина')
        # Устанавливаем допустимый жанр
        collector.set_book_genre('Анна Каренина', 'Детективы')
        # Попытка установить несуществующий жанр
        collector.set_book_genre('Анна Каренина', 'Неизвестный жанр')
        # Жанр не должен измениться
        assert collector.get_book_genre('Анна Каренина') == 'Детективы'



    def test_set_book_genre_nonexistent_book(self, collector):
        # Попытка установить жанр для несуществующей книги
        collector.set_book_genre('Не существующая книга', 'Фантастика')
        # Проверяем, что для несуществующей книги жанр не установлен
        assert collector.get_book_genre('Не существующая книга') is None



    def test_get_book_genre_existing(self, collector):
        collector.add_new_book('Мастер и Маргарита')
        collector.set_book_genre('Мастер и Маргарита', 'Фантастика')
        # Проверка существующей книги
        assert collector.get_book_genre('Мастер и Маргарита') == 'Фантастика'



    def test_get_book_genre_nonexistent(self, collector):
        # Проверка несуществующей книги
        assert collector.get_book_genre('Некоторая книга') is None



    def test_get_books_with_specific_genre_success(self, collector):
        collector.add_new_book('Книга1')
        collector.set_book_genre('Книга1', 'Фантастика')
        collector.add_new_book('Книга2')
        collector.set_book_genre('Книга2', 'Ужасы')
        result = collector.get_books_with_specific_genre('Фантастика')
        #Проверяем, что 'Книга1' есть в результате — потому что она принадлежит к этому жанру.
        assert 'Книга1' in result
        #Проверяем, что 'Книга2' не входит в результат — потому что она принадлежит к другому жанру.
        assert 'Книга2' not in result



    def test_get_books_genre_success(self, collector):
        collector.add_new_book('Книга3')
        collector.set_book_genre('Книга3', 'Мультфильмы')
        genre_dict = collector.get_books_genre()
        # Проверяем словарь и жанр добавленный в него.
        assert isinstance(genre_dict, dict)
        assert genre_dict['Книга3'] == 'Мультфильмы'



    def test_get_books_for_children_includes_multfilmy(self, collector):
        collector.add_new_book('Книга4')
        collector.set_book_genre('Книга4', 'Мультфильмы') # Предположительно рейтинг 0+
        children_books = collector.get_books_for_children()
        assert 'Книга4' in children_books



    def test_get_books_for_children_excludes_horrors(self, collector):
        collector.add_new_book('Книга5')
        collector.set_book_genre('Книга5', 'Ужасы') # Предположительно рейтинг 18+
        children_books = collector.get_books_for_children()
        assert 'Книга5' not in children_books



    def test_add_book_in_favorites_success(self, collector):
        collector.add_new_book('Книга6')
        collector.add_book_in_favorites('Книга6')
        # Проверка, что книга добавлена в favorites
        assert 'Книга7' in collector.get_list_of_favorites_books()



    def test_add_book_in_favorites_duplicate(self, collector):
        collector.add_new_book('Книга7')
        collector.add_book_in_favorites('Книга7')
        # Попытка добавить повторно — не должно дублироваться
        collector.add_book_in_favorites('Книга7')
        favorites = collector.get_list_of_favorites_books()
        assert favorites.count('Книга7') == 1



    def test_add_book_in_favorites_nonexistent(self, collector):
        # Попытка добавить несуществующую книгу
        collector.add_book_in_favorites('Не существующая')
        # Проверка, что не добавилась
        assert 'Не существующая' not in collector.get_list_of_favorites_books()



    def test_delete_book_from_favorites_success(self, collector):
        collector.add_new_book('Книга8')
        collector.add_book_in_favorites('Книга8')
        # Удаляем из избранного
        collector.delete_book_from_favorites('Книга8')
        # Проверяем, что книга больше не в списке избранных
        assert 'Книга8' not in collector.get_list_of_favorites_books()



    def test_favorites_list_initially_empty(self, collector):
        assert collector.get_list_of_favorites_books() == []  

  

    def test_get_list_of_favorites_books_after_adding_book_success(self, collector):
        collector.add_new_book('Книга9')
        collector.set_book_genre('Книга9', 'Фантастика')
        collector.add_book_in_favorites('Книга9')
        # Проверяем, что книга есть в списке избранных
        favs = collector.get_list_of_favorites_books()
        assert 'Книга9' in favs  



    def test_add_new_book_too_long_name_unsuccess(self, collector):
        # Название длиной 41 символ
        long_name = "a" * 41
        collector.add_new_book(long_name)
        # Книга не должна добавиться
        assert long_name not in collector.books_genre



    def test_add_new_book_success(self, collector):
        # Добавляем книгу с допустимой длиной
        collector.add_new_book("Моя новая книга")
        assert "Моя новая книга" in collector.books_genre
        # Жанр по умолчанию пустой
        assert collector.books_genre["Моя новая книга"] == ''
