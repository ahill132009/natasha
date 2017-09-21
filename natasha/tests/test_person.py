# coding: utf-8
from __future__ import unicode_literals

import pytest

from natasha.grammars.person import Person
from natasha.grammars.name import Name
from natasha import PersonExtractor


@pytest.fixture(scope='module')
def extractor():
    return PersonExtractor()


tests = [
    [
        'президент Николя Саркози',
        Person(
            position='президент',
            name=Name(
                first='николя', last='саркози',
                middle=None, nick=None
            )
        )
    ],
    [
        'Пресс-секретарь Михаил Леонтьев',
        Person(
            position='Пресс-секретарь',
            name=Name(
                first='михаил', last='леонтьев',
                middle=None, nick=None
            )
        )
    ]
]


@pytest.mark.parametrize('test', tests)
def test_extractor(extractor, test):
    text = test[0]
    etalon = test[1:]
    guess = [_.fact for _ in extractor(text)]
    assert guess == etalon
