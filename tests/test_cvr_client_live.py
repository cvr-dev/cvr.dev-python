import unittest

from cvr import Client
from cvr.errors import InvalidRequestError
from tests.utils import skip_if_no_api_key, get_api_key


@skip_if_no_api_key
class TestCVRProduktionsenheder(unittest.TestCase):
    def test_adresse_exists(self):
        """ Verifies that at least one produktionsenhed is returned when given an address
        that has produktionsenheder.
        """
        with Client(api_key=get_api_key()) as client:
            produktionsenheder = client.cvr.produktionsenheder(adresse="Prins Jørgens Gård 11")
            self.assertTrue(len(produktionsenheder) > 1)

    def test_adresse_not_exists(self):
        """ Verifies that no produktionsenheder are returned when given an address that has
        no produktionsenheder.
        """
        with Client(api_key=get_api_key()) as client:
            produktionsenheder = client.cvr.produktionsenheder(adresse="aklsdajhk1kj81342")
            self.assertEqual(0, len(produktionsenheder))

    def test_p_nummer_exists(self):
        """ Verifies that a single produktionsenhed is returned when a single p_nummer is given.
        """
        p_nummer = 1004862579
        with Client(api_key=get_api_key()) as client:
            produktionsenheder = client.cvr.produktionsenheder(p_numre=[p_nummer])
            self.assertEqual(1, len(produktionsenheder))
            self.assertEqual(p_nummer, produktionsenheder[0].p_nummer)

    def test_multiple_p_numre_exists(self):
        """ Verifies that multiple produktionsenheder are returned when multiple p_numre are given
        """
        p_numre = [1004862579, 1003388394, 1020852379]
        with Client(api_key=get_api_key()) as client:
            produktionsenheder = client.cvr.produktionsenheder(p_numre=p_numre)
            self.assertEqual(3, len(produktionsenheder))
            for produktionsenhed in produktionsenheder:
                self.assertTrue(produktionsenhed.p_nummer in p_numre)

    def test_p_nummer_not_exists(self):
        """ Verifies that an empty list is returned if the given p numre do not exist.
        """
        with Client(api_key=get_api_key()) as client:
            produktionsenheder = client.cvr.produktionsenheder(p_numre=[1337])
            self.assertEqual(0, len(produktionsenheder))

    def test_p_nummer_exists_and_not_exists(self):
        """ Verifies that an empty list is returned if one of the given p numre do not exist.
        """
        with Client(api_key=get_api_key()) as client:
            produktionsenheder = client.cvr.produktionsenheder(p_numre=[1004862579, 1337])
            self.assertEqual(0, len(produktionsenheder))

    def test_both_p_numre_and_adresse_given(self):
        """ Verifies that InvalidRequestError is raised if both adresse and p_numre
        args are given.
        """
        with Client(api_key=get_api_key()) as client:
            with self.assertRaises(InvalidRequestError):
                client.cvr.produktionsenheder(adresse="adresse", p_numre=[1234])


@skip_if_no_api_key
class TestCVRVirksomheder(unittest.TestCase):
    def test_cvr_nummer_exists(self):
        """ Verifies that a single virksomhed is returned when a single cvr_nummer is given.
        """
        cvr_nummer = 10103940
        with Client(api_key=get_api_key()) as client:
            virksomheder = client.cvr.virksomheder(cvr_numre=[cvr_nummer])
            self.assertEqual(1, len(virksomheder))
            self.assertEqual(cvr_nummer, virksomheder[0].cvr_nummer)

    def test_cvr_nummer_not_exists(self):
        """ Verifies that a no virksomhed is returned when a non-existing cvr_nummer is given.
        """
        with Client(api_key=get_api_key()) as client:
            virksomheder = client.cvr.virksomheder(cvr_numre=[1337])
            self.assertEqual(0, len(virksomheder))

    def test_multiple_cvr_numre_exists(self):
        """ Verifies that multiple virksomheder are returned when multiple cvr_numre are given
        """
        cvr_numre = {10103940, 10150817, 10213231}
        with Client(api_key=get_api_key()) as client:
            virksomheder = client.cvr.virksomheder(cvr_numre=cvr_numre)
            self.assertEqual(3, len(virksomheder))
            for virksomhed in virksomheder:
                self.assertTrue(virksomhed.cvr_nummer in cvr_numre)

    def test_navn_exists(self):
        """ Verifies that at least one virksomhed is returned when given a navn
        that exists.
        """
        with Client(api_key=get_api_key()) as client:
            virksomheder = client.cvr.virksomheder(navn="statsministeriet")
            self.assertTrue(len(virksomheder) > 0)

    def test_navn_not_exists(self):
        """ Verifies that no virksomhed is returned when given a navn that does
        not exist.
        """
        with Client(api_key=get_api_key()) as client:
            virksomheder = client.cvr.virksomheder(navn="kfgnkjdfgkjdgkdfhgkdjhgkdjgkjdfhgkjdfkdfngkdfjn")
            self.assertEqual(0, len(virksomheder))

    def test_navn_and_cvr_numre(self):
        """ Verifies that InvalidRequestError is raised when both navn and
        cvr_numre is given.
        """
        with Client(api_key=get_api_key()) as client:
            with self.assertRaises(InvalidRequestError):
                client.cvr.virksomheder(navn="navn", cvr_numre=[1234])

    def test_cvr_numre_exists_and_not_exists(self):
        """ Verifies that no virksomhed is returned when both existing and non-existing
        cvr_numre are given.
        """
        with Client(api_key=get_api_key()) as client:
            virksomheder = client.cvr.virksomheder(cvr_numre=[10103940, 1337])
            self.assertEqual(0, len(virksomheder))
