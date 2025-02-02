<h1>В текущем проекте используется фреймворк FastAPI с базой данных PostgreSQL, а для взаимодействия с БД применена библиотека TortoiseORM</h1>
<h2>Небольшой обзор возможностей</h2>
<h3>Запустим проект через консоль</h3>

![Снимок экрана 2025-02-02 093427](https://github.com/user-attachments/assets/2be57053-060e-442e-af5a-24a1eeb8868c)

<hr>
<p>(файл "db_config", содержащий конфигурацию используемой базы данных не включён в проект по понятным причинам)</p>

![Снимок экрана 2025-02-02 094650](https://github.com/user-attachments/assets/96742f88-63fe-41cb-9339-25b8fc8aa289)
<hr>

<h3>Окажемся на главной странице и увидим предварительно добавленные записи в базу данных</h3>

![Снимок экрана 2025-02-02 093502](https://github.com/user-attachments/assets/5f508edc-4571-47da-a9aa-7e93c96e90af)

![Снимок экрана 2025-02-02 093445](https://github.com/user-attachments/assets/7e8739e9-4cf6-4806-9abf-393ccb45e5de)

<h3>Взаимодействие с ней происходит через "FastAPI - Swagger UI", для которого созданы 2 файла с CRUD запросами для каждой из существующих моделей</h3>

![Снимок экрана 2025-02-02 094513](https://github.com/user-attachments/assets/254a555e-aec9-4ac3-bd88-4e8b14afafc0)

<h3>Например, получим товар по его ID</h3>

![Снимок экрана 2025-02-02 094547](https://github.com/user-attachments/assets/04654dbd-2194-4916-99e0-8c62a85941eb)

<h3>С пользователем доступны те же операции</h3>

![Снимок экрана 2025-02-02 094557](https://github.com/user-attachments/assets/71a4b5fa-b386-4a12-a29e-898e92ff38d9)

<h3>Возвращаемся к сайту. На главной представлено 8 последних товаров со скидкой</h3>

![Снимок экрана 2025-02-02 093523](https://github.com/user-attachments/assets/bc561051-5b38-46bc-8dc5-4b43423d9a96)
<hr>
<h3>Чтобы посмотреть больше перейдём в каталог</h3>

![Снимок экрана 2025-02-02 093537](https://github.com/user-attachments/assets/b1431e60-7dec-483a-92e0-6ea0c9f79f24)

<h3>Тут уже доступен весь ассортимент. Можно отсортировать товары по полу, а также пролистать страницы (на каждой отображается по 8 карточек)</h3>

![Снимок экрана 2025-02-02 093550](https://github.com/user-attachments/assets/675770b6-dd1c-432f-863a-aac562b6ec4a)
<hr>

![Снимок экрана 2025-02-02 093556](https://github.com/user-attachments/assets/79fd1fe2-43ec-4d6e-a820-9e6d95e805e6)
<hr>

![Снимок экрана 2025-02-02 093602](https://github.com/user-attachments/assets/7ca5c191-caa4-434e-abba-b2828fa1e0ae)

<h3>Отобразим фильтр "женские". Страниц соответственно станет меньше</h3>

![Снимок экрана 2025-02-02 093612](https://github.com/user-attachments/assets/d05ec6d3-d2f3-41ad-917b-47076ea5304d)
<hr>

![Снимок экрана 2025-02-02 093624](https://github.com/user-attachments/assets/a7c5ee5d-f13a-4197-a557-4ff81b1bb849)

<h3>Если перейти в карточку конкретного товара, то заказать ничего не выйдет потому что мы не авторизованы</h3>

![Снимок экрана 2025-02-02 093634](https://github.com/user-attachments/assets/4c17ba3a-33f4-474f-821c-835ea37c0d6b)

<h3>Исправляем ситуацию</h3>

![Снимок экрана 2025-02-02 093745](https://github.com/user-attachments/assets/beac821b-5253-435f-a61e-bca23e73ded1)

<h3>Без сложного пароля не обойтись</h3>

![Снимок экрана 2025-02-02 093758](https://github.com/user-attachments/assets/54a7e2e7-5dc7-4eca-b213-366ee38b83d9)

<h3>Теперь можно перейти в личный кабинет</h3>

![Снимок экрана 2025-02-02 093831](https://github.com/user-attachments/assets/4fc7e6b7-59ee-46ec-a42e-8dc34a893fa8)

<h3>Имеется возможность изменить свои данные или выйти из аккаунта. Изменим email</h3>

![Снимок экрана 2025-02-02 102215](https://github.com/user-attachments/assets/6eec2013-f5b2-4e85-b95d-c3bd0f915035)
<hr>

![Снимок экрана 2025-02-02 102239](https://github.com/user-attachments/assets/18cadaf7-9d39-41ac-b20a-d654b33beb8d)
<hr>

![Снимок экрана 2025-02-02 102247](https://github.com/user-attachments/assets/546cb6f1-e0f5-4a48-8bc0-0383022fd568)

<h3>Вернёмся в каталог и попробуем оформить заказ. Для примера отсортируем модели для мужчин</h3>

![Снимок экрана 2025-02-02 093912](https://github.com/user-attachments/assets/f52e027c-999e-4c11-afcd-c8caea3f2b6d)
<hr>

<h3>Выберем одну из представленных</h3>

![Снимок экрана 2025-02-02 093932](https://github.com/user-attachments/assets/ec615949-5d35-4f30-a74e-ddaf88da6391)
<hr>

![Снимок экрана 2025-02-02 093947](https://github.com/user-attachments/assets/2f5a1e04-b742-452a-bfc4-944aa32d853b)

<h3>Пытаемся заказать 8 пар размера M</h3>

![Снимок экрана 2025-02-02 094003](https://github.com/user-attachments/assets/3c110acb-c683-4820-bfbe-0394adb62988)

<h3>Но не тут то было. Появляется ошибка</h3>

![Снимок экрана 2025-02-02 094010](https://github.com/user-attachments/assets/3ea9d40b-283a-41e8-a760-855802dc6b1b)

<h3>Выбираем иное количество</h3>

![Снимок экрана 2025-02-02 094025](https://github.com/user-attachments/assets/c52aa53c-ec9d-4b35-8e6f-ed592719dece)

<h3>После заказа размера М не осталось, больше заказать его нельзя (до пополнения ассортимента, конечно же)</h3>

![Снимок экрана 2025-02-02 094035](https://github.com/user-attachments/assets/700743b8-5504-4a76-bbbc-ac830fe0479c)

<h3>В личном кабинете теперь появился столбец с ссылкой на страницу заказов</h3>

![Снимок экрана 2025-02-02 094047](https://github.com/user-attachments/assets/69ca84b7-55e3-473c-a627-cb8e3a8502fe)
<hr>

![Снимок экрана 2025-02-02 094055](https://github.com/user-attachments/assets/7b1ea3f8-4bd5-44ff-9401-a4afc1717035)

<h3>Можно или отменить или оплатить заказ</h3>

![Снимок экрана 2025-02-02 094103](https://github.com/user-attachments/assets/2a611db7-000c-4c61-a514-085cf91f457d)

<h3>Посмотрим ID товара и найдём его через базу данных</h3>

![Снимок экрана 2025-02-02 094121](https://github.com/user-attachments/assets/e30fb219-f20b-4f5d-8d87-14d1f36301ba)

<h3>Вот он, размеры пока доступны те же, как и отображалось в карточке товара после заказа</h3>

![Снимок экрана 2025-02-02 094139](https://github.com/user-attachments/assets/5b5ee04b-fd7b-43d3-9b9a-a24b84c0a653)

<h3>Сделаем отмену заказа</h3>

![Снимок экрана 2025-02-02 094146](https://github.com/user-attachments/assets/704620bc-0124-49c8-bab1-859b7c6a4a1f)
<hr>

![Снимок экрана 2025-02-02 094153](https://github.com/user-attachments/assets/2155e1be-4a4c-4e54-8a9f-b8eb032e2002)

<h3>Ещё раз взглянем на товар в базе данных. Всё "вернулось на свои места"</h3>

![Снимок экрана 2025-02-02 094208](https://github.com/user-attachments/assets/84b6e2e3-3144-4440-892f-c7c1a7139595)


<h3>Вернёмся на страницу того товара, который только что был убран из заказа (чтобы не искать его в каталоге, можно нажать на ссылку "отменён" и далее через "повторить" получаем страницу по айди)</h3>

![Снимок экрана 2025-02-02 094229](https://github.com/user-attachments/assets/d5f459bc-35d3-4714-9151-5abf03648086)

<h3>Снова можем заказать размер М</h3>

![Снимок экрана 2025-02-02 094236](https://github.com/user-attachments/assets/5fc2d97b-66ae-4d74-9832-2f083d512153)

<h3>Закажем другой размер для разнообразия</h3>

![Снимок экрана 2025-02-02 094244](https://github.com/user-attachments/assets/25fddfa6-627e-42af-bed1-11b297f611cf)

<h3>Но теперь отменять не станем. "Оплатим"</h3>

![Снимок экрана 2025-02-02 094257](https://github.com/user-attachments/assets/721b6c46-2146-4b06-a61c-a99a965b3460)

<h3>Далее идёт переадресация на страницу оплаты</h3>

![Снимок экрана 2025-02-02 094400](https://github.com/user-attachments/assets/4bf9c37d-4b9f-443a-8308-8cb218ff5c03)

<h3>Валидация данных тоже присутствует</h3>

![Снимок экрана 2025-02-02 104931](https://github.com/user-attachments/assets/614a41cf-d589-4cd5-856c-544cfd29b715)

<h3>После "оплаты" статус заказа, соответственно, меняется как и при его отмене</h3>

![Снимок экрана 2025-02-02 094409](https://github.com/user-attachments/assets/355ae6d7-b379-48ca-b969-0e45b93a268a)


