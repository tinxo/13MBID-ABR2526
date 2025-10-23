import pandas as pd
from pandera.pandas import DataFrameSchema, Column
import pytest

@pytest.fixture
def datos_banco():
    """Fixture para cargar los datos del banco desde un archivo CSV.
    Returns:
        pd.DataFrame: DataFrame que contiene los datos del banco.
    """
    df = pd.read_csv("data/raw/bank-additional-full.csv", sep=';')
    return df


def test_esquema(datos_banco):
    """Test de esquema para el DataFrame de datos_banco.

    Args:
        datos_banco (pd.DataFrame): DataFrame que contiene los datos del banco.
    """
    df = datos_banco
    esquema = DataFrameSchema({
        "age": Column(int, nullable=False),
        "job": Column(str, nullable=False),
        "marital": Column(str, nullable=False),
        "education": Column(str, nullable=False),
        "default": Column(str, nullable=True),
        "housing": Column(str, nullable=False),
        "loan": Column(str, nullable=False),
        "y": Column(str, nullable=False)
        # TODO: completar el resto de columnas
    })

    esquema.validate(df)


def test_basico(datos_banco):
    """Test básico para verificar que el DataFrame de datos_banco no está vacío
    y contiene las columnas esperadas.

    Args:
        datos_banco (pd.DataFrame): DataFrame que contiene los datos del banco.
    """
    df = datos_banco
    # Verificar que el DataFrame no está vacío
    assert not df.empty, "El DataFrame está vacío." 
    # Verificar nulos
    assert df.isnull().sum().sum() == 0, "El DataFrame contiene valores nulos."
    # Verificar cantidad de columnas
    assert df.shape[1] == 21, f"El DataFrame debería tener 21 columnas, pero tiene {df.shape[1]}."


# TODO: agregar al menos una (1) función de tests más con una (1) o más validaciones