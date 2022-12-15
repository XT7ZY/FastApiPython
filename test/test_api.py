from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.main import app, get_db
from src.models import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # Тестовая БД

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)

Base.metadata.drop_all(bind=engine)  # Удалем таблицы из БД
Base.metadata.create_all(bind=engine)  # Создаем таблицы в БД


def override_get_db():
    """
    Данная функция при тестах будет подменять функцию get_db() в main.py.
    Таким образом приложение будет подключаться к тестовой базе данных.
    """
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db  # Делаем подмену
client = TestClient(app)  # создаем тестовый клиент к нашему приложению

def test_create_Client():
    response = client.post(
        "/clients/",
        json={"client_name": "testing", "passport": "111"}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["client_name"] == "testing"

def test_read_client():
    response = client.get("/clients/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data[0]["client_name"] == "testing"

def test_get_client_by_id():
    response = client.get("/clients/1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["client_name"] == "testing"

def test_client_not_found():
    response = client.get("/clients/2")
    assert response.status_code == 404, response.text
    data = response.json()
    assert data["detail"] == "Такого клиента нет"




def test_currency_create():
    response = client.post(
        "/currencies/",
        json={"currency_name": "testing", "currency_rate": "111"}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["currency_name"] == "testing"

def test_read_currency():
    response = client.get("/currencies/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data[0]["currency_name"] == "testing"

def test_get_currency_by_id():
    response = client.get("/currencies/1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["currency_name"] == "testing"

def test_currency_not_found():
    response = client.get("/currencies/2")
    assert response.status_code == 404, response.text
    data = response.json()
    assert data["detail"] == "Такой валюты нет"




def test_cashier_create():
    response = client.post("/cashiers/",
    json={"cashier_name": "testing"}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["cashier_name"] == "testing"

def test_read_cashier():
    response = client.get("/cashiers/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data[0]["cashier_name"] == "testing"

def test_get_cashier_by_id():
    response = client.get("/cashiers/1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["cashier_name"] == "testing"

def test_cashier_not_found():
    response = client.get("/cashiers/2")
    assert response.status_code == 404, response.text
    data = response.json()
    assert data["detail"] == "Такого кассира нет"



def test_create_deal():
    response = client.post("/deal/1/1/1/",
    json={"deal_date": "2020-10-19", "sold": "True", "sum": 120}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["deal_date"] == "2020-10-19"
    assert data["sum"] == 120
    assert data["sold"] == True
    assert data["cashier_id"] == 1
    assert data["client_id"] == 1
    assert data["currency_id"] == 1

def test_get_deal_by_id():
    response = client.get("/deals/1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["deal_date"] == "2020-10-19"

def test_deal_not_found():
    response = client.get("/deals/2")
    assert response.status_code == 404, response.text
    data = response.json()
    assert data["detail"] == "Такой сделки не было"

def test_read_deals():
    response = client.get("/deal/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data[0]["deal_date"] == "2020-10-19"

def test_create_exist_client():
    response = client.post(
        "/clients/",
        json={"client_name": "testing", "passport": "111"}
    )
    assert response.status_code == 400, response.text
    data = response.json()
    assert data["detail"] == "Клиент уже существует"

def test_create_exist_currency():
    response = client.post(
        "/currencies/",
        json={"currency_name": "testing", "currency_rate": "111"}
    )
    assert response.status_code == 400, response.text
    data = response.json()
    assert data["detail"] == "Валюта уже есть"


def test_create_exist_cashier():
    response = client.post(
        "/cashiers/",
        json={"cashier_name": "testing"}
    )
    assert response.status_code == 400, response.text
    data = response.json()
    assert data["detail"] == "Кассир уже существует"

