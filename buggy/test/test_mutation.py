from buggy.models import Action, Bug
from buggy.enums import Priority, State
from .fixtures import user, category, bug


def test_create_bug(user, category):
    action = Action.build_bug(
        user=user,
        title='title',
        category=category,
        priority=Priority.URGENT,
        state=State.NEW,
    )
    assert Bug.objects.count() == 0, "the bug should not be created yet"
    action.commit()

    bug = Bug.objects.get()
    assert bug.title == 'title'
    assert bug.category == category
    assert bug.priority == Priority.URGENT
    assert bug.state == State.NEW
    assert bug.created_by == user


def test_edit_bug(user, bug):
    action = Action.build(bug=bug, user=user)
    action.set_title('new title')

    assert bug.actions.count() == 1, "Action should not be created yet"

    action.commit()

    assert bug.actions.count() == 2
    bug.refresh_from_db()
    assert bug.title == 'new title'


def test_operations(user, bug):
    action = Action.build(bug=bug, user=user)
    assert list(action.operations) == []

    op1 = action.add_comment('bar')
    assert list(action.operations) == [op1]

    op2 = action.set_title('foo')
    assert list(action.operations) == [op1, op2]

    action.commit()
    assert list(action.operations) == [op1, op2]

    action.refresh_from_db()
    assert list(action.operations) == [op1, op2]
