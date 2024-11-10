import requests

def test_server_1():
    try:
        response = requests.get('http://nginx-server:8080')
        assert response.status_code == 200
        assert response.text == 'Hello from server 1!'
        print("Server 1 test passed! Response content:", response.text)
    except Exception as e:
        print("Server 1 test failed:", e)

def test_server_2():
    try:
        response = requests.get('http://nginx-server:8081')
        assert response.status_code == 404
        assert response.text == 'Server 2 error: Not Found'
        print("Server 2 test passed! Response content:", response.text)
    except Exception as e:
        print("Server 2 test failed:", e)

if __name__ == '__main__':
    test_server_1()
    test_server_2()
