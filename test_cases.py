import pytest
import pymssql


@pytest.fixture
def conn():
    conn = pymssql.connect(  
            server='EPBYMINW06C5\SQLEXPRESS',
            port= '1433',
            user='TestUser3',
            password='TestUser3',
            database='TRN'
        )
    yield conn
    
@pytest.fixture
def cursor(conn):
    cursor = conn.cursor(as_dict=True)
    yield cursor
    conn.rollback()
    
def test_Row_Count_countries(cursor):
    cursor.execute('select * from TRN.hr.countries;')
    rs = cursor.fetchall()
    assert len(rs) == 25
    
def test_No_Duplicated_Rows_Countries(cursor):
    cursor.execute('select count(*) as Count from (select * from TRN.hr.countries) test EXCEPT select count(*) as Count from (select distinct * from TRN.hr.countries) test2;')
    rs = cursor.fetchall()
    assert len(rs) == 0
