import pytest

from django.contrib.auth import get_user_model

from buggy.models import Action, Category
from buggy.enums import Priority, State

User = get_user_model()


@pytest.fixture()
def user(db):
    return User.objects.create_user(
        email='test@example.com',
        name='Test User',
        password='password1',
    )


@pytest.fixture()
def category(db):
    return Category.objects.create(
        name='Category',
    )


@pytest.fixture()
def bug(user, category):
    action = Action.build_bug(
        user=user,
        title='title',
        category=category,
        priority=Priority.URGENT,
        state=State.NEW,
    )
    action.commit()
    return action.bug
