import pytest
from project.project import Gym
gym = Gym()

def test_initial_capacity():
    assert gym.capacity == 80


def test_book_class():
    gym.classes['spin'] = []
    gym.book_class("Haile", "yoga")

def test_show_classes():
    gym.classes['spin'] = ['member1']

    gym.show_classes = "\nCurrent Class Booking:\nspin: 1/20 - Available\n"
    ...

