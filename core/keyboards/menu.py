from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton

from core.utils.connector import connector


class MenuCallBack(CallbackData, prefix="main"):
    lang: str | None = None
    user_id: int | None = None
    method: str | None = None
    view: str | None = None
    level: int | None = None
    key: str | None = None
    data: str | None = None
    page: int = 1
    catalog_id: int | None = None
    subcatalog_id: int | None = None
    vacancy_id: int | None = None


def get_menu_button(
        lang: str,
        level: int,
        blocked: bool,
        admin: bool,
):
    keyboard = InlineKeyboardBuilder()

    for callback, text in connector[lang]['button']['menu'].items():
        if callback == 'catalog' and not blocked:
            keyboard.add(
                InlineKeyboardButton(
                    text=text,
                    callback_data=MenuCallBack(
                        lang=lang,
                        method=None,
                        level=level + 1,
                        key=callback,
                    ).pack()
                )
            )
        elif callback == 'browse' and not blocked:
            keyboard.add(
                InlineKeyboardButton(
                    text=text,
                    callback_data=MenuCallBack(
                        lang=lang,
                        method=None,
                        view='your',
                        level=3,
                        key='view',
                    ).pack()
                )
            )
        elif callback == 'create' and not blocked:
            keyboard.add(
                InlineKeyboardButton(
                    text=text,
                    callback_data=MenuCallBack(
                        lang=lang,
                        method='create',
                        level=10,
                        key='confirm_user',
                    ).pack()
                )
            )
        elif callback == 'favorite' and not blocked:
            keyboard.add(
                InlineKeyboardButton(
                    text=text,
                    callback_data=MenuCallBack(
                        lang=lang,
                        method=None,
                        view='liked',
                        level=3,
                        key='view',
                    ).pack()
                )
            )
        elif callback == 'profile' and not blocked:
            keyboard.add(
                InlineKeyboardButton(
                    text=text,
                    callback_data=MenuCallBack(
                        lang=lang,
                        method=None,
                        level=20,
                        key=callback,
                    ).pack()
                )
            )
        elif callback == 'about' and not blocked:
            keyboard.add(
                InlineKeyboardButton(
                    text=text,
                    callback_data=MenuCallBack(
                        lang=lang,
                        method=None,
                        level=30,
                        key=callback,
                    ).pack()
                )
            )
        elif callback == 'support':
            keyboard.add(
                InlineKeyboardButton(
                    text=text,
                    url="https://t.me/rilistx",
                )
            )
        elif callback == 'admin' and admin:
            keyboard.add(
                InlineKeyboardButton(
                    text=text,
                    callback_data=MenuCallBack(
                        lang=lang,
                        method=None,
                        level=40,
                        key=callback,
                    ).pack()
                )
            )

    sizes = ([1, 1, 1, 2, 2] + ([1] if admin else [])) if not blocked else [1]

    return keyboard.adjust(*sizes).as_markup()


def get_profession_button(
        lang: str,
        level: int,
        data_name: str,
        data_list: list,
        catalog_title: str | None = None,
):
    keyboard = InlineKeyboardBuilder()

    for item in data_list:
        if data_name == 'catalog':
            keyboard.add(
                InlineKeyboardButton(
                    text=connector[lang][data_name][item.title]['logo'] + ' ' + connector[lang][data_name][item.title]['name'],
                    callback_data=MenuCallBack(
                        lang=lang,
                        level=level + 1,
                        key='subcatalog',
                        catalog_id=item.id,
                    ).pack()
                )
            )
        else:
            keyboard.add(
                InlineKeyboardButton(
                    text=connector[lang]['catalog'][catalog_title][data_name][item.title],
                    callback_data=MenuCallBack(
                        lang=lang,
                        view='all',
                        level=level + 1,
                        key='view',
                        catalog_id=item.catalog_id,
                        subcatalog_id=item.id,
                    ).pack()
                )
            )

    if data_name == 'subcatalog':
        keyboard.add(
            InlineKeyboardButton(
                text=connector[lang]['button']['back'],
                callback_data=MenuCallBack(
                    lang=lang,
                    level=level - 1,
                    key='catalog',
                ).pack()
            )
        )

    keyboard.add(
        InlineKeyboardButton(
            text=connector[lang]['button']['exit'],
            callback_data=MenuCallBack(
                lang=lang,
                level=0,
                key='menu',
            ).pack()
        )
    )

    sizes = ([2 for _ in range(len(data_list) // 2)] + ([1] if len(data_list) % 2 else []) +
             ([2] if data_name == 'subcatalog' else [1]))

    return keyboard.adjust(*sizes).as_markup()


def get_vacancy_button(
        lang: str,
        view: str,
        level: int,
        key: str,
        page: int,
        catalog_id: int,
        subcatalog_id: int,
        pagination_button: dict,
        vacancy_id: int,
        counter: [int] = 0,
):
    keyboard = InlineKeyboardBuilder()

    for text, menu_name in pagination_button.items():
        if menu_name == "next":
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(
                    lang=lang,
                    view=view,
                    level=level,
                    key=key,
                    page=page + 1,
                    catalog_id=catalog_id,
                    subcatalog_id=subcatalog_id,
                ).pack()
            ))
            counter += 1
        elif menu_name == "previous":
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(
                    lang=lang,
                    view=view,
                    level=level,
                    key=key,
                    page=page - 1,
                    catalog_id=catalog_id,
                    subcatalog_id=subcatalog_id,
                ).pack()
            ))
            counter += 1

    if vacancy_id:
        keyboard.add(InlineKeyboardButton(
            text='Просмотреть',
            callback_data=MenuCallBack(
                lang=lang,
                view=view,
                level=level + 1,
                key='description',
                page=page,
                catalog_id=catalog_id,
                subcatalog_id=subcatalog_id,
                vacancy_id=vacancy_id,
            ).pack()
        ))

    if view == 'complaint':
        keyboard.add(InlineKeyboardButton(
            text=connector[lang]['button']['back'],
            callback_data=MenuCallBack(
                lang=lang,
                level=40,
                key='admin',
            ).pack()
        ))
    if view == 'all':
        keyboard.add(InlineKeyboardButton(
            text=connector[lang]['button']['back'],
            callback_data=MenuCallBack(
                lang=lang,
                level=level - 1,
                key='subcatalog',
                catalog_id=catalog_id,
            ).pack()
        ))

    keyboard.add(InlineKeyboardButton(
        text=connector[lang]['button']['exit'],
        callback_data=MenuCallBack(
            lang=lang,
            level=0,
            key='menu',
        ).pack()
    ))

    sizes = ([counter] if counter else []) + ([1] if vacancy_id else []) + ([2] if view == 'all' or view == 'complaint' else [1])

    return keyboard.adjust(*sizes).as_markup()


def get_description_button(
        lang: str,
        view: str,
        level: int,
        key: str,
        page: int,
        catalog_id: int,
        subcatalog_id: int,
        vacancy_id: int,
        liked_id: int,
        complaint_id: int,
        deactivate: bool,
        your_vacancy: bool,
        # count_complaint: int,
):
    keyboard = InlineKeyboardBuilder()

    if view == 'complaint':
        keyboard.add(InlineKeyboardButton(
            text='Заблокувати юзера',
            callback_data=MenuCallBack(
                lang=lang,
                method='blocked',
                view=view,
                level=10,
                key='confirm_admin',
                page=page,
                catalog_id=catalog_id,
                subcatalog_id=subcatalog_id,
                vacancy_id=vacancy_id,
            ).pack()
        ))

        keyboard.add(InlineKeyboardButton(
            text='Активировать',
            callback_data=MenuCallBack(
                lang=lang,
                method='activate',
                view=view,
                level=10,
                key='confirm_admin',
                page=page,
                catalog_id=catalog_id,
                subcatalog_id=subcatalog_id,
                vacancy_id=vacancy_id,
            ).pack()
        ))

        keyboard.add(InlineKeyboardButton(
            text='Деактивировать',
            callback_data=MenuCallBack(
                lang=lang,
                method='deactivate',
                view=view,
                level=10,
                key='confirm_admin',
                page=page,
                catalog_id=catalog_id,
                subcatalog_id=subcatalog_id,
                vacancy_id=vacancy_id,
            ).pack()
        ))

        sizes = [1, 2]
    elif not your_vacancy and view == 'all' or not your_vacancy and view == 'liked':
        keyboard.add(InlineKeyboardButton(
            text='Убрать из избранного' if liked_id else 'В избранное',
            callback_data=MenuCallBack(
                lang=lang,
                method='favorite',
                view=view,
                level=level,
                key=key,
                page=page,
                catalog_id=catalog_id,
                subcatalog_id=subcatalog_id,
                vacancy_id=vacancy_id,
            ).pack()
        ))
        keyboard.add(InlineKeyboardButton(
            text='Убарть жалобу' if complaint_id else 'Пожаловаться',
            callback_data=MenuCallBack(
                lang=lang,
                method='feedback',
                view=view,
                level=level,
                key=key,
                page=page,
                catalog_id=catalog_id,
                subcatalog_id=subcatalog_id,
                vacancy_id=vacancy_id,
            ).pack()
        ))

        sizes = [1, 1]
    else:
        if 5:
            keyboard.add(InlineKeyboardButton(
                text='Деактивировать' if deactivate else 'Активировать',
                callback_data=MenuCallBack(
                    lang=lang,
                    method='deactivate' if deactivate else 'activate',
                    view=view,
                    level=10,
                    key='confirm_user',
                    page=page,
                    catalog_id=catalog_id,
                    subcatalog_id=subcatalog_id,
                    vacancy_id=vacancy_id,
                ).pack()
            ))

            keyboard.add(InlineKeyboardButton(
                text='Изменить',
                callback_data=MenuCallBack(
                    lang=lang,
                    method='update',
                    view=view,
                    level=10,
                    key='confirm_user',
                    page=page,
                    catalog_id=catalog_id,
                    subcatalog_id=subcatalog_id,
                    vacancy_id=vacancy_id,
                ).pack()
            ))

        keyboard.add(InlineKeyboardButton(
            text='Удалить',
            callback_data=MenuCallBack(
                lang=lang,
                method='delete',
                view=view,
                level=10,
                key='confirm_user',
                page=page,
                catalog_id=catalog_id,
                subcatalog_id=subcatalog_id,
                vacancy_id=vacancy_id,
            ).pack()
        ))

        sizes = [1, 2]

    keyboard.add(InlineKeyboardButton(
        text=connector[lang]['button']['back'],
        callback_data=MenuCallBack(
            lang=lang,
            view=view,
            level=level - 1,
            key='view',
            page=page,
            catalog_id=catalog_id,
            subcatalog_id=subcatalog_id,
        ).pack()
    ))
    keyboard.add(InlineKeyboardButton(
        text=connector[lang]['button']['exit'],
        callback_data=MenuCallBack(
            lang=lang,
            level=0,
            key='menu',
        ).pack()
    ))

    sizes += [2]

    return keyboard.adjust(*sizes).as_markup()


def get_confirm_button(
        lang: str,
        method: str,
        view: str,
        key: str,
        page: int,
        catalog_id: int | None = None,
        subcatalog_id: int | None = None,
        vacancy_id: int | None = None,
        sizes: tuple[int] = (2,),
):
    keyboard = InlineKeyboardBuilder()

    if key == 'confirm_admin':
        keyboard.add(InlineKeyboardButton(
            text=connector[lang]['button'][key][method],
            callback_data=MenuCallBack(
                lang=lang,
                method=method,
                view=view,
                level=3,
                key='moderation',
                page=page,
                catalog_id=catalog_id,
                subcatalog_id=subcatalog_id,
                vacancy_id=vacancy_id,
            ).pack()
        ))
    else:
        keyboard.add(InlineKeyboardButton(
            text=connector[lang]['button'][key][method],
            callback_data=MenuCallBack(
                lang=lang,
                method=method,
                view=view,
                key='vacancy',
                page=page,
                catalog_id=catalog_id,
                subcatalog_id=subcatalog_id,
                vacancy_id=vacancy_id,
            ).pack()
        ))

    keyboard.add(InlineKeyboardButton(
        text=connector[lang]['button']['cancel'],
        callback_data=MenuCallBack(
            lang=lang,
            view=None if method == 'create' else view,
            level=0 if method == 'create' else 4,
            key='menu' if method == 'create' else 'description',
            page=1 if method == 'create' else page,
            catalog_id=None if method == 'create' else catalog_id,
            subcatalog_id=None if method == 'create' else subcatalog_id,
            vacancy_id=None if method == 'create' else vacancy_id,
        ).pack()
    ))

    return keyboard.adjust(*sizes).as_markup()


def get_profile_button(
        lang: str,
        level: int,
):
    keyboard = InlineKeyboardBuilder()

    keyboard.add(InlineKeyboardButton(
        text='Настройки профиля',
        callback_data=MenuCallBack(
            lang=lang,
            level=level + 1,
            key='setting',
        ).pack()
    ))
    keyboard.add(InlineKeyboardButton(
        text=connector[lang]['button']['exit'],
        callback_data=MenuCallBack(
            lang=lang,
            level=0,
            key='menu',
        ).pack()
    ))

    sizes = [1, 1]

    return keyboard.adjust(*sizes).as_markup()


def get_setting_button(
        lang: str,
        level: int,
        first_name: str | None = None,
):
    keyboard = InlineKeyboardBuilder()

    keyboard.add(InlineKeyboardButton(
        text='Изменить имя' if first_name else 'Добавить имя',
        callback_data=MenuCallBack(
            lang=lang,
            level=level,
            key='change',
            data='name',
        ).pack()
    ))
    keyboard.add(InlineKeyboardButton(
        text=connector[lang]['button']['back'],
        callback_data=MenuCallBack(
            lang=lang,
            level=level - 1,
            key='profile',
        ).pack()
    ))

    keyboard.add(InlineKeyboardButton(
        text=connector[lang]['button']['exit'],
        callback_data=MenuCallBack(
            lang=lang,
            level=0,
            key='menu',
        ).pack()
    ))

    sizes = [1, 2]

    return keyboard.adjust(*sizes).as_markup()


def get_about_button(
        lang: str,
):
    keyboard = InlineKeyboardBuilder()

    keyboard.add(InlineKeyboardButton(
        text='Задонатить',
        url="https://t.me/wadsworkuk",
    ))
    keyboard.add(InlineKeyboardButton(
        text='Наш канал',
        url="https://t.me/wadsworkuk",
    ))
    keyboard.add(InlineKeyboardButton(
        text=connector[lang]['button']['exit'],
        callback_data=MenuCallBack(
            lang=lang,
            level=0,
            key='menu',
        ).pack()
    ))

    sizes = [1, 2]

    return keyboard.adjust(*sizes).as_markup()


def get_admin_button(
        lang: str,
):
    keyboard = InlineKeyboardBuilder()

    keyboard.add(
        InlineKeyboardButton(
            text='text',
            callback_data=MenuCallBack(
                lang=lang,
                view='complaint',
                level=3,
                key='view',
            ).pack()
        )
    )
    keyboard.add(
        InlineKeyboardButton(
            text=connector[lang]['button']['exit'],
            callback_data=MenuCallBack(
                lang=lang,
                level=0,
                key='menu',
            ).pack()
        )
    )

    sizes = [1, 1]

    return keyboard.adjust(*sizes).as_markup()
