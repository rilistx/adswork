connector = {
    'uk': {
        'start_message': '# ###   Ласкаво просимо!   ### #',

        'message': {
            'start': {
                'authorized': 'Вы вже є у системі.',
                'contact': 'Дуже добре! Мы тебе зареєстрували у системі.',
            },

            'menu': {
                'menu': 'Ласкаво просимо до головного меню!',
                'catalog': 'Оберіть категорію вашої професії:',
                'subcatalog': 'Оберіть, ким ви бажаете працювати:',
                'vacancy': 'В цій категорії немає вакансій!',
                'browse': 'Ви не створили ще не обнієї вакансії!',
                'create': 'Бажаєшь створити нову вакансію? Я тобі допоможу!',
                'favorite': 'В тебе поки що не має уподобань(',
                'profile': 'Твій особистий профіль!',
                'about': 'Це інформація о том, хто створив цей бот!',
                'support': 'Я можу тобі чимось допомогти?',
            },

            'vacancy': {
                'create': {
                    'catalog': 'Обери напрямок професії.',
                    'subcatalog': 'Обери професію.',
                    'name': 'Дай короткий опис або назву своеї вакансії.',
                    'description': 'Дай більш детальний опис своеї вакансії.',
                    'experience': 'Можливо працювати віддалено?',
                    'language': 'Потрібно знати іноземну мову?',
                    'disability': 'Можливо працювати інваліду?',
                    'salary': 'Скільки ви будете платити?',
                    'region': 'Оберыть область в якій знаходится ваша компанія.',
                    'city': 'Оберыть місто в якій знаходится ваша компанія.',
                    'finish': 'Дуже добре! Ми зареестрували вашу ваканцію.',
                    'exit': 'Ви повністю відмінили створення!',
                },

                'update': {
                    'catalog': 'Обери напрямок професії. Або залиш старий!',
                    'subcatalog': 'Обери професію. Або залиш старий!',
                    'name': 'Дай короткий опис або назву своеї вакансії. Або залиш старий!',
                    'description': 'Дай більш детальний опис своеї вакансії. Або залиш старий!',
                    'experience': 'Можливо працювати віддалено? Або залиш старий!',
                    'language': 'Потрібно знати іноземну мову? Або залиш старий!',
                    'disability': 'Можливо працювати інваліду? Або залиш старий!',
                    'salary': 'Скільки ви будете платити? Або залиш старий!',
                    'region': 'Оберыть область в якій знаходится ваша компанія. Або залиш старий!',
                    'city': 'Оберыть місто в якій знаходится ваша компанія. Або залиш старий!',
                    'finish': 'Дуже добре! Ми зареестрували вашу ваканцію. Або залиш старий!',
                    'exit': 'Ви повністю відмінили створення! Або залиш старий!',
                },
            },
        },

        'button': {
            'contact': '📱 Мій номер',
            'menu': {
                'catalog': '🗃️ Оголошення',
                'browse': '📌 Мои оголошення',
                'create': '🆕 Створити оголошення',
                'favorite': '⭐️ Обране',
                'profile': '🧑‍💻 Профіль',
                'about': 'ℹ️ Про нас',
                'support': '⚙️ Тех. підтримка',
            },
            'skip': 'Пропустити',
            'yes': 'Так',
            'not': 'Ні',
            'back': 'Назад',
            'exit': 'Вихід',
            'create': 'Создать',
        },

        'catalog': {
            'construction': {
                'name': 'Будівництво',
                'logo': '🧱',
                'subcatalog': {
                    'cranes_man': 'Кранівник',
                    'tiler': 'Плиточник',
                    'fitter': 'Монтажник',
                    'welder': 'Зварювальник',
                    'painter': 'Маляр',
                    'plumber': 'Сантехнік',
                    'facade_man': 'Фасадник',
                    'plasterer': 'Штукатур',
                    'electrician': 'Електрик',
                    'other': 'Інше',
                },
            },
            'medical': {
                'name': 'Медицина',
                'logo': '💊',
                'subcatalog': {
                    'nurse': 'Медсестра',
                    'dentist': 'Стоматолог',
                    'pharmacist': 'Фармацевт',
                    'veterinarian': 'Ветеринар',
                    'other': 'Інше',
                },
            },
            'it': {
                'name': 'АйТі',
                'logo': '🖥',
                'subcatalog': {
                    'sysadmin': 'Сис. Админ',
                    'operator': 'Оператор ПК',
                    'developer': 'Веб Розробник',
                    'gamedev': 'Розробник ігор',
                    'repairman': 'Мастер з ремонту',
                    'other': 'Інше',
                },
            },
            'finances': {
                'name': 'Фінанси',
                'logo': '💰',
                'subcatalog': {
                    'lawyer': 'Юрист',
                    'other': 'Інше',
                },
            },
            'realestate': {
                'name': 'Нерухомість',
                'logo': '🏠',
                'subcatalog': {
                    'realtor': 'Ріелтор',
                    'broker': 'Брокер',
                    'other': 'Інше',
                },
            },
        },

        'country': {
            'uk': {
                'name': 'Україна',
                'region': {
                    'kiev': {
                        'name': 'Києвська',
                        'city': {
                            'kiev': 'Києв',
                        },
                    },
                    'odessa': {
                        'name': 'Одеська',
                        'city': {
                            'odessa': 'Одеса',
                            'izmail': 'Ізмаїл',
                            'southern': 'Южний',
                            'chernomorsk': 'Черноморськ',
                            'sarata': 'Сарата',
                        },
                    },
                    'nikolajev': {
                        'name': 'Миколаївська',
                        'city': {
                            'nikolajev': 'Миколаїв',
                            'ochakov': 'Очаків',
                        },
                    },
                    'lviv': {
                        'name': 'Львівська',
                        'city': {
                            'lviv': 'Львів',
                        },
                    },
                    'vinnytsia': {
                        'name': 'Вінницька',
                        'city': {
                            'vinnytsia': 'Вінниця',
                        },
                    },
                },
            },
        },
    },
}
