import random

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from core.models.models import Language, Currency, Catalog, Subcatalog, Vacancy, Country, Region, City, User


# ########################################   USER   ############################################### #

async def search_user(session: AsyncSession, user_id: int):
    result = await session.execute(select(User).where(User.id == user_id))

    return result.scalar()


async def create_username(session: AsyncSession):
    while True:
        username = str(random.randint(10000000, 99999999))
        search = await session.execute(select(User).where(User.username == username))
        result = search.scalars().one_or_none()

        if not result:
            return username


async def create_user(session: AsyncSession, user_id, username, first_name, phone_number, language_id, currency_id, country_id) -> None:
    session.add(User(
        id=user_id,
        username=username,
        first_name=first_name,
        phone_number=phone_number,
        language_id=language_id,
        currency_id=currency_id,
        country_id=country_id,
    ))

    await session.commit()


# ########################################   GET DATA   ############################################### #

async def get_language_all(session: AsyncSession):
    query = await session.execute(select(Language))

    return query.scalars().all()


async def get_language_one(session: AsyncSession, language_id=None, language_abbreviation=None):
    if language_id:
        query = await session.execute(select(Language).where(Language.id == language_id))
    else:
        query = await session.execute(select(Language).where(Language.abbreviation == language_abbreviation))

    return query.scalar()


async def get_catalog_all(session: AsyncSession):
    query = await session.execute(select(Catalog))

    return query.scalars().all()


async def get_catalog_one(session: AsyncSession, catalog_id=None, catalog_title=None, catalog_logo=None):
    if catalog_id:
        query = await session.execute(select(Catalog).where(Catalog.id == catalog_id))
    elif catalog_title:
        query = await session.execute(select(Catalog).where(Catalog.title == catalog_title))
    else:
        query = await session.execute(select(Catalog).where(Catalog.logo == catalog_logo))

    return query.scalar()


async def get_subcatalog_all(session: AsyncSession, catalog_id: int):
    query = await session.execute(select(Subcatalog).where(Subcatalog.catalog_id == catalog_id))

    return query.scalars().all()


async def get_subcatalog_one(session: AsyncSession, subcatalog_title: str, catalog_id: int):
    query = await session.execute(
        select(Subcatalog).where(Subcatalog.title == subcatalog_title, Subcatalog.catalog_id == catalog_id)
    )

    return query.scalar()


async def get_country_one(session: AsyncSession, country_id=None, country_name=None):
    if country_id:
        query = await session.execute(select(Country).where(Country.id == country_id))
    else:
        query = await session.execute(select(Country).where(Country.name == country_name))

    return query.scalar()


async def get_country_first(session: AsyncSession):
    query = await session.execute(select(Country))

    return query.scalars().first()


async def get_region_all(session: AsyncSession):
    query = await session.execute(select(Region))

    return query.scalars().all()


async def get_region_one(session: AsyncSession, region_id=None, region_name=None):
    if region_id:
        query = await session.execute(select(Region).where(Region.id == region_id))
    else:
        query = await session.execute(select(Region).where(Region.name == region_name))

    return query.scalar()


async def get_city_all(session: AsyncSession, region_id: int):
    query = await session.execute(select(City).where(City.region_id == region_id))

    return query.scalars().all()


async def get_city_one(session: AsyncSession, city_name: str, region_id: int):
    query = await session.execute(select(City).where(City.name == city_name, City.region_id == region_id))

    return query.scalar()


async def get_currency_one(session: AsyncSession, currency_abbreviation: str):
    query = await session.execute(select(Currency).where(Currency.abbreviation == currency_abbreviation))

    return query.scalar()


async def get_currency_first(session: AsyncSession):
    query = await session.execute(select(Currency))

    return query.scalars().first()


async def get_vacancy_all(session: AsyncSession, subcatalog_id: int):
    query = await session.execute(select(Vacancy).where(Vacancy.subcatalog_id == subcatalog_id))

    return query.scalars().all()


async def get_vacancy_all_active(session: AsyncSession, subcatalog_id: int):
    query = await session.execute(select(Vacancy).where(Vacancy.subcatalog_id == subcatalog_id, Vacancy.active is True))

    return query.scalars().all()


async def get_vacancy_one(session: AsyncSession, vacancy_id: int):
    query = await session.execute(select(Vacancy).where(Vacancy.id == vacancy_id))

    return query.scalar()


async def get_vacancy_one_active(session: AsyncSession, vacancy_id: int):
    query = await session.execute(select(Vacancy).where(Vacancy.id == vacancy_id, Vacancy.active is True))

    return query.scalar()


async def get_user_one(session: AsyncSession, user_id: int):
    query = await session.execute(select(User).where(User.id == user_id))
    user = query.scalar()

    return user


# ########################################   VACANCY   ############################################### #

async def create_vacancy(
        session: AsyncSession,
        subcatalog_id,
        name,
        description,
        experience,
        language,
        disability,
        currency_id,
        price,
        country_id,
        region_id,
        city_id,
        user_id,
) -> None:
    session.add(Vacancy(
        subcatalog_id=subcatalog_id,
        name=name,
        description=description,
        experience=experience,
        language=language,
        disability=disability,
        currency_id=currency_id,
        price=price,
        country_id=country_id,
        region_id=region_id,
        city_id=city_id,
        user_id=user_id,
    ))

    await session.commit()
