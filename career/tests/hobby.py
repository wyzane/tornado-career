import requests
from unittest import TestCase


class TestHobby(TestCase):

    def setUp(self):
        base_url = "localhost:8001/api/v1/hobby/{}"
        self.create_url = base_url.format("create")
        self.list_url = base_url.format("list")
        self.update_url = base_url.format("update")
        self.delete_url = base_url.format("delete")

    def tearDown(self):
        print("----- test finish -----")

    def test_hobby_create(self):
        pass

    def test_hobby_list(self):
        pass

    def test_hobby_update(self):
        pass

    def test_hobby_delete(self):
        pass

