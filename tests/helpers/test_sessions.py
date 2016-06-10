from unittest import TestCase
from mock import patch, MagicMock

import frontend.helpers.sessions as module
from lib.irma.common.exceptions import IrmaDatabaseError


class TestSessions(TestCase):

    @patch("frontend.helpers.sessions.db_session")
    def test001_transaction(self, m_db_session):
        with module.session_transaction():
            pass
        m_db_session.commit.assert_called()
        m_db_session.rollback.assert_not_called()
        m_db_session.close.assert_called()

    @patch("frontend.helpers.sessions.db_session")
    def test002_transaction_error(self, m_db_session):
        exception = IrmaDatabaseError
        with self.assertRaises(exception):
            with module.session_transaction():
                raise exception
        m_db_session.commit.assert_not_called()
        m_db_session.rollback.assert_called()
        m_db_session.close.assert_called()

    @patch("frontend.helpers.sessions.db_session")
    def test003_query(self, m_db_session):
        with module.session_query():
            pass
        m_db_session.commit.assert_not_called()
        m_db_session.rollback.assert_not_called()
        m_db_session.close.assert_not_called()

    @patch("frontend.helpers.sessions.db_session")
    def test004_query_error(self, m_db_session):
        exception = IrmaDatabaseError
        with self.assertRaises(exception):
            with module.session_query():
                raise exception
        m_db_session.commit.assert_not_called()
        m_db_session.rollback.assert_not_called()
        m_db_session.close.assert_not_called()
