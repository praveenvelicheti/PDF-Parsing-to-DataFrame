import pytest
  
import project0
from project0 import project0
from project0 import main

url = 'http://normanpd.normanok.gov/filebrowser_download/657/2019-02-14%20Daily%20Arrest%20Summary.pdf'

def test_extract_incidents:
    project0.fetchincidents(url)
    incidents_test = project0.extractincidents()
    assert len(incidents_test[1]) == 9


def test_status:
    project0.fetchincidents(url)
    incidents_test = project0.extractincidents()
    db_test = project0.createdb()
    project0.populatedb(db_test, incidents_test)
   assert  project0.status(db_test) is not None
