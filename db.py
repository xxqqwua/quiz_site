import sqlite3

connect = sqlite3.connect("test.db")
cursor = connect.cursor()
# cursor.execute("DROP TABLE IF EXISTS questions")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS questions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT,
        right_answer TEXT,
        wrong_answer1 TEXT,
        wrong_answer2 TEXT,
        wrong_answer3 TEXT
    )
""")
cursor.execute("DROP TABLE IF EXISTS quiz")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS quiz(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(200),
        age_from INTEGER, 
        age_to INTEGER
    )
""")
# cursor.execute("DROP TABLE IF EXISTS quiz_questions")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS quiz_questions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_question INTEGER,
        id_quiz INTEGER,
        FOREIGN KEY (id_question) REFERENCES questions (id),
        FOREIGN KEY (id_quiz) REFERENCES quiz (id)
    )
""")
cursor.execute('''PRAGMA foreign_keys=on''')

cursor.execute("""INSERT INTO questions (question, 
                                        right_answer, 
                                        wrong_answer1, 
                                        wrong_answer2, 
                                        wrong_answer3)
                    VALUES ("Какой формы Земля?", 
                    "Шарообразная", "Плоская", "Кубовидная", 
                    "В форме пончика")
""")

questions = [
    # ("Какой язык используется для работы с БД?", "SQL", "python", "C++", "java"),
    # ("Каким станет камень если кинуть его в красное море?", "Мокрым", "Красным", "Зелёным", "Сухим"),
    ["Как можно заказать пиццу?", "По телефону", "Через сайт ресторана", "Через социальные сети", "В магазине электроники"],
    ["Как узнать, готова ли уже пицца, которую я заказал?", "Позвонить в ресторан", "Прийти в ресторан и посмотреть", "Получить уведомление на телефон", "Написать на почту ресторана"],
    ["Какие ингредиенты обычно используются для приготовления пиццы?", "Сыр", "Бананы", "Творог", "Апельсины"],
    ["Как долго может занять доставка пиццы?", "30 минут", "10 минут", "1 час", "3 часа"],
    ["Какую температуру должна иметь пицца при доставке?", "Теплая", "Очень горячая", "Холодная", "Комнатная"],
    ["Какие добавки можно заказать к пицце?", "Соус", "Сыр", "Овощи", "Курица"],
    ["Какие промо-коды можно использовать при заказе пиццы?", "Скидка на первый заказ", "Бесплатная бутылка вина", "Скидка при заказе рублейот 1000 гривен", "Бесплатная доставка"],
]

quizzes = [
    ("Как купить пиццу.", 18, 70),
    ("Повросы по програмированию.", 10, 70),
    ("Вопросы на логику.", 6, 17),
]

cursor.executemany("""INSERT INTO quiz
    (        name ,
        age_from , 
        age_to)
        VALUES (?, ?, ?)""", quizzes)

    

cursor.executemany("""INSERT INTO questions 
    (question, right_answer, wrong_answer1, wrong_answer2, wrong_answer3)
    VALUES (?, ?, ?, ?, ?)""", questions)
# cursor.execute("insert into quiz_questions(id_question, id_quiz) VALUES(2,2)")
# cursor.execute("insert into quiz_questions(id_question, id_quiz) VALUES(1,1)")
# cursor.execute("insert into quiz_questions(id_question, id_quiz) VALUES(3,3)")
cursor.execute("insert into quiz_questions(id_question, id_quiz) VALUES(4,1)")
cursor.execute("insert into quiz_questions(id_question, id_quiz) VALUES(5,1)")
cursor.execute("insert into quiz_questions(id_question, id_quiz) VALUES(6,1)")
cursor.execute("insert into quiz_questions(id_question, id_quiz) VALUES(7,1)")
cursor.execute("insert into quiz_questions(id_question, id_quiz) VALUES(8,1)")
cursor.execute("insert into quiz_questions(id_question, id_quiz) VALUES(9,1)")
cursor.execute("insert into quiz_questions(id_question, id_quiz) VALUES(10,1)")


connect.commit()
cursor.execute("SELECT * FROM quiz_questions")
data = cursor.fetchall()
for d in data:
    print(d)