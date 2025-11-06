from src.train_model import train_model

def test_train_model():
    assert train_model() is not None

if __name__ == "__main__":
    test_train_model()