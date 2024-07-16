import unittest
from agenda import Agenda, Event

class TestAgenda(unittest.TestCase):
    def setUp(self):
        self.agenda = Agenda()

    def test_add_event(self):
        self.agenda.add_event("Compleanno", "2024-07-20", "Festa di compleanno a casa di Mario")
        self.assertIn("Compleanno", self.agenda.events)
        self.assertIsInstance(self.agenda.events["Compleanno"], Event)

    def test_remove_event(self):
        self.agenda.add_event("Compleanno", "2024-07-20", "Festa di compleanno a casa di Mario")
        self.agenda.remove_event("Compleanno")
        self.assertNotIn("Compleanno", self.agenda.events)

    def test_list_events(self):
        self.agenda.add_event("Compleanno", "2024-07-20", "Festa di compleanno a casa di Mario")
        self.agenda.add_event("Riunione", "2024-07-21", "Riunione di lavoro")
        self.assertEqual(len(self.agenda.events), 2)


if __name__ == "__main__":
    unittest.main()
