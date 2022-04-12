from fastapi import FastAPI
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_book_main():
    response = client.get("/v1/books")
    assert response.status_code == 200
    assert response.json() == [{'title': 'the lord of the rings', 'author': 'J. R. R. Tolkien', 'price': 10.99},{'title':'A Game of Thrones','author':'George R. R. Martin','price':9.99},{'title':'The Name of the Wind','author':'Patrick Rothfuss','price':8.99},{'title':'The Way of Kings','author':'Brandon Sanderson','price':7.99},{'title':'The Lies of Locke Lamora','author':'Scott Lynch','price':6.99},{'title':'The Final Empire','author':'Brandon Sanderson','price':5.99},{'title':'The Eye of the World','author':'Robert Jordan','price':4.99},{'title':'The Blade Itself','author':'Joe Abercrombie','price':3.99},{'title':'The Fellowship of the Ring','author':'J. R. R. Tolkien','price':2.99},{'title':'The Black Prism','author':'Brent Weeks','price':1.99}]

